#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

#define LL long long

using namespace std;

inline void work()
{
    int n, q;
    scanf("%d%d", &n, &q);
    
    LL dis[n + 1], spd[n + 1];
    for (int i = 1; i <= n; ++i)
    {
        scanf("%lld%lld", &dis[i], &spd[i]);
    }
    
    LL g0[n + 1][n + 1];
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            scanf("%lld", &g0[i][j]);
            if (i == j) g0[i][j] = 0;
        }
    }
    
    for (int k = 1; k <= n; ++k)
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
            {
                if (g0[i][k] != -1 && g0[k][j] != -1)
                {
                    if (g0[i][j] == -1 || g0[i][k] + g0[k][j] < g0[i][j])
                    {
                        g0[i][j] = g0[i][k] + g0[k][j];
                    }
                }
            }
    
    double g1[n + 1][n + 1];
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            if (i == j)
            {
                g1[i][j] = 0.0;
                continue;
            }
            if (g0[i][j] == -1 || g0[i][j] > dis[i])
            {
                g1[i][j] = 1e12;
                continue;
            }
            g1[i][j] = 1.0 * g0[i][j] / spd[i];
        }
    }
    
    for (int k = 1; k <= n; ++k)
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
            {
                if (g1[i][k] + g1[k][j] < g1[i][j])
                {
                    g1[i][j] = g1[i][k] + g1[k][j];
                }
            }
    
    for (int i = 1; i <= q; ++i)
    {
        int x, y;
        scanf("%d%d", &x, &y);
        printf("%.10f", g1[x][y]);
        if (i == q) printf("\n"); else printf(" ");
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i)
    {
        printf("Case #%d: ", i);
        work();
    }
}
