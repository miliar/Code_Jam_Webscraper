#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 720 + 5;

int dp[maxn][maxn][2][2], used[maxn * 2];

void upmin(int &a, int b)
{
    a = min(a, b);
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("answer.out", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--)
    {
        memset(used, -1, sizeof(used));
        memset(dp, 0x3f, sizeof(dp));
        int n, m;
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; ++i)
        {
            int s, t;
            scanf("%d%d", &s, &t);
            for(int j = s; j < t; ++j) used[j] = 0;
        }
        for(int i = 0; i < m; ++i)
        {
            int s, t;
            scanf("%d%d", &s, &t);
            for(int j = s; j < t; ++j) used[j] = 1;
        }
        dp[0][0][0][0] = dp[0][0][1][1] = 0;
        for(int i = 0; i <= 720; ++i)
        {
            for(int j = 0; j <= 720; ++j)
            {
                for(int k = 0; k < 2; ++k)
                {
                    for(int l = 0; l < 2; ++l)
                    {
                        if(i < 720 && used[i + j] != 0) upmin(dp[i + 1][j][k][0], dp[i][j][k][l] + l);
                        if(j < 720 && used[i + j] != 1) upmin(dp[i][j + 1][k][1], dp[i][j][k][l] + (l ^ 1));
                    }
                }
            }
        }
        int ans = 0x3f3f3f3f;
        for(int i = 0; i < 2; ++i) for(int j = 0; j < 2; ++j) upmin(ans, dp[720][720][i][j] + (i ^ j));
        printf("Case #%d: ", ++cas);
        printf("%d\n", ans);
    }
    return 0;
}
