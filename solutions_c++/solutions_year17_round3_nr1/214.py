#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

typedef long double LD;
typedef pair<int, int> pii;

const double PI = atan(1.0) * 4.0;

int N, K;
long double dp[1005][1005];
long double mxx[1005][1005];
pii pk[1005];

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
        for(int i = 1; i <= N; i++)
        {
            int rr, hh;
            scanf("%d%d", &rr, &hh);
            pk[i] = {rr, hh};
        }
        sort(pk + 1, pk + N + 1);
        reverse(pk + 1, pk + N + 1);

        for(int i = 1; i <= N; i++)
        {
            int r = pk[i].first;
            int h = pk[i].second;
            dp[i][1] = (LD)1LL * PI * r * r;
            dp[i][1] += (LD)1LL * 2 * PI * r * h;
            mxx[i][1] = max(mxx[i - 1][1], dp[i][1]);
            for(int j = 2; j <= K; j++)
            {
                dp[i][j] = 0.0;
                LD addh = 1LL * 2 * PI * r * h;
                dp[i][j] = mxx[i - 1][j - 1] + addh;
                mxx[i][j] = max(mxx[i - 1][j], dp[i][j]);
            }
        }

        LD ans = mxx[N][K];
        cout << fixed << setprecision(10) << ans << "\n";
    }

    return 0;
}
