#include <iostream>
#include <vector>
#include <set>

using namespace std;

int n, q;
long long e[105], s[105], d[105][105], was[105][105];
double dist[105][105];
set<pair<double, pair<int, int>>> qq;

void load() {
    cin >> n >> q;
    for (int i = 0;i < n;i++) {
        cin >> e[i] >> s[i];
    }
    for (int i = 0;i < n;i++) {
        for (int j = 0;j < n;j++) {
            cin >> d[i][j];
        }
        d[i][i] = 0;
    }

    for (int k = 0;k < n;k++) {
        for (int i = 0;i < n;i++) {
            for (int j = 0;j < n;j++) {
                if (d[i][k] == -1 || d[k][j] == -1 || (d[i][j] != -1 && d[i][j] < d[i][k] + d[k][j])) {
                    continue;
                }
                d[i][j] = d[i][k] + d[k][j];
            }
        }
    }
}

double go(int u, int v) {
    memset(was, 0, sizeof(was));
    was[u][u] = 1;
    dist[u][u] = 0;
    qq.clear();
    qq.insert(make_pair(0, make_pair(u, u)));
    while (!qq.empty()) {
        double cd = qq.begin()->first;
        int cv = qq.begin()->second.first;
        int hv = qq.begin()->second.second;
        qq.erase(qq.begin());
        //cerr << cd << " " << cv << " " << hv << endl;

        if (cv == v) {
            return cd;
        }
        if (!was[cv][cv] || (dist[cv][cv] > cd)) {
            was[cv][cv] = 1;
            qq.erase(make_pair(dist[cv][cv], make_pair(cv, cv)));
            dist[cv][cv] = cd;
            qq.insert(make_pair(dist[cv][cv], make_pair(cv, cv)));
        }
        long long lefth = e[hv] - d[hv][cv];
        for (int i = 0;i < n;i++) {
            if (d[cv][i] == -1 || d[cv][i] > lefth) continue;
            if (!was[i][hv] || (dist[i][hv] > cd + d[cv][i] / double(s[hv]))) {
                was[i][hv] = 1;
                qq.erase(make_pair(dist[i][hv], make_pair(i, hv)));
                dist[i][hv] = cd + d[cv][i] / double(s[hv]);
                qq.insert(make_pair(dist[i][hv], make_pair(i, hv)));
            } 
        }
    }
    return -1;
}

void solve(int test) {
    printf("Case #%d:", test);
    for (int i = 0, u, v;i < q;i++) {
        cin >> u >> v;
        u--, v--;

        printf(" %.8lf", go(u, v));
    }
    printf("\n");
}

int main() {
#ifdef VALERA
    freopen("a.in", "r", stdin);
#endif
    int t;
    cin >> t;

    for (int i = 0;i < t;i++) {
        load();
        solve(i + 1);
    }
    return 0;
}
