#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 200;
const double eps = 1e-8;
ll dis[N], vel[N];
ll g[N][N];
double dp[N];
int n;
queue<int> que;
int ins[N];
int dcmp(double x){
    if (fabs(x) < eps) return 0;
    return x < 0 ? -1 : 1;
}
int main(){
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int cas=1; cas<=test; cas++){
        int q, u, v;
        scanf("%d %d", &n, &q);
        for (int i=1; i<=n; i++) scanf("%lld %lld", &dis[i], &vel[i]);

        for (int i=1; i<=n; i++)
            for (int j=1; j<=n; j++)
                scanf("%d", &g[i][j]);
        for (int k=1; k<=n; k++)
        for (int i=1; i<=n; i++) if (g[i][k] != -1)
        for (int j=1; j<=n; j++) if (g[k][j] != -1){
            if (g[i][j] == -1 || g[i][j] > g[i][k] + g[k][j])
                g[i][j] = g[i][k] + g[k][j];
        }
//        for (int i=1; i<=n; i++)
//        for (int j=1; j<=n; j++){
//
//        }
        printf("Case #%d:", cas);
        while (q--){
            scanf("%d %d", &u, &v);
            for (int i=0; i<=n; i++) dp[i] = 1e30;
            dp[u] = 0;
            while (!que.empty()) que.pop();
            memset(ins, 0, sizeof(ins));
            que.push(u);
            ins[u] = 1;
            while (!que.empty()){
                int u = que.front(); que.pop();
                for (int v = 1; v<=n; v++) if (u != v && g[u][v] <= dis[u]){
                    double tmp = dp[u] + g[u][v] * 1.0 / vel[u];
                    if (dcmp(dp[v] - tmp) > 0){
                        dp[v] = tmp;
                        if (!ins[v]) {
                            ins[v] = 1;
                            que.push(v);
                        }
                    }
                }
                ins[u] = 0;
            }
            printf(" %.10lf", dp[v]);
        }
        puts("");
//            for (int i=1; i<=n; i++)
//                printf("    %4d %.8lf\n", i, dp[i]);
    }
    fclose(stdout);
    return 0;
}


