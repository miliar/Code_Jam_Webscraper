#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int N = 110;
LL d[N][N];
double dis[N];
int e[N], s[N];
int n, q;
bool vis[N];

double dijs(int u, int v) {
    memset(vis, 0, sizeof(vis));
    fill(dis + 1, dis + n + 1, 1e18);
    dis[u] = 0;
    for (int i = 1; i <= n; i++) {
        int k = -1;
        double mx = 1e18;
        for (int j = 1; j <= n; j++) if (!vis[j] && dis[j] < mx) mx = dis[j], k = j;
        vis[k] = 1;
        if (k == v) break;
        for (int j = 1; j <= n; j++) if (!vis[j] && d[k][j] != -1) {
            if (d[k][j] <= e[k] && dis[k] + d[k][j] * 1.0 / s[k] < dis[j]) 
                dis[j] = dis[k] + d[k][j] * 1.0 / s[k];
        }
    }
    return dis[v];
}

int main() {
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        scanf("%d%d", &n, &q);
        for (int i = 1; i <= n; i++) scanf("%d%d", e + i, s + i);
        for (int i = 1; i <= n; i++) 
            for (int j = 1; j <= n; j++) scanf("%lld", &d[i][j]);
        for (int k = 1; k <= n; k++) 
            for (int i = 1; i <= n; i++)
                for (int j = 1; j <= n; j++) 
                    if (d[i][k] != -1 && d[k][j] != -1) {
                        if (d[i][j] == -1) d[i][j] = d[i][k] + d[k][j];
                        else d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                    }
        printf("Case #%d:", _);
        while (q--) {
            int u, v;
            scanf("%d%d", &u, &v);
            printf(" %.9f", dijs(u, v)); 
        }
        puts("");
    }

    return 0;
}
