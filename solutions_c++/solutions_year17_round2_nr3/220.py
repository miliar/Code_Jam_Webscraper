#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testcase;
    scanf("%d", &testcase);
    for (int ti = 1; ti <= testcase; ti++) {
        printf("Case #%d: ", ti);
        int n, m;
        double ans = 0;
        scanf("%d%d", &n, &m);
        double f[101][101];
        int d[101][101];
        int a[101], b[101];
        double g[101][101];
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &a[i], &b[i]);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                scanf("%d", &d[i][j]);
                f[i][j] = d[i][j];
                if (i == j) g[i][j] = 0.0; else g[i][j] = 1000000000000000.0;
            }
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (f[i][k] != -1 && f[k][j] != -1) {
                        if (f[i][j] == -1 || f[i][k] + f[k][j] < f[i][j]) {
                            f[i][j] = f[i][k] + f[k][j];
                        }
                    }
                }
            }
        }
        // printf("=========\n");
        // for (int  i = 0; i < n; i++){
        //     for (int j = 0; j < n; j++) {
        //         printf("%d %d %d\n", i, j, f[i][j]);
        //     }
        // }
        // printf("======\n");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (f[i][j] != -1 && f[i][j] <= a[i]) {
                    g[i][j] = f[i][j] * 1.0 / b[i] * 1.0;
                }
            }
        }
        // printf("g=========\n");
        // for (int  i = 0; i < n; i++){
        //     for (int j = 0; j < n; j++) {
        //         printf("%d %d %.5f\n", i, j, g[i][j]);
        //     }
        // }
        // printf("======\n");
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (g[i][j] > g[i][k] + g[k][j]) {
                        g[i][j] = g[i][k] + g[k][j];
                    }
                }
            }
        }
        // printf("g=========\n");
        // for (int  i = 0; i < n; i++){
        //     for (int j = 0; j < n; j++) {
        //         printf("%d %d %.5f\n", i, j, g[i][j]);
        //     }
        // }
        for (int i = 0; i < m; i++) {
            int u, v;
            scanf("%d%d", &u, &v);
            printf("%.9f ", g[u-1][v-1]);
        }
        printf("\n");
    }
}