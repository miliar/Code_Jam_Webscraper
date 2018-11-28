#include <bits/stdc++.h>

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define forn(i, n) for(int i=0;i<(n);++i)
#define clr(ar, val) memset(ar, val, sizeof(ar))

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<ld, ld> point;

const int MAXN = 111;
const int INF = int(1e9) + 7;
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

int test, iter;
int n, q;
vector<pair<long double, long double>> h;
vector<vector<long long>> d(MAXN, vector<long long>(MAXN, 0));
vector<long double> dp(MAXN), ans;
vector<bool> used(MAXN);

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> test;

    for (int iter = 1; iter <= test; iter++) {
        h.clear();
        cin >> n >> q;
        for (int i = 0; i < n; i++) {
            int e, s;
            cin >> e >> s;
            h.push_back({e, s});
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> d[i][j];
            }
        }
        for (int i = 0; i < n; i++) {
            d[i][i] = 0;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (d[i][j] == -1) {
                    d[i][j] = LINF;
                }
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (d[i][k] < LINF && d[k][j] < LINF) {
                        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                    }
                }
            }
        }

        ans.clear();
        for (int it = 0; it < q; it++) {
            int u, v;
            cin >> u >> v;
            u--; v--;
            for (int i = 0; i < n; i++) {
                dp[i] = LINF;
                used[i] = false;
            }

            dp[u] = 0;
            for (int it = 0; it < n; it++) {
                int cur = -1;
                for (int j = 0; j < n; j++) {
                    if (!used[j] && (cur == -1 || dp[j] < dp[cur])) {
                        cur = j;
                    }
                }
                used[cur] = true;

                for (int t = 0; t < n; t++) {
                    long long dist = d[cur][t];
                    if (cur == t || dist > h[cur].first) {
                        continue;
                    }

                    long double tt = static_cast<long double>(dist) / h[cur].second;
                    dp[t] = min(dp[t], dp[cur] + tt);
                }
            }

            ans.push_back(dp[v]);
        }
        cout << "Case #" << iter << ": " << setprecision(18);
        for (auto x : ans) {
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}
