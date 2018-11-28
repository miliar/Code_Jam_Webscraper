#include <bits/stdc++.h>

using namespace std;

const int MX_SZ = 104;
const long double INF = 1e+18 + 42;
long long d[MX_SZ][MX_SZ];

void solve(int t) {
    cout << "Case #" << t << ": ";
    int n, q;
    cin >> n >> q;
    vector<pair<long long, long double>> h(n);
    for (int i = 0; i < n; ++i) {
        cin >> h[i].first >> h[i].second;
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> d[i][j];
        }
    }
    int v, u;
    cin >> v >> u;
    long double ans[MX_SZ];
    fill(ans, ans + MX_SZ, INF);
    ans[n - 1] = 0;
    for (int i = n - 2; i >= 0; --i) {
        long double cd = 0;
        for (int j = i + 1; j < n; ++j) {
            cd += d[j - 1][j];
            if (cd > h[i].first) {
                break;
            }
            ans[i] = min(ans[i], ans[j] + (cd / h[i].second));
        }
    }
    cout << setprecision(32) << ans[0] << endl;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
}
