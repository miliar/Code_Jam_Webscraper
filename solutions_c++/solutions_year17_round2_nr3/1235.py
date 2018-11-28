#include <bits/stdc++.h>
#define LL long long

using namespace std;

LL e[112],s[112],d[112];
double dp[112];

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,x,n,q;
    double ans;

    scanf("%d",&t);

    for(int z = 1; z <= t; ++z)
    {
        ans = 0;

        scanf("%d%d",&n,&q);

        for(int i = 0; i < n; ++i)
        {
            scanf("%lld%lld",&e[i],&s[i]);
            dp[i] = -1;
        }
        dp[0] = 0;

        for(int i = 0; i < n; ++i)
        {
            for(int j = 0; j < n; ++j)
            {
                scanf("%d",&x);
                if(x != -1) d[i] = x;
            }
        }
        d[n-1] = -1;

        scanf("%d%d",&x,&q);

        for(int i = 0; i < n-1; ++i)
        {
            int j = i;
            LL now = 0;
            now += d[j];
            while(j < n-1 && now <= e[i])
            {
                j++;
                if(dp[j] == -1 || dp[j] > dp[i]+now*1.0/s[i])
                    dp[j] = dp[i]+now*1.0/s[i];
                now += d[j];
            }
        }

        printf("Case #%d: %.10f\n",z,dp[n-1]);
    }

    return 0;
}
