#include <cstdio>
#include <cstring>
#include <algorithm>

const int MAXP = 20;
const int MAXN = 101;
const int INF = ~0u >> 2;

int T, n, p, a[MAXP], dp[MAXN][MAXN][MAXN][MAXN][MAXP];

void update(int &x, int y) {
    if (x < y) x = y;
}

int main() {
    freopen("A.in", "r", stdin);
    scanf("%d", &T);
    for (int cs = 1; cs <= T; cs++) {
        scanf("%d%d", &n, &p);
        std::fill(a, a + MAXP, 0);
        for (int i = 1; i <= n; i++) {
            int g;
            scanf("%d", &g);
            a[g % p]++;
        }
        for (int i = a[0]; i >= 0; i--)
            for (int j = a[1]; j >= 0; j--)
                for (int k = a[2]; k >= 0; k--)
                    for (int l = a[3]; l >= 0; l--)
                        for (int r = p - 1; r >= 0; r--)
                            dp[i][j][k][l][r] = -INF;
        dp[a[0]][a[1]][a[2]][a[3]][0] = 0;
        for (int i = a[0]; i >= 0; i--)
            for (int j = a[1]; j >= 0; j--)
                for (int k = a[2]; k >= 0; k--)
                    for (int l = a[3]; l >= 0; l--)
                        for (int r = p - 1; r >= 0; r--) {
                            if (i > 0) {
                                update(dp[i - 1][j][k][l][(r) % p], dp[i][j][k][l][r] + (r == 0));
                            }
                            if (j > 0) {
                                update(dp[i][j - 1][k][l][(r + 1) % p], dp[i][j][k][l][r] + (r == 0));
                            }
                            if (k > 0) {
                                update(dp[i][j][k - 1][l][(r + 2) % p], dp[i][j][k][l][r] + (r == 0));
                            }
                            if (l > 0) {
                                update(dp[i][j][k][l - 1][(r + 3) % p], dp[i][j][k][l][r] + (r == 0));
                            }
                        }
        int answer = -INF;
        for (int r = p - 1; r >= 0; r--) {
            update(answer, dp[0][0][0][0][r]);
        }
        printf("Case #%d: %d\n", cs, answer);
    }
    return 0;
}
