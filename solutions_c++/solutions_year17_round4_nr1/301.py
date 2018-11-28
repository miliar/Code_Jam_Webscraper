#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

const int N = 100 + 10;

int dp[N][N][N][4], G[N];
int cnt[4], n, p;

int solve(int i, int j, int k, int m) {
  if (dp[i][j][k][m] != -1) return dp[i][j][k][m];
  if (i == cnt[1] && j == cnt[2] && k == cnt[3]) return 0;
  int ret = 0;
  if (i < cnt[1]) ret = std::max(ret, solve(i + 1, j, k, (m + 1) % p));
  if (j < cnt[2]) ret = std::max(ret, solve(i, j + 1, k, (m + 2) % p));
  if (k < cnt[3]) ret = std::max(ret, solve(i, j, k + 1, (m + 3) % p));
  ret += m == 0;
  return dp[i][j][k][m] = ret;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    scanf("%d%d", &n, &p);
    int ret = 0;
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < n; ++i) {
      scanf("%d", G + i);
      if (G[i] % p == 0) ++ret;
      else {
        cnt[G[i] % p]++;
      }
    }
    memset(dp, -1, sizeof(dp));
    printf("Case #%d: %d\n", cas, solve(0, 0, 0, 0) + ret);
  }
  return 0;
}
