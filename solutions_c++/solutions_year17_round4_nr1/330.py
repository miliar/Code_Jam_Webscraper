#include <bits/stdc++.h>

using namespace std;

const int N = 110;

int n, p;
int dp[N][N][N];
int cnt[5];

int solver() {
  scanf("%d %d", &n, &p);
  memset(cnt, 0, sizeof cnt);
  for (int i = 1; i <= n; i++) {
    int x;
    scanf("%d", &x);
    cnt[x % p]++;
  }
  int res = cnt[0];
  memset(dp, 0, sizeof dp);
  for (int i = 0; i <= cnt[1]; i++) {
    for (int j = 0; j <= cnt[2]; j++) {
      for (int k = 0; k <= cnt[3]; k++) {
        if (i < cnt[1]) {
          dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k] + ((i + j * 2 + k * 3) % p == 0));
        }
        if (j < cnt[2]) {
          dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k] + ((i + j * 2 + k * 3) % p == 0));
        }
        if (k < cnt[3]) {
          dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k] + ((i + j * 2 + k * 3) % p == 0));
        }
      }
    }
  }
  return res + dp[cnt[1]][cnt[2]][cnt[3]];
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tc;
  scanf("%d", &tc);
  for (int i = 1; i <= tc; i++) {
    printf("Case #%d: %d\n", i, solver());
  }
  return 0;
}
