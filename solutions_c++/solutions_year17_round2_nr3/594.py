#include <bits/stdc++.h>

using std::cin;
using std::cout;
using std::cerr;
using std::ios_base;
using std::fixed;
using std::endl;

using std::pair;
using std::make_pair;
using std::swap;

using std::string;
using std::vector;
using std::map;
using std::set;

using std::sort;
using std::reverse;

#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define sqr(x) ((x) * (x))

const int MAXN = 105;
const int INF = 1e9;
const int MOD = 1e9+7;
const long long L_INF = 4e18;
const long double EPS = 1e-10;

int T;
int n, q;
long long d[MAXN][MAXN];
long long e[MAXN], s[MAXN];
long double dp[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    srand(566);

    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        cin >> n >> q;
        for (int i = 0; i < n; i++)
            cin >> e[i] >> s[i];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> d[i][j];
                if (d[i][j] == -1)
                    d[i][j] = L_INF;
            }
            d[i][i] = 0;
        }
        
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    d[i][j] = std::min(d[i][j], d[i][k] + d[k][j]);

        while (q--) {
            int v, u;
            cin >> v >> u;
            v--, u--;

            for (int i = 0; i < n; i++)
                dp[i] = L_INF;
            dp[v] = 0;

            for (int k = 0; k < n; k++) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (e[j] < d[j][i])
                            continue;
                        dp[i] = std::min(dp[i], dp[j] + 1.0 * d[j][i] / s[j]);
                    }
                }
            }
            cout << dp[u] << ' ';
        }
        cout << '\n';
    }

#ifdef LOCAL
    cerr << "\n== " << 1.0 * clock() / CLOCKS_PER_SEC << " sec.\n";
#endif
    return 0;
}
