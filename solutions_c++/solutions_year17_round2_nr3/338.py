#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll inf = 1e14 + 7;

struct HeapNode {
    int u; double d;
    bool operator < (const HeapNode &x) const {
        return d > x.d;
    }
};

int kases;
int n, Q, e[200], sp[200];
ll d[200][200];
int done[200];
double dis[200];

int main() {
    #ifdef ULTMASTER
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    #endif
    scanf("%d", &kases);
    for (int kase = 1; kase <= kases; ++kase) {
        scanf("%d%d", &n, &Q);
        for (int i = 1; i <= n; ++i)
            scanf("%d%d", &e[i], &sp[i]);
        for (int i = 1; i <= n; ++i) 
            for (int j = 1; j <= n; ++j) {
                scanf("%lld", &d[i][j]);
                if (d[i][j] == -1)
                    d[i][j] = inf;
            }
        for (int k = 1; k <= n; ++k)
            for (int i = 1; i <= n; ++i)
                for (int j = 1; j <= n; ++j)
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        // for (int i = 1; i <= n; ++i) {
        //     for (int j = 1; j <= n; ++j)
        //         printf("%lld ", d[i][j]);
        //     printf("\n");
        // }
        printf("Case #%d: ", kase);
        for (int qq = 0; qq < Q; ++qq) {
            int s, t;
            scanf("%d%d", &s, &t);
            for (int i = 1; i <= n; ++i)
                dis[i] = 1e18;
            dis[s] = 0;
            memset(done, 0, sizeof done);
            priority_queue<HeapNode> q;
            q.push((HeapNode){s, 0});
            while (!q.empty()) {
                HeapNode x = q.top();
                q.pop();
                int u = x.u;
                if (done[u]) continue;
                done[u] = 1;
                for (int v = 1; v <= n; ++v) {
                    if (!done[v] && d[u][v] <= e[u] && 
                        dis[v] > dis[u] + (double)d[u][v] / sp[u]) {
                        dis[v] = dis[u] + (double)d[u][v] / sp[u];
                        q.push((HeapNode){v, dis[v]});
                    }
                }
            }
            printf("%.6f%c", dis[t], (qq == Q - 1 ? '\n' : ' '));
        }
    }
    return 0;
}
