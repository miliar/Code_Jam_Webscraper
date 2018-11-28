#include <iostream>
#include <iomanip>
#include <utility>
#include <vector>

using namespace std;

const long long INF = 1000000000000000;

typedef long long ll;

struct Horse {
    long long dist;
    long long speed;
};

void run_floyd(vector<vector<long long>> &d) {
    for (size_t i = 0; i < d.size(); ++i) {
        for (size_t u = 0; u < d.size(); ++u) {
            for (size_t v = 0; v < d.size(); ++v) {
                d[u][v] = min(d[u][v], d[u][i] + d[i][v]);
            }
        }
    }
}

void relax(const int a, const int b, long double time,
           vector<vector<long double>> &ans) {
    for (size_t u = 0; u < ans.size(); ++u) {
        for (size_t v = 0; v < ans.size(); ++v) {
            ans[u][v] = min(ans[u][v],
                            ans[u][a] + time + ans[b][v]);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    for (int testCase = 0; testCase < T; ++testCase) {
        int n, q;
        cin >> n >> q;
        vector<Horse> horses(n);
        for (auto &h : horses) {
            cin >> h.dist >> h.speed;
        }
        vector<vector<long long>> d(n, vector<long long>(n));
        for (auto &line : d) {
            for (auto &el : line) {
                cin >> el;
                if (el == -1) {
                    el = INF;
                }
            }
        }
        run_floyd(d);
        vector<vector<long double>> ans(n, vector<long double>(n, INF));
        for (int i = 0; i < n; ++i) {
            ans[i][i] = 0;
        }
        for (int a = 0; a < n; ++a) {
            for (int b = 0; b < n; ++b) {
                if (a != b && d[a][b] <= horses[a].dist) {
                    relax(a, b, d[a][b] / (long double)horses[a].speed, ans);
                }
            }
        }
        cout << "Case #" << testCase + 1 << ": ";
        cout << fixed << setprecision(20);
        for (; q > 0; --q) {
            int u, v;
            cin >> u >> v;
            u--, v--;
            cout << ans[u][v] << " ";
        }
        cout << endl;
    }
    return 0;
}
