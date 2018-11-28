// Kappa 123
#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define FILE "file"

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int INF = numeric_limits<int>::max();
const ll LLINF = numeric_limits<ll>::max();
const ull ULLINF = numeric_limits<ull>::max();
const double PI = acos(-1.0);

long long e[110];
long long s[110];
long long d[110][110];
double dp[110][110];

int main()
{
    freopen(FILE".in", "r", stdin);
    freopen(FILE".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int tcase = 1; tcase <= T; tcase++)
    {
        int n, q;
        cin >> n >> q;
        for(int i = 0; i < n; i++)
            cin >> e[i] >> s[i];
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                cin >> d[i][j];
                if(d[i][j] == -1)
                    d[i][j] = LLINF;
                dp[i][j] = 1e18;
                if(i == j)
                    dp[i][j] = 0, d[i][j] = 0;
            }
        }
        for(int k = 0; k < n; k++)
        {
            for(int i = 0; i < n; i++)
            {
                for(int j = 0; j < n; j++)
                {
                    if(d[i][k] < LLINF && d[k][j] < LLINF)
                        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                }
            }
        }
//        for(int i = 0; i < n; i++)
//        {
//            for(int j = 0; j < n; j++)
//                cout << (d[i][j] == LLINF ? -1 : d[i][j]) << " ";
//            cout << endl;
//        }
        for(int k = 0; k < n; k++)
        {
            for(int i = 0; i < n; i++)
            {
                for(int j = 0; j < n; j++)
                {
                    if(d[i][k] <= e[i] && d[k][j] <= e[k])
                    {
                        dp[i][j] = min(dp[i][j], 1.0 * d[i][k] / s[i] + 1.0 * d[k][j] / s[k]);
                    }
                }
            }
        }
        for(int k = 0; k < n; k++)
        {
            for(int i = 0; i < n; i++)
            {
                for(int j = 0; j < n; j++)
                {
                    if(dp[i][k] < 1e18 && dp[k][j] < 1e18)
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
                }
            }
        }
        cout << "Case #" << tcase << ": ";
        while(q--)
        {
            int a, b;
            cin >> a >> b;
            a--, b--;
            cout << setprecision(10) << fixed << dp[a][b] << " ";
        }
        cout << '\n';
    }
    return 0;
}
