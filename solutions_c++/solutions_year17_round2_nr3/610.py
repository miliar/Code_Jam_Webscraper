#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

const int N = 1e2 + 7;

int n, q;
LL e[N], s[N], d[N][N];
long double dp[N][N];

int main()
{
    int te; scanf("%d", &te);
    for(int t = 1; t <= te; t++)
    {
        scanf("%d%d", &n, &q);
        for(int i = 1; i <= n; i++)
        {
            scanf("%lld%lld", &e[i], &s[i]);
        }
        for(int i = 1; i <= n; i++)
        {
            for(int j = 1; j <= n; j++)
            {
                scanf("%lld", &d[i][j]);
                if(d[i][j] == -1) d[i][j] = 1e18 + 7;
            }
        }
        for(int u = 1; u <= n; u++)
        {
            for(int a = 1; a <= n; a++)
            {
                for(int b = 1; b <= n; b++)
                {
                    d[a][b] = min(d[a][b], d[a][u] + d[u][b]);
                }
            }
        }
        for(int i = 1; i <= n; i++)
        {
            for(int j = 1; j <= n; j++)
                dp[i][j] = 1e18 + 7;
            dp[i][i] = 0;
        }
        for(int i = 1; i <= n; i++)
        {
            for(int j = 1; j <= n; j++)
            {
                if(d[i][j] <= e[i])
                {
                    dp[i][j] = min(dp[i][j], (long double)d[i][j] / (long double)s[i]);
                }
            }
        }
        for(int u = 1; u <= n; u++)
        {
            for(int a = 1; a <= n; a++)
            {
                for(int b = 1; b <= n; b++)
                {
                    dp[a][b] = min(dp[a][b], dp[a][u] + dp[u][b]);
                }
            }
        }
        printf("Case #%d:", t);
        while(q--)
        {
            int a, b; scanf("%d%d", &a, &b);
            printf(" %.6Lf", dp[a][b]);
        }
        puts("");
    }
    return 0;
}
