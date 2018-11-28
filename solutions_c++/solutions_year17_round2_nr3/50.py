#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, q;
double e[111], s[111];
double d[111][111];

vector<int> v[111];
vector<double> w[111];

int f[111];
double g[111];
priority_queue<pair<double,int>> h;

void solve(int x) {
    cin >> n >> q;
    for (int i = 1; i <= n; i++) cin >> e[i] >> s[i];
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> d[i][j];
            if (d[i][j] == -1) d[i][j] = 1e15;
        }
    }
    for (int k = 1; k <= n; k++) {
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                d[a][b] = min(d[a][b],d[a][k]+d[k][b]);
            }
        }
    }
    
    for (int i = 1; i <= n; i++) {
        v[i].clear();
        w[i].clear();
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == j) continue;
            if (d[i][j] > e[i]) continue;
            v[i].push_back(j);
            w[i].push_back(d[i][j]/s[i]);
        }
    }
    cout << "Case #" << x << ": ";
    for (int i = 1; i <= q; i++) {
        int u, z;
        cin >> u >> z;
        for (int j = 1; j <= n; j++) {
            f[j] = 0;
            g[j] = 1e15;
        }
        g[u] = 0;
        while (h.size()) h.pop();
        h.push({0,u});
        while (h.size()) {
            auto x = h.top(); h.pop();
            int xs = x.second;
            double xe = -x.first;
            if (f[xs]) continue;
            f[xs] = 1;
            for (int j = 0; j < v[xs].size(); j++) {
                if (g[xs]+w[xs][j] < g[v[xs][j]]) {
                    g[v[xs][j]] = g[xs]+w[xs][j];
                    h.push({-g[v[xs][j]], v[xs][j]});
                }
            }
        }
        printf("%.9lf ", g[z]);
    }
    printf("\n");
    cerr << "Case #" << x << " ready\n";
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}
