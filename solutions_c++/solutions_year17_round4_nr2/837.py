#include <stdio.h>
#include <algorithm>
#include <vector>
#include <assert.h>
#include <numeric>
#include <functional>

const int kN = 1000 + 5;
int v[kN][kN];
int n, c, m;

int main()
{
    int cas;
    scanf("%d", &cas);
    while (cas--) {
        scanf("%d%d%d", &n, &c, &m);
        memset(v, 0, sizeof(v));
        for (int i = 0; i < m; ++ i) {
            int p, b;
            scanf("%d%d", &p, &b); --p; -- b;
            v[b][p] ++;
        }
        int coast = 0, promot = 0;
        for (int i = 0; i < n; ++ i)
            coast = std::max(coast, std::accumulate(v[i], v[i] + n, 0));
        for (int i = 0, sum = 0; i < n; ++ i) {
            for (int j = 0; j < c; ++ j)
                sum += v[j][i];
            coast = std::max(coast, (sum + i) / (i + 1));
        }
        for (int i = 0; i < n; ++ i) {
            int sum = 0;
            for (int j = 0; j < c; ++ j)
                sum += v[j][i];
            promot += std::max(0, sum - coast);
        }
        static int ca = 0;
        printf("Case #%d: %d %d\n", ++ ca, coast, promot);
    }
}
