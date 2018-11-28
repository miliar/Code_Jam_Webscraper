#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

typedef pair<int, int> pii;

const int INF = (1 << 30) - 1;

int A, B;
pii a[105], b[105];
int who[2005];
int dp[2005][2005][2][2];  /// dp[i][j][k][s] - minim suntem la minutul i, k a stat j minute, este randul lui k, am inceput cu s

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; test++)
    {
        printf("Case #%d: ", test);

        for(int i = 0; i <= 24 * 60; i++)    who[i] = -1;

        scanf("%d%d", &A, &B);
        for(int i = 1; i <= A; i++)
        {
            int st, dr;
            scanf("%d%d", &st, &dr);
            st++; dr++;
            a[i] = {st, dr - 1};
            for(int j = st; j < dr; j++)    who[j] = 1;
        }
        for(int i = 1; i <= B; i++)
        {
            int st, dr;
            scanf("%d%d", &st, &dr);
            a[i] = {st, dr - 1};
            st++; dr++;
            for(int j = st; j < dr; j++)    who[j] = 0;
        }

        dp[1][1][0][1] = INF;
        dp[1][1][1][0] = INF;
        dp[1][0][0][0] = dp[1][0][1][1] = dp[1][0][1][0] = dp[1][0][0][1] = INF;

        int M = 24 * 60;

        for(int i = 2; i <= M; i++)
            for(int k = 0; k <= 1; k++)
                for(int s = 0; s <= 1; s++)
                {
                    if(who[i] == (1 ^ k) || who[0] == (s ^ 1) )
                    {
                        for(int j = 0; j <= M / 2; j++)   dp[i][j][k][s] = INF;
                        continue;
                    }
                    for(int j = 1; j <= i && j <= M / 2; j++)
                        dp[i][j][k][s] = min(dp[i - 1][j - 1][k][s], dp[i - 1][ (i - 1) - (j - 1) ][k ^ 1][s] + 1);
                    dp[i][0][k][s] = INF;
                    for(int j = M / 2 + 1; j <= i; j++)
                        dp[i][j][k][s] = INF;
                }

        int ans1 = min(dp[M][M / 2][0][0], dp[M][M / 2][0][1] + 1);
        int ans2 = min(dp[M][M / 2][1][1], dp[M][M / 2][1][0] + 1);
        int ans = min(ans1, ans2);
        printf("%d\n", ans);
    }

    return 0;
}
