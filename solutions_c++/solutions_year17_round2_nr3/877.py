#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl
#define pb push_back
using namespace std;
typedef long long ll;


const int MAXN = 1005;
const double INF = 1000000000000000;
void cans(int test, double ans)
{
    cout << "Case #" << test << ": " << ans << endl;
}


double dp[MAXN];
double d[MAXN][MAXN];
double c[MAXN];
double s[MAXN];
double e[MAXN];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cout << setprecision(10) << fixed;

    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        int n, q;
        cin >> n >> q;
        for (int i = 1; i <= n; i++)
        {
            cin >> e[i] >> s[i];
        }
        c[1] = 0;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
                cin >> d[i][j];
            c[i+1] = c[i] + d[i][i+1];
        }



        for (int i = 0; i < q; i++)
        {
            int u, v;
            cin >> u >> v;

            dp[n] = 0;
            for (int i = 1; i < n; i++) dp[i] = INF;
            for (int i = n-1; i >= 1; i--)
            {
                for (int j = i+1; j <= n && c[i] + e[i] >= c[j]; j++)
                {
                    dp[i] = min(dp[i], (c[j] - c[i])/s[i] + dp[j]);
                }
            }
        }



        cans(tt, dp[1]);
    }



    return 0;
}


