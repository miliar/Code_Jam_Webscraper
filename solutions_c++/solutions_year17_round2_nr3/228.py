#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define pb push_back

const int N = 110;
set<pair<double, int>> setD;
double dist[N];
int64_t d[N][N];
int e[N], s[N];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, tt;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt) {
        int n, q;
        scanf("%d%d", &n, &q);
        for (int i = 1; i <= n; ++i) {
            scanf("%d%d", e + i, s + i);
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                scanf("%lld", &d[i][j]);
            }
        }
        for (int k = 1; k <= n; ++k) {
            for (int i = 1; i <= n; ++i) {
                for (int j = 1; j <= n; ++j) {
                    if (d[i][k] != -1 && d[k][j] != -1 && (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j])) {
                        d[i][j] = d[i][k] + d[k][j];
                    }
                }
            }
        }
        printf("Case #%d: ", tt);
        while (q--) {
            int st, en;
            scanf("%d%d", &st, &en);
            setD.clear();
            fill(dist, dist + n + 1, 1e+18);
            dist[st] = 0;
            setD.emplace(0, st);
            while (!setD.empty()) {
                double time = setD.begin()->fi;
                int i = setD.begin()->se;
                setD.erase(setD.begin());
                for (int j = 1; j <= n; ++j) {
                    if (d[i][j] != -1 &&
                        d[i][j] <= e[i] &&
                        dist[j] > time + d[i][j] * 1. / s[i]) {
                        auto it  = setD.find({dist[j], j});
                        if (it != setD.end()) {
                            setD.erase(it);
                        }
                        dist[j] = time + d[i][j] * 1. / s[i];
                        setD.insert({dist[j], j});
                    }
                }
            }
            printf("%.10f ", dist[en]);
        }
        printf("\n");
    }
}
