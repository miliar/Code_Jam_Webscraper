#include <cstdio>
#include <algorithm>

using namespace std;

int dp[111][111][111][4];
int cnt[4];

int main()
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        int N, P;
        scanf("%d %d", &N, &P);
        for (int i = 0; i < 4; ++i)
            cnt[i] = 0;
        for (int i = 0; i < N; ++i)
        {
            int G;
            scanf("%d", &G);
            ++cnt[G % P];
        }
        int ans = cnt[0];
        for (int i = 0; i <= N + 1; ++i)
            for (int j = 0; j <= N + 1; ++j)
                for (int k = 0; k <= N + 1; ++k)
                    for (int l = 0; l < P; ++l)
                        dp[i][j][k][l] = -1e9;
        dp[0][0][0][0] = 0;
        int last = (cnt[1] + cnt[2] * 2 + cnt[3] * 3) % P;
        for (int i = 0; i <= cnt[1]; ++i)
            for (int j = 0; j <= cnt[2]; ++j)
                for (int k = 0; k <= cnt[3]; ++k)
                    for (int l = 0; l < P; ++l)
                    {
                        dp[i + 1][j][k][(l + 1) % P] = max(dp[i + 1][j][k][(l + 1) % P], dp[i][j][k][l] + (l == 0));
                        dp[i][j + 1][k][(l + 2) % P] = max(dp[i][j + 1][k][(l + 2) % P], dp[i][j][k][l] + (l == 0));
                        dp[i][j][k + 1][(l + 3) % P] = max(dp[i][j][k + 1][(l + 3) % P], dp[i][j][k][l] + (l == 0));
                    }
        static int kase = 1;
        printf("Case #%d: %d\n", kase, ans + dp[cnt[1]][cnt[2]][cnt[3]][last]);
        ++kase;
    }
    return 0;
}