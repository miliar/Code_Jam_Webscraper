#include <cstdio>
#include <algorithm>
#include <cstring>
#define REP(i, N) for (int i = 0; i < N; i++)
using namespace std;
int T, C[5], N, P, dp[2][102][102][102][5];
//sum, i, j, k

int main() {
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    memset(C, 0, sizeof C);
    scanf("%d%d", &N, &P);
    REP(i, N) {
      int x; scanf("%d", &x);
      ++C[x % P];
    }
    for (int s = 1; s <= N; s++) {
      REP(i, C[0]+1) REP(j, C[1]+1) REP(k, C[2]+1) {
        int m = s - i - j - k;
        if (m < 0 || m > C[3]) continue;
        REP(p, P) {
          int ans = -1;
          if (i > 0) ans = max(ans, dp[s-1&1][i-1][j][k][(p - 0 + P)%P]);
          if (j > 0) ans = max(ans, dp[s-1&1][i][j-1][k][(p - 1 + P)%P]);
          if (k > 0) ans = max(ans, dp[s-1&1][i][j][k-1][(p - 2 + P)%P]);
          if (m > 0) ans = max(ans, dp[s-1&1][i][j][k]  [(p - 3 + P)%P]);
          ans += (p == 0);
          dp[s&1][i][j][k][p] = ans;
        }
      }
    }
    printf("%d\n", dp[N&1][C[0]][C[1]][C[2]][0]);
  }
  return 0;
}
