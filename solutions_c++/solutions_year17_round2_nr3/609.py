#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <list>


using namespace std;

#define N 105
double adj[N][N];
double dis[N][N];
double len[N];
double sp[N];
double cost[N][N];
int n, q;
double f[N];
const double INF = 1e12;

void init() {
}

int main() {
    int test;
    scanf("%d", &test);
    for (int cas = 1; cas <= test; cas++) {
        scanf("%d%d", &n, &q);
        for (int i = 1; i <= n; i++) {
            scanf("%lf%lf", len + i, sp + i);
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                scanf("%lf", &adj[i][j]);
                if (adj[i][j] == -1) {
                    adj[i][j] = INF;
                }
            }
        }

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (adj[i][k] < INF && adj[k][j] < INF) {
                        adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);
                    }
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (adj[i][j] > len[i]) {
                    cost[i][j] = INF;
                    continue;
                }
                cost[i][j] = adj[i][j] / sp[i];
            }
        }

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (cost[i][k] < INF && cost[k][j] < INF) {
                        cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j]);
                    }
                }
            }
        }


        printf("Case #%d:", cas);

        for (int tt = 0; tt < q; tt++) {
            int a, b;
            scanf("%d%d", &a, &b);
            printf(" %.7f", cost[a][b]);
        }
        puts("");
    }
    return 0;
}
