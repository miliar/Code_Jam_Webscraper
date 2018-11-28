#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

const double eps = 1e-12;

int N, K;
double U;
double p[55];
double dp[55][55];

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
        scanf("%d%d", &N, &K);
        cin >> U;
        for(int i = 1; i <= N; i++) cin >> p[i];

        sort(p + 1, p + N + 1);
        reverse(p + 1, p + N + 1);

        double st = 0.0;
        double dr = 1.0;
        double val = 0.0;
        while(st <= dr)
        {
            double mij = st + (dr - st) / 2.0;

            double cnt = 0.0;
            for(int i = 1; i <= K; i++)
                if(p[i] < mij)  cnt += mij - p[i];

            if( U - cnt > eps || fabs(U - cnt) <= eps )
            {
                val = mij;
                st = mij + eps;
            }
            else
                dr = mij - eps;
        }

        for(int i = 1; i <= K; i++)
            p[i] = max(p[i], val);

        dp[0][0] = 1.0;
        for(int i = 1; i <= N; i++)
        {
            dp[i][0] = dp[i - 1][0] * (1.0 - p[i]);
            for(int j = 1; j <= i; j++)
                dp[i][j] =  dp[i - 1][j] * (1.0 - p[i]) +
                            dp[i - 1][j - 1] * p[i];
        }

        double ans = 0.0;
        for(int i = K; i <= N; i++) ans += dp[N][i];

        cout << fixed << setprecision(10) << ans << "\n";
    }

    return 0;
}
