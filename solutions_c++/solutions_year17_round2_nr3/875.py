#include <stdio.h>
#include <string.h>
int e[111], s[111];
int d[111][111];
double best[111];

int main() {
    int cn, tn;
    for (scanf("%d", &tn), cn = 1; cn <= tn; cn++) {
        int n, q;
        scanf("%d%d", &n, &q);
        for (int i = 1; i <= n; i++) {
            scanf("%d%d", &e[i], &s[i]);
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                scanf("%d", &d[i][j]);
            }
        }
        printf("Case #%d:", cn);
        for (int i = 1; i <= q; i++) {
            int u, v;
            scanf("%d%d", &u, &v);
            for (int i = 0; i < n; i++) {
                best[i] = -10;
            }
            best[n] = 0;
            for (int i = n - 1; i >= 1; i--) {
                int nowd = 0;
                for (int j = i + 1; j <= n; j++) {
                    nowd += d[j-1][j];
                    if (nowd > e[i]) {
                        break;
                    }
                    if (best[j] > -1) {
                        double newt = (double)(nowd) / s[i] + best[j];
                        if (best[i] < -1 || best[i] > newt) {
                            best[i] = newt;
                        }
                    }
                }
            }
            printf(" %.8lf", best[1]);
        }
        printf("\n");
    }
    return 0;
}
