#include<bits/stdc++.h>
using namespace std;

int a[5][1005];
int g[3][1010];
int large[3], ones[3];

int main(){
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, c, m;
        memset(g, 0, sizeof(g));
        large[1] = large[2] = 0;
        ones[1] = ones[2] = 0;
        scanf("%d%d%d", &n, &c, &m);
        for (int i = 0; i < m; i++) {
            int p, b;
            scanf("%d%d", &p, &b);
            g[b][p]++;
            if (p == 1) {
                ones[b]++;
            } else {
                large[b]++;
            }
        }
        int tot1 = large[1] >= ones[2] ? large[1] - ones[2] : 0;
        int tot2 = large[2] >= ones[1] ? large[2] - ones[1] : 0;

        int min_ride = max(tot1, tot2);
        int min_swap = 0;

        large[1] = tot1;
        large[2] = tot2;

        if (large[1] > 0 && large[2] > 0) {
            if (large[1] < large[2]) {
                swap(large[1], large[2]);
                for (int i = 1; i <= n; i++) {
                    swap(g[1][i], g[2][i]);
                }
            }
            large[1] += g[1][1] + g[2][1];
            large[2] += g[1][1] + g[2][1];

            for (int i = 2; i <= n; i++) {
                min_swap += max(0, g[1][i] + g[2][i] - large[1]);
            }
        }
        min_ride += g[1][1] + g[2][1];
        printf("Case #%d: %d %d\n", cas, min_ride, min_swap);
        fprintf(stderr, "Case #%d: %d %d\n", cas, min_ride, min_swap);
    }
    return 0;
}
