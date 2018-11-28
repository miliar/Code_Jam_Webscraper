#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <algorithm>

typedef std::pair<int, int> pii;
constexpr int HALF = 720;
int A[2];
int dp[2][HALF + 4][HALF + 4];
char can[2][2 * HALF + 4];

constexpr int INF = 1000000000;

int main(void) {
  int TT;
  scanf("%d", &TT);
  for (int T = 1; T <= TT; ++T) {
    memset(can, 1, sizeof(can));
    scanf("%d%d", &A[0], &A[1]);
    for (int k = 0; k < 2; ++k)
      for (int i = 0; i < A[k]; ++i) {
        int C, D;
        scanf("%d%d", &C, &D);
        for (int j = C; j < D; ++j)
          can[k][j] = 0;
      }

    int best = INF;
    for (int start = 0; start < 2; ++start) {
      if (!can[start][0])
        continue;
      // memset(dp, 0x3f, sizeof(dp));
      int ca = 1, cb = 1;
      for (int i = 1; i <= HALF; ++i) {
        ca = ca && can[0][i - 1];
        cb = cb && can[1][i - 1];
        dp[0][i][0] = start == 0 && ca ? 0 : INF;
        dp[1][i][0] = INF;
        dp[0][0][i] = INF;
        dp[1][0][i] = start == 1 && cb ? 0 : INF;
      }
      // dp[start][0][0] = 0;
      // dp[!start][0][0] = INF;

      for (int a = 1; a <= HALF; ++a)
        for (int b = 1; b <= HALF; ++b) {
          for (int k = 0; k < 2; ++k) {
            if (!can[k][a + b - 1]) {
              dp[k][a][b] = INF;
              continue;
            }
            if (k == 0)
              dp[0][a][b] = std::min(dp[0][a - 1][b], dp[1][a - 1][b] + 1);
            else
              dp[1][a][b] = std::min(dp[1][a][b - 1], dp[0][a][b - 1] + 1);
          }
        }
      // for (int a = 0; a <= HALF; ++a) {
      //   for (int b = 0; b <= HALF; ++b)
      //     printf("%d%d ", (int)can[0][a + b], (int)can[1][a + b]);
      //   printf("\n");
      // }
      // printf("\n");
      // for (int a = 0; a <= HALF; ++a) {
      //   for (int b = 0; b <= HALF; ++b)
      //     printf("%d %d  ", dp[0][a][b], dp[1][a][b]);
      //   printf("\n");
      // }
      // printf("\n");

      // printf("start=%d  %d %d\n", start, dp[0][HALF][HALF], dp[1][HALF][HALF]);
      best = std::min(best, std::min(dp[start][HALF][HALF], dp[!start][HALF][HALF] + 1));
    }
    printf("Case #%d: %d\n", T, best);
  }
  return 0;
}
