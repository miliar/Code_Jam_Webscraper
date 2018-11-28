#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAXN 110
typedef long long LL;

int n, q, s[MAXN], e[MAXN];
LL dis[MAXN][MAXN];
double ans[MAXN];
bool vis[MAXN];

void Folyd()
{
    int i, j, k;
    for(k = 1; k <= n; ++k)
        for(i = 1; i <= n; ++i)
            for(j = 1; j <= n; ++j)
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
}

void Init()
{
    int i, j;
    scanf("%d %d", &n, &q);
    for(i = 1; i <= n; ++i){
        scanf("%d %d", e + i, s + i);
    }
    for(i = 1; i <= n; ++i)
        for(j = 1; j <= n; ++j){
            scanf("%I64d", &dis[i][j]);
            if(dis[i][j] == -1) dis[i][j] = 1e17;
        }
}

double Query(int S, int T)
{
    memset(vis, 0, sizeof(vis));
    int i, j;
    for(i = 1; i <= n; ++i) ans[i] = -1;
    ans[S] = 0;
    while(true){
        for(i = 1, j = -1; i <= n; ++i){
            if(vis[i] || ans[i] < 0) continue;
            if(j < 0) j = i;
            else if(ans[i] < ans[j]) j = i;
        }
        if(j == -1) break;
        vis[j] = true;
        for(i = 1; i <= n; ++i){
            if(vis[i]) continue;
            if(dis[j][i] > e[j]) continue;
            if(ans[i] < 0) ans[i] = ans[j] + dis[j][i] / (double) s[j];
            else ans[i] = fmin(ans[i], ans[j] + dis[j][i] / (double) s[j]);
        }
    }
    return ans[T];
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, i, j, u, v;
    for(scanf("%d", &T), j = 1; j <= T; ++j){
        Init();
        Folyd();
        printf("Case #%d:", j);
        for(i = 1; i <= q; ++i){
            scanf("%d %d", &u, &v);
            printf(" %.8f", Query(u, v));
        }
        printf("\n");
    }
    return 0;
}
