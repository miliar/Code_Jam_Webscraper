#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<queue>
#include<vector>
#include<fstream>
#define inf 1000000000
using namespace std;
int dp[1444][722][2][2];
int h[1444];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, i, j, k, g, l, r, n, m, ans;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas)
    {
        scanf("%d%d", &n, &m);
        for(i = 0; i <= 1440; ++i)
        {
            for(j = 0; j <= 720; ++j)
            {
                for(k = 0; k <= 1; ++k)
                {
                    for(g = 0; g <= 1; ++g)
                        dp[i][j][k][g] = inf;
                }
            }
        }
        memset(h, 0, sizeof(h));
        for(i = 1; i <= n; ++i)
        {
            scanf("%d%d", &l, &r);
            for(j = l + 1; j <= r; ++j)
                h[j] = 1;
            /*if(r == 1440)
                h[0] = 1;
            if(l == 0)
                h[1440] = 1;*/
        }
        for(i = 1; i <= m; ++i)
        {
            scanf("%d%d", &l, &r);
            for(j = l + 1; j <= r; ++j)
                h[j] = 2;
            /*if(r == 1440)
                h[0] = 2;
            if(l == 0)
                h[1440] = 2;*/
        }
        if(h[1] == 1)
        {
            dp[1][1][0][0] = 0;
        }else
        if(h[1] == 2)
        {
            dp[1][0][1][1] = 0;
        }else
        {
            dp[1][1][0][0] = dp[1][0][1][1] = 0;
        }
        for(i = 2; i <= 1440; ++i)
        {
            for(j = 0; j <= 720; ++j)
            {
                if(h[i] == 1)
                {
                    if(j != 0)
                    {
                        dp[i][j][0][0] = min(dp[i - 1][j - 1][0][0], dp[i - 1][j - 1][1][0] + 1);
                        dp[i][j][0][1] = min(dp[i - 1][j - 1][0][1], dp[i - 1][j - 1][1][1] + 1);
                    }
                }else
                if(h[i] == 2)
                {
                    dp[i][j][1][0] = min(dp[i - 1][j][1][0], dp[i - 1][j][0][0] + 1);
                    dp[i][j][1][1] = min(dp[i - 1][j][1][1], dp[i - 1][j][0][1] + 1);
                }else
                {
                    if(j != 0)
                    {
                        dp[i][j][0][0] = min(dp[i - 1][j - 1][0][0], dp[i - 1][j - 1][1][0] + 1);
                        dp[i][j][0][1] = min(dp[i - 1][j - 1][0][1], dp[i - 1][j - 1][1][1] + 1);
                    }
                    dp[i][j][1][0] = min(dp[i - 1][j][1][0], dp[i - 1][j][0][0] + 1);
                    dp[i][j][1][1] = min(dp[i - 1][j][1][1], dp[i - 1][j][0][1] + 1);
                }
            }
        }
        dp[1440][720][0][1]++;
        dp[1440][720][1][0]++;
        int t1 = min(dp[1440][720][0][0], dp[1440][720][0][1]);
        int t2 = min(dp[1440][720][1][0], dp[1440][720][1][1]);
        printf("Case #%d: %d\n", cas, min(t1, t2));
    }
    return 0;
}
/*
1
0 0
*/
