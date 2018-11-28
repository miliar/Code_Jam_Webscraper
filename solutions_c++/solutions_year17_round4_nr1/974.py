#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

const int MAXN = 111, MAXP = 5, inf = 1023456789, d = 0;

int T, N, P, G[MAXN], freq[MAXP], dp[MAXN][MAXN][MAXN][MAXP];

int solve(int c1, int c2, int c3, int mod) {
  if (dp[c1][c2][c3][mod] >= 0) {
    return dp[c1][c2][c3][mod];
  }

  int res = -inf; 
  int gain = (mod == 0 ? 1 : 0);
  if (c1 > 0) {
    int leftover = (mod - 1 + P) % P;
    res = max(res, gain + solve(c1 - 1, c2, c3, leftover));
  }
  if (c2 > 0) {
    int leftover = (mod - 2 + P) % P;
    res = max(res, gain + solve(c1, c2 - 1, c3, leftover));
  }
  if (c3 > 0) {
    int leftover = (mod - 3 + P) % P;
    res = max(res, gain + solve(c1, c2, c3 - 1, leftover));
  }
  dp[c1][c2][c3][mod] = res;
  return res;
}

int main() {
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    scanf("%d %d", &N, &P);

    for (int i = 0; i < MAXP; ++i) {
      freq[i] = 0;
    }

    for (int i = 0; i < N; ++i) {
      scanf("%d", &G[i]);
      freq[G[i] % P]++;
    }

    for (int i = 0; i <= N; ++i) {
      for (int j = 0; j <= N; ++j) {
        for (int k = 0; k <= N; ++k) {
          for (int l = 0; l <= P; ++l) {
            dp[i][j][k][l] = -inf;
          }
        }
      }
    }
    for (int i = 0; i <= P; ++i) {
      dp[0][0][0][i] = 0;
    }

    int answer = freq[0];
    answer += solve(freq[1], freq[2], freq[3], 0);

    printf("Case #%d: %d\n", t, answer);
  }

  return 0;
}
