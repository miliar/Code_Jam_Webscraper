#include<bits/stdc++.h>

using namespace std;

bool is[1005];

bool test(int x)
{
    int last=10;
    int now=0;
    while(x)
    {
        now=x%10;
        x/=10;
        if(now>last)
            return false;
        last=now;
    }
    return true;
}


int main()
{
    freopen("./B-small-attempt0.in","r",stdin);
    int T;
    for(int i=1;i<=1000;++i)
        is[i]=test(i);
    scanf("%d",&T);
    for(int cas=1;cas<=T;++cas)
    {
        int now;
        scanf("%d",&now);
        for(int j=now;j>=1;--j)
        {
            if(is[j])
            {
                printf("Case #%d: %d\n",cas,j);
                break;
            }
        }
    }
    return 0;
}
