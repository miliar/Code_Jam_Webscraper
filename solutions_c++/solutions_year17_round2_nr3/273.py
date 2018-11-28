#include <iostream>
#include <vector>
#include <utility>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

using LL = long long;
using LD = long double;

const LL INF = 1e18;


int main () {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);
    cout.setf(std::ios_base::fixed);
    cout.precision(8);
    cerr.setf(std::ios_base::fixed);
    cerr.precision(25);
    int tt;
    cin >> tt;
    for (int t = 0; t < tt; ++t) {
        int n, m;
        cin >> n >> m;
        vector < pair < LL, LD > > horses(n);
        for (int i = 0; i < n; ++i) {
            cin >> horses[i].first >> horses[i].second;
        }
        vector < vector < LL > > gr(n, vector < LL > (n));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> gr[i][j];
            }
        }
        vector < vector < LD > > dist(n, vector < LD > (n));
        for (int st = 0; st < n; ++st) {
            vector < LL > d (n, INF);
            d[st] = 0;
            vector < char > u (n);
            for (int i = 0; i < n; ++i) {
                int v = -1;
                for (int j = 0; j < n; ++j) {
                    if (!u[j] && (v == -1 || d[j] < d[v])) {
                        v = j;
                    }
                }
                if (d[v] == INF) {
                    break;
                }
                u[v] = true;
                for (size_t to = 0; to < gr[v].size(); ++to) {
                    LL len = gr[v][to];
                    if (len == -1) {
                        continue;
                    }
                    if (d[v] + len < d[to]) {
                        d[to] = d[v] + len;
                    }
                }
            }
            for (int i = 0; i < n; ++i) {
                if (d[i] <= horses[st].first) {
                    dist[st][i] = d[i] / horses[st].second;
                } else {
                    dist[st][i] = INF;
                }
            }
        }
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
        cout << "Case #" << t + 1 << ": ";
        for (int i = 0; i < m; ++i) {
            int a, b;
            cin >> a >> b;
            a--; b--;
            cout << dist[a][b] << " ";
        }
        cout << "\n";
    }
    return 0;
}


