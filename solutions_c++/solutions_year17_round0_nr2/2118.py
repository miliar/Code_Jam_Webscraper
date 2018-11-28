#include <bits/stdc++.h>

using namespace std;

vector<int> getdig(long long n) {
  vector<int> ret;
  while (n) {
    ret.push_back(n % 10);
    n /= 10;
  }
  reverse(ret.begin(), ret.end());
  return ret;
}

void go(long long n) {
  vector<int> dig = getdig(n);
  int z = dig.size();
  long long dp[z][10][2];
  memset(dp, -1, sizeof(dp));
  for (int j = 0; j < dig[0]; ++j) {
    dp[0][j][0] = j;
  }
  dp[0][dig[0]][1] = dig[0];
  for (int i = 0; i < z - 1; ++i) {
    for (int j = 0; j < 10; ++j) {
      //dp[i][j][0]
      for (int nj = j; nj < 10; ++nj)
        dp[i + 1][nj][0] = max(dp[i + 1][nj][0], dp[i][j][0] * 10 + nj);
      //dp[i][j][1]
      for (int nj = j; nj < dig[i + 1]; ++nj)
        dp[i + 1][nj][0] = max(dp[i + 1][nj][0], dp[i][j][1] * 10 + nj);
      if (dig[i + 1] >= j)
        dp[i + 1][dig[i + 1]][1] = max(dp[i + 1][dig[i + 1]][1], dp[i][j][1] * 10 + dig[i + 1]);
    }
  }
  long long mx = 0;
  for (int j = 0; j < 10; ++j)
    for (int k = 0; k < 2; ++k)
      mx = max(mx, dp[z - 1][j][k]);
  printf("%lld\n", mx);
}

int main() {
  int t;
  scanf("%d", &t);
  long long n;
  for (int _ = 1; _ <= t; ++_) {
    scanf("%lld", &n);
    printf("Case #%d: ", _);
    go(n);
  }
  return 0;
}
