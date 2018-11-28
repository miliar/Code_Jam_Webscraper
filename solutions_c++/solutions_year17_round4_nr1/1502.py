#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int T, N, P;
int G, R[4];
int dp[101][101][101];
int sum(int j, int k, int l) { return (j * 1 + k * 2 + l * 3) % P == 0; }
int main() {
  scanf("%d", &T);
  for (int TT = 1; TT <= T; TT++) {
    scanf("%d%d", &N, &P);
    memset(dp, 0, sizeof(dp));
    memset(R, 0, sizeof(R));
    for (int i = 0; i < N; i++) {
      scanf("%d", &G);
      R[G % P]++;
    }
    // memset(dp, 0x3f, sizeof(dp));
    dp[0][0][0] = 0;
    int ans = R[0];
    for (int j = 0; j <= R[1]; j++)
      for (int k = 0; k <= R[2]; k++)
        for (int l = 0; l <= R[3]; l++) {
          if (j > 0) {
            dp[j][k][l] = max(dp[j][k][l], dp[j - 1][k][l] + sum(j - 1, k, l));
          }
          if (k > 0) {
            dp[j][k][l] = max(dp[j][k][l], dp[j][k - 1][l] + sum(j, k - 1, l));
          }
          if (l > 0) {
            dp[j][k][l] = max(dp[j][k][l], dp[j][k][l - 1] + sum(j, k, l - 1));
          }
        }
    ans += dp[R[1]][R[2]][R[3]];
    printf("Case #%d: %d\n", TT, ans);
  }
  return 0;
}
