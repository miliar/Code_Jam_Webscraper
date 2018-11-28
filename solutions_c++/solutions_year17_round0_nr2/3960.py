#include<cstdio>

int chk(int a)
{
    int tmp;
    while(a!=0)
    {
         tmp = a%10;
        a/=10;
        if(tmp == 0)return true;
        if(tmp < a%10)return true;
    }
    return false;
}

main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        int a;
        scanf("%d",&a);
        while(chk(a))a--;
        printf("Case #%d: %d\n",i+1,a);
    }
}
