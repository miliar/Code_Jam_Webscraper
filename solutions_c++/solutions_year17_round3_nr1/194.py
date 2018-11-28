#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

const double pi = acos(-1.0);
struct Pancake
{
    int r,h;
    bool operator < (const Pancake &it) const
    {
        return 2*pi*r*h>2*pi*it.r*it.h;
    }
}pancake[1010];

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t,n,k;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d%d",&n,&k);
        for (int i=1;i<=n;++i)
        {
            scanf("%d%d",&pancake[i].r,&pancake[i].h);
        }
        sort(pancake+1,pancake+n+1);
        double ans=0,tmp=0;
        for (int i=1;i<=n;++i)
        {
            tmp=0;
            int left=k-1;
            for (int j=1;left>0&&j<=n;++j)
            {
                if (i!=j&&pancake[j].r<=pancake[i].r)
                {
                    tmp+=2*pi*pancake[j].r*pancake[j].h;
                    --left;
                }
            }
            tmp+=2*pi*pancake[i].r*pancake[i].h;
            tmp+=pi*pancake[i].r*pancake[i].r;
            if (left==0) ans=max(ans,tmp);
        }
        printf("Case #%d: %.9f\n",cas,ans);
    }
    return 0;
}
