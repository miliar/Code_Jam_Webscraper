#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, q;
        cin >> n >> q;
        vector<pair<int, int>> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i].first >> a[i].second;
        }

        const long long inf = 1ll << 50;
        vector<vector<long long>> d(n, vector<long long>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int val;
                cin >> val;
                d[i][j] = val == -1 ? inf : val;
            }
            d[i][i] = 0;
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                }
            }
        }

        vector<vector<long double>> tm(n, vector<long double>(n, inf));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                long long dist = d[i][j];
                if (dist <= a[i].first) {
                    tm[i][j] = (long double)dist/a[i].second;
                }
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    tm[i][j] = min(tm[i][j], tm[i][k] + tm[k][j]);
                }
            }
        }

        cout << "Case #" << t << ":";
        while (q--) {
            int v, u;
            cin >> v >> u;
            cout << fixed << setprecision(10) << " " << tm[v-1][u-1];
        }
        cout << endl;
    }
}



