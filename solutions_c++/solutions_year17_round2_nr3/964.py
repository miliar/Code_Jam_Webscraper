#include <iostream>
#include <vector>

using namespace std;


const int maxn = 1e3;

long double d[maxn][maxn];
long double dist[maxn];
bool used[maxn];

void solve() {
    int n = 0;
    int q = 0;
    cin >> n;
    cin >> q;
    vector < long double > ei, si;
    for (int i = 0; i < n; i++) {
        long double eei, ssi;
        cin >> eei >> ssi;
        ei.push_back(eei);
        si.push_back(ssi);
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            d[i][j] = 1e18;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> d[i][j];
            if (d[i][j] == -1)
                d[i][j] = 1e18;
        }
    }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
    cout.precision(10);
    while (q--) {
        int u, v;
        cin >> u >> v;
        u--;
        v--;
        for (int i = 0; i < n; i++)
            dist[i] = 1e18;
        dist[u] = 0;
        for (int i = 0; i < n; i++) {
            used[i] = false;
        }
        for (int i = 0; i < n; i++) {
            int bc = -1;
            for (int j = 0; j < n; j++) {
                if (used[j])
                    continue;
                if (bc == -1)
                    bc = j;
                if (dist[j] < dist[bc])
                    bc = j;
            }
            used[bc] = true;
            for (int k = 0; k < n; k++) {
                if (d[bc][k] <= ei[bc]) {
                    dist[k] = min(dist[k], dist[bc] + d[bc][k] / si[bc]);
                }
            }
        }
        cout << fixed << dist[v] << " ";

    }
    cout << endl;
}

int main() {
    int test = 0;
    cin >> test;
    for (int t_id = 1; t_id <= test; t_id++) {
        cout << "Case #" << t_id << ": ";
        solve();
    }
    return 0;
}