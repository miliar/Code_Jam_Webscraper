#include <bits/stdc++.h>
using namespace std;

long long g[110][110];
int use[110];
double dis[110];
int e[110], s[110];

double calc(int u, int v, int n) {
    memset(use, 0, sizeof(use));
    for (int i = 0; i < n; i++) {
        dis[i] = -10000.0;
    }
    dis[u] = 0.0;
    for (int i = 0; i < n; i++) {
        int id = -1;
        for (int j = 0; j < n; j++) {
            if (use[j]) {
                continue;
            }
            if (dis[j] < -100) {
                continue;
            }
            if (id == -1 || dis[j] < dis[id]) {
                id = j;
            }
        }
        if (id == -1) {
            break;
        }
        use[id] = 1;
        for (int i = 0; i < n; i++) {
            if (use[i]) {
                continue;
            }
            long long dd = g[id][i];
            if (dd == -1) {
                continue;
            }
            if (dd <= e[id]) {
                double tt = dd * 1.0 / s[id];
                if (dis[i] < -100.0 || dis[i] > dis[id] + tt) {
                    dis[i] = dis[id] + tt;
                }
            }
        }
    }
    return dis[v];
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, q;
        scanf("%d%d", &n, &q);
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &e[i], &s[i]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                scanf("%I64d", &g[i][j]);
            }
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (g[i][k] != -1 && g[k][j] != -1) {
                        if (g[i][j] == -1 || g[i][j] > g[i][k] + g[k][j]) {
                            g[i][j] = g[i][k] + g[k][j];
                        }
                    }
                }
            }
        }
        printf("Case #%d:", cas);
        for (int i = 0; i < q; i++) {
            int u, v;
            scanf("%d%d", &u, &v);
            u--;
            v--;
            double res = calc(u, v, n);
            printf(" %.20f", res);
            fprintf(stderr, " (%.20f)", res);
        }
        printf("\n");
    }
    return 0;
}