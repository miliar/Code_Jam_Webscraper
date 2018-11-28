#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

typedef pair<double, double> pdd;

bool dequals(double d1, double d2) {
    return fabs(d1 -d2) < 1e-6;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        int n;
        int Q;
        cin >> n >> Q;
        vector<pdd> horses(n);
        for (int i = 0; i < n; i++) {
            int e, s;
            cin >> e >> s;
            horses[i] = pdd(e, s);
        }
        vector< vector<double> > graph(n, vector<double>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> graph[i][j];
            }
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (!dequals(-1, graph[i][k]) && !dequals(-1, graph[k][j])) {
                        if (dequals(graph[i][j], -1)|| graph[i][k] + graph[k][j] < graph[i][j]) {
                            graph[i][j] = graph[i][k] + graph[k][j];
                        }
                    }
                }
            }
        }
        vector< vector<bool> > reach(n, vector<bool>(n));
        double BIG = 200000000000;
        vector< vector<double> > dp(n, vector<double>(n, BIG));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {   
                if (i != j && !dequals(graph[i][j], -1) && (graph[i][j] < horses[i].first || dequals(graph[i][j], horses[i].first))) {
                    reach[i][j] = true;
                    dp[i][j] = min(dp[i][j], graph[i][j] / horses[i].second);
                }
            }
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
                }
            }
        }
        for (int q = 0; q < Q; q++) {
            int u, v;
            cin >> u >> v;
            u--;
            v--;
            cout << setprecision(20) << dp[u][v] << (q == Q - 1 ? '\n' : ' ');
        }
    }
    return 0;
}