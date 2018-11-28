#include <bits/stdc++.h>

using namespace std;

const long long INF = 1e18 + 7;

int n;
long long graph[100][100];
long long dist[100][100];
long long endurance[100];
long long speed[100];

void calc_dists() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = graph[i][j];
            if (dist[i][j] == -1) {
                dist[i][j] = INF;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        dist[i][i] = 0;
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
}

long double time_needed[100];

void update_times(int u) {
    vector<pair<long double, int>> to_update;

    for (int v = 0; v < n; v++) {
        if (endurance[u] >= dist[u][v]) {
            long double travel_time = (long double)(dist[u][v]) / speed[u];
            if (time_needed[u] + travel_time < time_needed[v]) {
                time_needed[v] = time_needed[u] + travel_time;
                to_update.push_back({ time_needed[v], v });
            }
        }
    }

    sort(to_update.begin(), to_update.end());
    for (const auto& p: to_update) {
        if (p.first == time_needed[p.second]) {
            update_times(p.second);
        }
    }
}

void calc_times(int start) {
    fill(time_needed, time_needed + n, INF);
    time_needed[start] = 0.0;

    update_times(start);
}

void solve() {
    int q;
    cin >> n >> q;

    for (int i = 0; i < n; i++) {
        cin >> endurance[i] >> speed[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> graph[i][j];
        }
    }

    calc_dists();

    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
        u--, v--;

        calc_times(u);
        cout << time_needed[v] << ' ';
    }
}

int main() {
    int t;
    cin >> t;

    cout << fixed;
    cout.precision(12);

    for (int c = 1; c <= t; c++) {
        cout << "Case #" << c << ": ";
        solve();
        cout << endl;
    }
}
