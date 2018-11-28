#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, q;
        cin >> n >> q;
        vector<pair<int, int>> pony(n);
        for (int i = 0; i < n; i++) {
            cin >> pony[i].first >> pony[i].second;
        }
        vector<vector<double>> dis(n, vector<double>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> dis[i][j];
                if (dis[i][j] == -1) {
                    dis[i][j] = 1e20;
                }
            }
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
                }
            }
        }
        vector<vector<double>> ct(n, vector<double>(n, 1e20));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dis[i][j] <= pony[i].first) {
                    ct[i][j] = min(ct[i][j], dis[i][j] / pony[i].second);
                }
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    ct[i][j] = min(ct[i][j], ct[i][k] + ct[k][j]);
                }
            }
        }

        cout << "Case #" << t << ":";
        for (int i = 0; i < q; i++) {
            int bg, ed;
            cin >> bg >> ed;
            cout << ' ' << fixed << setprecision(6) << ct[bg - 1][ed - 1];
        }
        cout << endl;
    }
}
