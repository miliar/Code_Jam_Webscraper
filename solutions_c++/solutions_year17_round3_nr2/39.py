#include <bits/stdc++.h>
using namespace std;

int solve() {
  static int const all = 24 * 60;
  static int a[2][all];
  memset(a, 0, sizeof a);
  {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
      int l, r;
      cin >> l >> r;
      for (int x = l; x < r; ++x)
        a[0][x] = 1;
    }
    for (int i = 0; i < m; ++i) {
      int l, r;
      cin >> l >> r;
      for (int x = l; x < r; ++x)
        a[1][x] = 1;
    }
  }
  static int dp[2][2][all + 1][all + 1];
  memset(dp, 63, sizeof dp);
  dp[0][0][0][0] = 0;
  dp[1][1][0][0] = 0;
  for (int x = 1; x <= all; ++x) {
    for (int f = 0; f < 2; ++f) {
      for (int e = 0; e < 2; ++e) {
        for (int c = 0; c <= x && c <= all / 2; ++c) {
          int &cur = dp[f][e][x][c];
          if (a[e][x - 1])
            continue;
          if (c > 0) {  /// this guy
            cur = min(cur, dp[f][e][x - 1][c - 1]);
          }
          cur = min(cur, dp[f][e ^ 1][x - 1][x - c] + 1);
        }
      }
    }
  }
  int ans = 1e9;
  for (int f = 0; f < 2; ++f)
    for (int g = 0; g < 2; ++g)
      ans = min(ans, dp[f][g][all][all / 2] + (f ^ g));
  return ans;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
    cout << "Case #" << i << ": " << solve() << '\n';
}

