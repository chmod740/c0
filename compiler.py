import sys, re
from enum import Enum

class Compiler:
    """
    关键字
    """
    key = ('^printf+$', '^scanf+$', "^if+$", "^else+$", "^for+$", r"^int+$", "^return+$", "^static+$",
           r"^void+$", r"^while+$", r'^\++$', r'^\-+$', r'^\*+$', r'^/+$', r'^==+$', r'^=+$', r'^>=+$',
           r'^<=+$', r'^>+$', r'^<+$', r'^\(+$',
           r'^\)+$', r'^{+$', r'^}+$', r'^[0-9a-zA-Z]+$', r'^[0-9][0-9]+$', r'^,+$', r'^;+$', r'^:+$')
    # key = ('^printf', '^scanf', "^if", "^else", "^for", r"^int+$", "^return", "static",
    #        "void", "while", r'\+', r'\-', r'\*', '/', '==', '=', '>=', '<=', '>', '<', r'\(',
    #        r'\)', r'{', r'{', r'[a-zA-Z][a-zA-Z0-9]{0,10}', r'[0-9][0-9]{0,10}', ',', ';', ':')
    """
    符号
    """
    class Sym(Enum):
        printfsym = 0
        scanfsym = 1
        ifsym = 2
        elsesym = 3
        forsym = 4
        intsym = 5
        returnsym = 6
        staticsym = 7
        voidsym = 8
        whilesym = 9
        pulssym = 10
        subsym = 11
        mulsym = 12
        divsym = 13
        dengdengsym = 14
        dengsym = 15
        dayudengyusym = 16
        xiaoyudengyusym = 17
        dayusym = 18
        xiaoyusym = 19
        zuoxiaokuohaosym = 20
        youxiaokuohaosym = 21
        zuodakuohaosym = 22
        youdakuohaosym = 23
        identsym = 24
        numbersym = 25
        douhaosym = 26
        fenhaosym = 27
        maohaosym = 28

    """
    源文件的文件名
    """
    source_file_name = ''
    """
    全部的代码
    """
    all_source_code = None

    """
    词法分析的结果，为语法分析作准备
    """
    sym_list = []

    def lexical_analysis(self, filename):
        # 读入文件内容
        self.source_file_name = sys.path[0] + '/' + filename
        self.get_all_source_code()
        # 得到词法分析的结果
        self.get_sym_list()

        for element in self.sym_list:
            print(element)


    def get_sym_list(self):
        sym = self.get_char()
        while sym is not None:
            self.sym_list.append(sym)
            sym = self.get_char()
        return self.sym_list
    """
    得到单词
    """
    def get_char(self):
        # if self.all_source_code is None:
        #     self.get_all_source_code()

        self.format_all_source_code()
        if len(self.all_source_code) == 0:
            return None
        for i in range(10):
            i = i + 1
            if i > len(self.all_source_code):
                break
            find_flag = True
            match_count = 0
            for express in self.key:
                results = re.findall(express, self.all_source_code[0: i])
                if len(results) > 0:
                    s = self.all_source_code[0:i]
                    match_count = match_count + 1

            if match_count == 0:
                find_flag = False
                sym = self.all_source_code[0: int(i-1)]
                all_source_code_length = len(self.all_source_code)
                self.all_source_code = self.all_source_code[i-1: all_source_code_length]
                return self.get_sym(sym)

    def get_sym(self, s):
        i = 0
        for express in self.key:
            if len(re.findall(express, s)) > 0:
                return self.Sym(i)
            i = i + 1

    """
    得到文件的所有内容
    """
    def get_all_source_code(self):
        if self.all_source_code is None:
            self.all_source_code = ''
        file = open(self.source_file_name)
        source_code_temp = ''
        while file.readable():
            source_code_temp = file.readline()
            if source_code_temp is None or source_code_temp == '':
                break
            self.all_source_code = self.all_source_code + source_code_temp
        self.all_source_code = str(self.all_source_code).replace('\t', '').replace('\n', ' ') + " "
        return self.all_source_code
    def format_all_source_code(self):
        if len(self.all_source_code) > 0:
            if self.all_source_code[0] == ' ' or self.all_source_code[0] == '\n':
                self.all_source_code = self.all_source_code[1: len(self.all_source_code)]
                self.format_all_source_code()