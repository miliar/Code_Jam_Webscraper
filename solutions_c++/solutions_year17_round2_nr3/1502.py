#include <bits/stdc++.h>

using namespace std;

const int maxn = 2000;
const long double INF = 1e18;


long double d[maxn];
long double ans[maxn];
int u[maxn], v[maxn];
int e[maxn], s[maxn];

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    cout.precision(20);
    for (int z = 0; z < t; ++z) {
        int n, q;
        cin >> n >> q;
        for (int i = 0; i < n; ++i) {
            cin >> e[i] >> s[i];
        }
        d[0] = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int x;
                cin >> x;
                if (x > -1) {
                    d[j] = d[i] + x;
                }

            }
        }
        for (int i = 0; i < q; ++i) {
            cin >> u[i] >> v[i];
        }

        ans[0] = 0;
        for (int i = 1; i < n; ++i) ans[i] = INF;
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (e[j] < d[i] - d[j]) continue;
                ans[i] = min(ans[i], ans[j] + (d[i] - d[j]) / s[j]);
            }
        }

        cout << "Case #" << z + 1 << ": " << ans[n - 1] << "\n";

    }



    return 0;
}
