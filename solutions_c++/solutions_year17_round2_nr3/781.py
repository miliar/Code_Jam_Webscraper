#include <cstdio>
#include <cmath>

const int maxn = 1e2 + 10;

int E[maxn], S[maxn], d[maxn][maxn];
double dp[maxn];

int main()
{
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++kase)
    {
        int N, Q;
        scanf("%d %d", &N, &Q);
        for (int i = 1; i <= N; ++i)
            scanf("%d %d", &E[i], &S[i]);
        for (int i = 1; i <= N; ++i)
            for (int j = 1; j <= N; ++j)
                scanf("%d", &d[i][j]);
        scanf("%*d %*d");
        for (int i = 1; i <= N; ++i)
            dp[i] = 1e233;
        dp[1] = 0;
        for (int i = 1; i < N; ++i)
        {
            long long sum = 0;
            for (int j = i + 1; j <= N; ++j)
            {
                sum += d[j - 1][j];
                if (sum > E[i])
                    break;
                dp[j] = fmin(dp[j], dp[i] + 1.0 * sum / S[i]);
            }
        }
        printf("Case #%d: %.10f\n", kase, dp[N]);
    }
    return 0;
}