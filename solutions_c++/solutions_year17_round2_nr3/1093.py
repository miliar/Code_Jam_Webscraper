#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ll;
typedef long double ld;
const double PI = acos(-1.);
ll INF = (ll) 1000 * 1000 * 1000 * 1000 * 100;



int main() {
    freopen("/home/york_io/Documents/Code/contest/in.txt", "r", stdin);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n, q;
        cin >> n >> q;
        vector<ll> dist(n), speed(n);
        for (int i = 0; i < n; ++i) {
            cin >> dist[i] >> speed[i];
        }
        vector<double> dd(n, INF);
        dd[0] = 0.;
        vector<vector<ll>> m(n, vector<ll>(n, -1));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> m[i][j];
            }
        }

        int u, v;
        for (int i = 0; i < q; ++i) {
            cin >> u >> v;
            --u;
            --v;
        }

        for (int i = 0; i < n; ++i) {
            ll tr = 0;
            for (int to = i + 1; to < n; ++to) {
                tr += m[to - 1][to];
                if (tr > dist[i]) break;
                dd[to] = min(dd[to], (double) tr / speed[i] + dd[i]);
            }
        }
        cout.precision(10);
        cout << fixed << "Case #" << t << ": " << dd[n-1] << endl;
    }

    return 0;
}

