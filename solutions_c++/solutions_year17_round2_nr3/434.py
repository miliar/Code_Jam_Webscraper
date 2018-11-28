#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;

long long g[105][105];
double g2[105][105];
long long km[105];
double speed[105];

int main() {
    int t, cas = 0;
    int n, q;
    scanf("%d", &t);
    while (t--) {
        cas++;
        scanf("%d %d", &n, &q);
        for (int i = 0; i < n; ++i) {
            scanf("%lld %lf", &km[i], &speed[i]);
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                scanf("%lld", &g[i][j]);
            }
        }
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (g[i][k] == -1 || g[k][j] == -1) {
                        continue;
                    }
                    if (g[i][j] == -1 || g[i][j] > g[i][k] + g[k][j])
                        g[i][j] = g[i][k] + g[k][j];
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (g[i][j] == -1 || g[i][j] > km[i]) {
                    g2[i][j] = -1;
                } else {
                    g2[i][j] = (double)g[i][j] / speed[i];
                }
            }
        }
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (g2[i][k] < 0 || g2[k][j] < 0) {
                        continue;
                    }
                    if (g2[i][j] < 0 || g2[i][j] > g2[i][k] + g2[k][j])
                        g2[i][j] = g2[i][k] + g2[k][j];
                }
            }
        }
        printf("Case #%d:", cas);
        while (q--) {
            int x, y;
            scanf("%d %d", &x, &y);
            x--;
            y--;
            printf(" %.12lf", g2[x][y]);
        }
        printf("\n");
    }
    return 0;
}
