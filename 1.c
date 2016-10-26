int a ;
void ax()
{
    printf(a);
    a = 4;
}
void main()
{
    a = 3;
    ax();
    printf(a);
}
void main()
{
        int m,n,r,q,a;
        scanf(m);
        scanf(n);
        r=1;
        a=3;
        while(a)
        {
        while(r)
        {
        q=m/n;
        r=m-q*n;
        m=n;
        n=r;
        }
        printf(m);
        a=a-1;
        }
}