// Google Code Jam 2017 Round 1B - C
// https://code.google.com/codejam/contest/8294486/dashboard#s=p2
// 2017.04.22

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#define ll long long
#define N 111
#define md 1000000007
using namespace std;

int t;
int n, q;
ll e[N], v[N], d[N][N];
double tg[N][N];

struct spd {
    int n; // node id
    double t; // time
    ll h; // remain health
};

bool operator < (spd u, spd v){
    return u.t > v.t;
}

int main(void){
    scanf("%d", &t);
    for(int s = 1; s <= t; s++){
        scanf("%d%d", &n, &q);
        for(int i = 1; i <= n; i++) scanf("%lld%lld", &e[i], &v[i]);
        for(int i = 1; i <= n; i++) for(int j = 1; j <= n; j++) scanf("%lld", &d[i][j]);

        // gen time graph: visit from node i to node j using horse i
        memset(tg, -1, sizeof tg);
        for(int i = 1; i <= n; i++){
            bool vis[N];
            memset(vis, 0, sizeof vis);
            priority_queue<spd> tms;
            spd tmp; tmp.n = i, tmp.t = 0, tmp.h = e[i];
            tms.push(tmp);
            while(tms.empty() == false){
                spd tp = tms.top(); tms.pop();
                tg[i][tp.n] = tp.t;
                vis[tp.n] = true;
//                printf("n=%d t=%lf h=%lld\n", tp.n, tp.t, tp.h);
                for(int j = 1; j <= n; j++){
                    if(vis[j] == true || d[tp.n][j] == -1 || tp.h < d[tp.n][j]) continue;
                    tmp.n = j; tmp.t = tp.t + (double)d[tp.n][j] / v[i]; tmp.h = tp.h - d[tp.n][j];
                    tms.push(tmp);
                }
            }
//            for(int j = 1; j <= n; j++) printf("%lf ", tg[i][j]); printf("\n");
        }
        
        // all pair shortest
        for(int k = 1; k <= n; k++)
            for(int i = 1; i <= n; i++)
                for(int j = 1; j <= n; j++){
                    if(isnan(tg[i][k]) || isnan(tg[k][j])) continue;
                    if(isnan(tg[i][j]))
                        tg[i][j] = tg[i][k] + tg[k][j];
                    else
                        tg[i][j] = min(tg[i][j], tg[i][k] + tg[k][j]);
                }
        
        
        printf("Case #%d: ", s);
        while(q--){
            int u, v;
            scanf("%d%d", &u, &v);
            printf("%lf ", tg[u][v]);
        }
        printf("\n");
    }
}
