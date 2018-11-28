#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

int n;
vector<vector<ll>> dist;
vector<pair<ll, ll>> horses; // distance, speed

vector<ll> dijkstra(int start) {
    vector<ll> dist2(n, -1);
    priority_queue<pair<ll, int>> q;
    q.push({0, start});
    while (q.size()) {
        ll d;
        int v;
        tie(d, v) = q.top();
        q.pop();
        if (dist2[v] != -1 && dist2[v] <= -d) continue;
        dist2[v] = -d;
        for (int i = 0; i < n; ++i) {
            int dd = dist[v][i];
            if (dd == -1) continue;
            q.push({d - dd, i});
        }
    }
    dist2[start] = -1;
    return dist2;
}

void solve(int)
{
    ll q;
    cin >> n >> q;
    horses.assign(n, {});
    dist.assign(n, vector<ll>(n));
    for (auto& p: horses) cin >> p.first >> p.second;
    for (auto& v: dist) for (ll& l: v) cin >> l;

    vector<vector<double>> dist2(n, vector<double>(n));
    for (int start = 0; start < n; ++start) {
        auto v = dijkstra(start);
        ll speed, max_distance;
        tie(max_distance, speed) = horses[start];
        for (int i = 0; i < n; ++i) {
            if (v[i] != -1 && v[i] <= max_distance) {
                dist2[start][i] = v[i] / static_cast<double>(speed);
            } else {
                dist2[start][i] = -1;
            }
        }
    }

    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dist2[i][k] >= 0 && dist2[k][j] >= 0) {
                    double new_dist = dist2[i][k] + dist2[k][j];
                    if (dist2[i][j] < 0 || new_dist < dist2[i][j]) {
                        dist2[i][j] = new_dist;
                    }
                }
            }
        }
    }

    for (int i = 0; i < q; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        double d = dist2[u][v];
        assert(d >= 0);
        cout << setprecision(30) << d << " ";
    }
    cout << endl;
}

int32_t main()
{
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve(i);
    }
}
