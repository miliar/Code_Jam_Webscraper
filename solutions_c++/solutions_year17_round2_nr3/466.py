#include <set>
#include <map>
#include <vector>
#include <iomanip>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;

int n;
vector <double> E, S;
vector < vector <double> > D;

double deikstra(int s, int t, bool ch) {
    vector<double> d(n, -1), p(n);
    d[s] = 0;
    vector<char> u(n, 0);
    for (int i = 0; i < n; ++i) {
        int v = -1;
        for (int j = 0; j < n; ++j)
            if (!u[j] && d[j] != -1 && (v == -1 || d[j] < d[v]))
                v = j;
        if (v == -1)
            break;
        u[v] = true;

        for (size_t j = 0; j < n; ++j) {
            if (D[v][j] != -1) {
                double to = j, len = D[v][j];
                if (ch) {
                    if (d[to] == -1 || d[v] + len < d[to]) {
                        d[to] = d[v] + len;
                    }
                } else {
                    if (E[v] >= len && (d[to] == -1 || d[v] + len / S[v] < d[to]) ) {
                        d[to] = d[v] + len / S[v];
                    }
                }
            }
        }
    }
    return d[t];
}

void solve(int cs) {
    D.clear();
    E.clear();
    S.clear();
    cout << "Case #" << cs << ": ";
    int q, T;
    cin >> n >> q;
    E.resize(n, 0);
    S.resize(n, 0);
    for (int i = 0; i < n; ++i) {
        cin >> E[i] >> S[i];
    }
    D.resize(n, vector <double> (n, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> D[i][j];
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            double r = deikstra(i, j, true);
            if (r != -1) {
                D[i][j] = r;
            }
        }
    }
    for (int i = 0; i < q; ++i) {
        int v, u;
        cin >> v >> u; --v; --u;
        cout << setprecision(8) << std::fixed;
        cout << deikstra(v, u, false) << " ";
    }
    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
    return 0;
}
