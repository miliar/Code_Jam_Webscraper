#include <bits/stdc++.h>

using namespace std;

constexpr int MAXN = 100;
constexpr int MAXE = 1e9;
constexpr int MAXS = 1000;

using LL = long long;

constexpr LL INF = -1;
constexpr double D_INF = 1e190;
constexpr LL LL_INF = 1LL << 61;

double jizz() {
    int n, q; scanf("%d%d", &n, &q);

    LL es[MAXN]; double vs[MAXN];
    for (int i = 0; i < n; ++i) scanf("%lld%lf", &es[i], &vs[i]);

    LL dis[MAXN][MAXN];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            scanf("%lld", &dis[i][j]);

    LL dis2[MAXN][MAXN];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            dis2[i][j] = dis[i][j] == INF ? LL_INF : dis[i][j];

    for (int k = 0; k < n; ++k)
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                dis2[i][j] = min(dis2[i][j], dis2[i][k] + dis2[k][j]);

    double time[MAXN][MAXN];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            time[i][j] = D_INF;
            if (dis2[i][j] <= es[i]) time[i][j] = double(dis2[i][j]) / vs[i];
        }
    }

    for (int i = 0; i < n; ++i) time[i][i] = 0;

    for (int k = 0; k < n; ++k)
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) {
                time[i][j] = min(time[i][j], time[i][k] + time[k][j]);
            }

    while (q --> 0) {
        int s, t; scanf("%d%d", &s, &t); --s, --t;
        printf(" %lf", time[s][t]);
    }
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d:", t);
        jizz();
        putchar('\n');
    }

    return 0;
}
