#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <string>
#include <utility>
#include <vector>

constexpr int MAX = 100;
int N, P;
int a[4];
char dp[MAX][MAX][MAX];

int solve(void) {
  if (P == 2)
    return a[0] + (a[1] + 1) / 2;
  if (P == 3) {
    int result = a[0];
    int a12 = std::min(a[1], a[2]);
    a[1] -= a12;
    a[2] -= a12;
    result += a12;
    result += (a[1] + 2) / 3 + (a[2] + 2) / 3;
    return result;
  }
  return a[0] + dp[a[1]][a[2]][a[3]];
}

inline int OK(int b, int c, int d) {
  return (b + 2 * c + 3 * d) % 4 == 0;
}

int main(void) {
  for (int b = 0; b < MAX; ++b) {
    for (int c = 0; c < MAX; ++c)
      for (int d = 0; d < 1; ++d) {
        int best = 0;
        if (b) best = std::max(best, (int)dp[b - 1][c][d] + OK(b - 1, c, d));
        if (c) best = std::max(best, (int)dp[b][c - 1][d] + OK(b, c - 1, d));
        if (d) best = std::max(best, (int)dp[b][c][d - 1] + OK(b, c, d - 1));
        dp[b][c][d] = best;
        // printf("%d %d %d --> %d\n", b, c, d, best);
      }
  }

  int TT;
  scanf("%d", &TT);
  for (int T = 1; T <= TT; ++T) {
    scanf("%d%d", &N, &P);
    a[0] = a[1] = a[2] = a[3] = 0;
    for (int i = 0; i < N; ++i) {
      int x;
      scanf("%d", &x);
      ++a[x % P];
    }

    printf("Case #%d: %d\n", T, solve());
  }

  return 0;
}

