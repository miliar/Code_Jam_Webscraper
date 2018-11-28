#include <stdio.h>
double ans[101];
long long e[101],v[101],dis[101][101];
long long td[101];
main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("Cs1.txt","w",stdout);
    long long t; scanf("%lld",&t);
    long long n,q;
    for(long long tt = 1;tt <= t;tt++)
    {
        scanf("%lld %lld",&n,&q);
        for(long long i = 0;i < n;i++)
            scanf("%lld %lld",&e[i],&v[i]);
        for(long long i = 0;i < n;i++)
        for(long long j = 0;j < n;j++)
            scanf("%lld",&dis[i][j]);
        scanf("%lld %lld");
        ans[0] = 0;
        td[0] = 0;
        for(long long i = 1;i < n;i++)
            td[i] = td[i-1] + dis[i-1][i];
        for(long long i = 1;i < n;i++)
        {
            ans[i] = ans[i-1] + ((double)dis[i-1][i]) / v[i-1];
            for(long long j = i-2;j >= 0;j--)
            {
                if(e[j] >= td[i]-td[j])
                {
                    if(ans[j] + ((double)(td[i]-td[j])) / v[j] < ans[i])
                        ans[i] = ans[j] + (double)(td[i]-td[j]) / v[j];
                }
            }
        }
        printf("Case #%lld: %f\n",tt,ans[n-1]);
    }
}
