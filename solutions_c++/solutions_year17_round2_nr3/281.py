#include <bits/stdc++.h>

using namespace std;

using ll = long long;
const ll INF = (ll)1e18;

struct Solver {
    vector<vector<ll>> dist;
    vector<vector<double>> d;
    vector<ll> max_d;
    vector<ll> speed;

    void run() {
        int n, q;
        cin >> n >> q;
        max_d.resize(n);
        speed.resize(n);
        dist.assign(n, vector<ll>(n, INF));
        d.assign(n, vector<double>(n, INF));
        for (int i = 0; i < n; i++)
            cin >> max_d[i] >> speed[i];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                int x;
                cin >> x;
                if (x < 0)
                    continue;
                dist[i][j] = x;
            }
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (i == j)
                    d[i][j] = 0;
                else {
                    if (max_d[i] >= dist[i][j])
                        d[i][j] = dist[i][j] * 1.0 / speed[i];
                }
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        for (int i = 0; i < q; i++) {
            int from, to;
            cin >> from >> to;
            --from;
            --to;
            cout << d[from][to] << " ";
        }
        cout << "\n";
    }
};

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(20);

    int ts;
    cin >> ts;
    for (int t = 1; t <= ts; t++) {
        cout << "Case #" << t << ": ";
        Solver solver;
        solver.run();
    }
}
