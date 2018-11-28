#include <bits/stdc++.h>
#define foru(i, a, b) for(int i = a; i <= b; i++)
using namespace std;
const int MAXN = 105;
int n, q;
int c[4];
int dp3[MAXN][MAXN][3], dp4[MAXN][MAXN][MAXN][4];

void maximize(int &u, int v) {
    u = max(u, v);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int TC;
    scanf("%d", &TC);

    foru(TT, 1, TC) {
        scanf("%d%d", &n, &q);

        foru(i, 0, q - 1) c[i] = 0;
        foru(i, 1, n) {
            int x;
            scanf("%d", &x);
            ++c[x % q];
        }

        printf("Case #%d: ", TT);
        if (q == 2)
            printf("%d\n", c[0] + (c[1] + 1) / 2);
        else if (q == 3) {
            foru(i, 0, c[1]) foru(j, 0, c[2]) foru(x, 0, 2) dp3[i][j][x] = -1e9;
            dp3[0][0][0] = 0;
            foru(i, 0, c[1])
                    foru(j, 0, c[2])
                        foru(x, 0, 2) {
                            int val = dp3[i][j][x] + (x == 0 ? 1 : 0);
                            if (i < c[1])
                                maximize(dp3[i + 1][j][(x + 1) % 3], val);
                            if (j < c[2])
                                maximize(dp3[i][j + 1][(x + 2) % 3], val);
                        }
            int ans = 0;
            foru(x, 0, 2) maximize(ans, dp3[c[1]][c[2]][x]);
            printf("%d\n", ans + c[0]);
        } else {
            foru(i, 0, c[1]) foru(j, 0, c[2]) foru(k, 0, c[3]) foru(x, 0, 3) dp4[i][j][k][x] = -1e9;
            dp4[0][0][0][0] = 0;
            foru(i, 0, c[1])
                foru(j, 0, c[2])
                    foru(k, 0, c[3])
                        foru(x, 0, 3) {
                            int val = dp4[i][j][k][x] + (x == 0 ? 1 : 0);
                            if (i < c[1])
                                maximize(dp4[i + 1][j][k][(x + 1) % 4], val);
                            if (j < c[2])
                                maximize(dp4[i][j + 1][k][(x + 2) % 4], val);
                            if (k < c[3])
                                maximize(dp4[i][j][k + 1][(x + 3) % 4], val);
                        }
            int ans = 0;
            foru(x, 0, 3) maximize(ans, dp4[c[1]][c[2]][c[3]][x]);
            printf("%d\n", ans + c[0]);
        }
    }
    return 0;
}
