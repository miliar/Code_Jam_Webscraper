#include <iostream>

const int MaxN = 101;
using namespace std;

double e[MaxN], s[MaxN], g[MaxN][MaxN];
double dis[MaxN][MaxN];

int main() {
    int total_case;
    cin >> total_case;
    for (int test_case = 1; test_case <= total_case; ++test_case) {
        int n, q;
        cin >> n >> q;
        for (int i = 1; i <= n; ++i) {
            cin >> e[i] >> s[i];
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                cin >> g[i][j];
                if (g[i][j] < 0) g[i][j] = 1e20;
                dis[i][j] = 1e20;
            }
            g[i][i] = dis[i][i] = 0;
        }
        for (int k = 1; k <= n; ++k) {
            for (int i = 1; i <= n; ++i) {
                for (int j = 1; j <= n; ++j) {
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
                }
            }
        }
        /*for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                cout << g[i][j] << " ";
            }
            cout << "\n";
        }*/
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (g[i][j] <= e[i]) {
                    dis[i][j] = g[i][j] / s[i];
                }
            }
        }
        for (int k = 1; k <= n; ++k) {
            for (int i = 1; i <= n; ++i) {
                for (int j = 1; j <= n; ++j) {
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
                }
            }
        }
        cout << "Case #" << test_case << ":";
        for (int i = 1; i <= q; ++i) {
            int u, v;
            cin >> u >> v;
            printf(" %.10f", dis[u][v]);
            // cout << " " << dis[u][v];
        }
        cout << "\n";
    }
}
