#include <cstdio>
bool tidy(int x)
{
    int tmp=x%10;
    x/=10;
    while(x)
    {
        if(x%10>tmp)
            return 0;
        tmp=x%10;
        x/=10;
    }
    return 1;
}
int main()
{
    int T,n;
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        scanf("%d",&n);
        int ans=1;
        for(int t=2;t<=n;++t)
            if(tidy(t))
                ans=t;
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
