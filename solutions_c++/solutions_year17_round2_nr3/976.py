#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define PI acos(-1)
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
const int M = 105;
int n, q, E[M], S[M];
ll D[M][M];
bool can[M][M], visit[M];
void calc() {
        memset(can, 0, sizeof can);
        for(int k = 1; k <= n; k++) {
                for(int i = 1; i <= n; i++) {
                        for(int j = 1; j <= n; j++) {
                                if(D[i][k] == 1e18 || D[k][j] == 1e18)continue;
                                D[i][j] = min(D[i][j], 1LL * D[i][k] + 1LL * D[k][j]);
                        }
                }
        }
        for(int i = 1; i <= n; i++) {
                for(int j = 1; j <= n; j++) {
                        if(D[i][j] <= E[i])
                                can[i][j] = 1;
                }
        }
}
double dijkstra(int st, int ed) {
       memset(visit, 0, sizeof visit);
        priority_queue<pair<double, int> > Q;
        Q.push(mp(0, st));
        while(!Q.empty()) {
                pair<double, int> p = Q.top();
                Q.pop();
                int u = p.s;
                if(u == ed) {
                        return -p.f;
                }
                if(visit[u])continue;
                visit[u] = 1;
                for(int i = 1; i <= n; i++) {
                        if(!can[u][i] || D[u][i] == 1e18)continue;
                        Q.push(mp(p.f - 1.0 * D[u][i] / S[u], i));
                }
        }
}
int main()
{
        freopen("C-large.in", "r", stdin);
        freopen("out.txt", "w", stdout);
        int t, c = 0;
        scanf("%d", &t);
        while(t--) {
                c++;
                printf("Case #%d: ", c);
                scanf("%d %d", &n, &q);
                for(int i = 1; i <= n; i++) {
                        scanf("%d %d", &E[i], &S[i]);
                }
                for(int i = 1; i <= n; i++) {
                        for(int j = 1; j <= n; j++) {
                                scanf("%lld", &D[i][j]);
                                if(D[i][j] == -1)
                                        D[i][j] = 1e18;
                        }
                }
                calc();
                while(q--) {
                        int u, v;
                        scanf("%d %d", &u, &v);
                        printf("%lf", dijkstra(u, v));
                        if(q)
                                printf(" ");
                }
                printf("\n");
        }
        return 0;
}
/*
1
3 1
2 3
2 4
4 4
-1 1 -1
-1 -1 1
-1 -1 -1
1 3
*/
/*
1
4 3
30 60
10 1000
12 5
20 1
-1 10 -1 31
10 -1 10 -1
-1 -1 -1 10
15 6 -1 -1
2 4
3 1
3 2
*/
