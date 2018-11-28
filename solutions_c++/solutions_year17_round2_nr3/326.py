#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

const int MAXN = 111;
const long long inf_small = 1023456789;
const long long inf = inf_small * (long long) 100 * 100;

int T, N, Q, u, v;
long long horsedist[MAXN], horsespeed[MAXN];
long long dist_1edge[MAXN][MAXN]; // km
long long dist_shortest[MAXN][MAXN]; // actual shortest distance b/t each pair
long double dist_1horse[MAXN][MAXN]; // actually time; min time to get between each pair with one horse
long double dist_actual[MAXN][MAXN]; // actually time; min time to get between each pair with many horses

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d %d", &N, &Q);
        for (int i = 1; i <= N; ++i) {
            scanf("%lld %lld", &horsedist[i], &horsespeed[i]);
        }
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                scanf("%lld", &dist_1edge[i][j]);
                dist_shortest[i][j] = dist_1edge[i][j] < 0 ? inf : dist_1edge[i][j]; 
            }
        }

        for (int k = 1; k <= N; ++k) {
            for (int i = 1; i <= N; ++i) {
                for (int j = 1; j <= N; ++j) {
                    dist_shortest[i][j] = min(dist_shortest[i][j],
                                              dist_shortest[i][k] + dist_shortest[k][j]);
                }
            }
        }

        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                if (dist_shortest[i][j] <= horsedist[i]) {
                    dist_1horse[i][j] = dist_shortest[i][j] / (long double) horsespeed[i];
                } else {
                    dist_1horse[i][j] = inf;
                }
                dist_actual[i][j] = dist_1horse[i][j];
            }
        }

        for (int k = 1; k <= N; ++k) {
            for (int i = 1; i <= N; ++i) {
                for (int j = 1; j <= N; ++j) {
                    dist_actual[i][j] = min(dist_actual[i][j],
                                            dist_actual[i][k] + dist_actual[k][j]);
                }
            }
        }

        printf("Case #%d:", t);
        for (int i = 0; i < Q; ++i) {
            scanf("%d %d", &u, &v);
            printf(" %0.9Lf", dist_actual[u][v]);
        }
        printf("\n");
    }

    return 0;
}
