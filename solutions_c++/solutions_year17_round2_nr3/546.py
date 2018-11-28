#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

typedef long long LL;

#define N 110

int T, t = 1;

int n, q;
int housekm[N], housesp[N];
LL dis[N][N];
int querys[N], querye[N];
double ans[N];
double dp[N];
bool vis[N];

void floyd(){
    for(int k = 0; k < n; ++k){
        for(int i = 0; i < n; ++i){
            if(i == k){
                continue;
            }
            for(int j = 0; j < n; ++j){
                if(j == i || j == k){
                    continue;
                }
                if(dis[i][k] != -1 && dis[k][j] != -1){
                    if(dis[i][j] == -1 || dis[i][j] > dis[i][k] + dis[k][j]){
                        dis[i][j] = dis[i][k] + dis[k][j];
                    }
                }
            }
        }
    }
    for(int k = 0; k < n; ++k){
        dis[k][k] = -1;
    }
}

void bfs(int s, int e){
    memset(vis, false, sizeof(vis));
    for(int i = 0; !vis[e]; ++i){
        double best = -1;
        int node = -1;
        for(int j = 0; j < n; ++j){
            if(vis[j] || dp[j] < 0){
                continue;
            }
            if(best < 0 || best > dp[j]){
                best = dp[j];
                node = j;
            }
        }
        vis[node] = true;
        for(int j = 0; j < n; ++j){
            if(!vis[j] && dis[node][j] != -1 && dis[node][j] <= housekm[node]){
                if(dp[j] < 0 || dp[j] > best + 1.0 * dis[node][j] / housesp[node]){
                    dp[j] = best + 1.0 * dis[node][j] / housesp[node];
                }
            }
        }
    }
}

int main() {
    scanf("%d", &T);
    while(T--) {
        scanf("%d%d", &n, &q);
        for(int i = 0; i < n; ++i) {
            scanf("%d%d", &housekm[i], &housesp[i]);
        }
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                scanf("%lld", &dis[i][j]);
            }
        }
        floyd();
        for(int i = 0; i < q; ++i) {
            scanf("%d%d", &querys[i], &querye[i]);
            --querys[i];
            --querye[i];
            for(int j = 0; j < n; ++j){
                dp[j] = -1;
            }
            dp[querys[i]] = 0;
            bfs(querys[i], querye[i]);
            ans[i] = dp[querye[i]];
        }
        printf("Case #%d:", t++);
        for(int i = 0; i < q; ++i){
            printf(" %f", ans[i]);
        }
        printf("\n");
    }
    return 0;
}
