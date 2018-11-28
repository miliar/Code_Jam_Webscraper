#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
const int MAXN = 105;
int TC, N, P;
int cnt[5];
int dp[5][MAXN][MAXN][MAXN][4];
int r(int x, int y, int z, int l) {
    if (dp[P][x][y][z][l] != -1) return dp[P][x][y][z][l];
    dp[P][x][y][z][l] = 0;
    if (x+y+z == 0) return 0;
    if (x > 0) dp[P][x][y][z][l] = max(dp[P][x][y][z][l], (l == 0) + r(x-1, y, z, (l+P-1)%P));
    if (y > 0) dp[P][x][y][z][l] = max(dp[P][x][y][z][l], (l == 0) + r(x, y-1, z, (l+P-2)%P));
    if (z > 0) dp[P][x][y][z][l] = max(dp[P][x][y][z][l], (l == 0) + r(x, y, z-1, (l+P-3)%P));
    
    //printf("%d %d %d %d : %d\n", x, y, z, l, dp[P][x][y][z][l]);
    return dp[P][x][y][z][l];
}
int main() {
    scanf("%d", &TC);
    memset(dp, -1, sizeof dp);
    for (int Txn = 1; Txn <= TC; ++Txn) {
        scanf("%d%d", &N, &P);
        memset(cnt, 0, sizeof cnt);
        for (int i = 0, x; i < N; ++i) {
            scanf("%d", &x);
            cnt[x%P]++;
        }
        printf("Case #%d: ", Txn);
        printf("%d\n", r(cnt[1], cnt[2], cnt[3], 0) + cnt[0]);
    }
}