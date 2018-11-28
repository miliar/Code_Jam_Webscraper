#include <bits/stdc++.h>
using namespace std;
namespace {
  #ifdef LOCAL_JUDGE
    #define trace(...) cerr << ">> "; __f(#__VA_ARGS__, __VA_ARGS__)
    template <typename Arg1>
    void __f(const char* name, Arg1&& arg1) {
      cerr << name << " = " << arg1 << std::endl;
    }
    template <typename Arg1, typename... Args>
    void __f(const char* names, Arg1&& arg1, Args&&... args) {
      const char* comma = strchr(names + 1, ',');
      cerr.write(names, comma - names) << " = " << arg1<<" | ";__f(comma+1, args...);
    }
    #define debug cerr << ">>> line " << __LINE__ << '\n';
  #else
    #define trace(...)
    #define debug
  #endif
};
typedef long long LL;

const int T = 24 * 60 + 1, Th = 12 * 60, INF = 1e5;
int dp[T][T][2][2]; // [T_0, T_1, prev, start]
int poss[T];
bool exc[T];

void solve() {
  fill(poss, poss + T, 2);
  fill(exc, exc + T, true);
  int n, m; cin >> n >> m;
  for (int i = 0; i < n + m; i++) {
    int l, r; cin >> l >> r;
    for (int t = l + 1; t <= r; t++) poss[t] = (i < n);
    for (int t = l + 1; t < r; t++) exc[t] = false;
  }

  dp[0][0][0][0] = dp[0][0][1][0] = 0;
  dp[0][0][0][1] = dp[0][0][1][1] = 0;
  for (int i = 1; i < T; i++) {
    dp[i][0][0][0] = (poss[i] != 1) ? dp[i - 1][0][0][0] : INF;
    dp[i][0][1][0] = INF;
    dp[i][0][1][1] = dp[i][0][0][1] = INF;
  }
  for (int j = 1; j < T; j++) {
    dp[0][j][0][1] = INF;
    dp[0][j][1][1] = (poss[j] != 0) ? dp[0][j - 1][1][1] : INF;
    dp[0][j][1][0] = dp[0][j][0][0] = INF;
  }
  for (int i = 1; i <= Th; i++) {
    for (int j = 1; j <= Th; j++) {
      dp[i][j][0][0] = dp[i][j][1][0] = INF;
      dp[i][j][0][1] = dp[i][j][1][1] = INF;
      if (poss[i + j] != 1) {
        dp[i][j][0][0] = dp[i - 1][j][0][0];
        dp[i][j][0][1] = dp[i - 1][j][0][1];
        if (exc[i + j - 1]) {
          dp[i][j][0][0] = min(dp[i][j][0][0], 1 + dp[i - 1][j][1][0]);
          dp[i][j][0][1] = min(dp[i][j][0][1], 1 + dp[i - 1][j][1][1]);
        }
      }
      if (poss[i + j] != 0) {
        dp[i][j][1][0] = dp[i][j - 1][1][0];
        dp[i][j][1][1] = dp[i][j - 1][1][1];
        if (exc[i + j - 1]) {
          dp[i][j][1][0] = min(dp[i][j][1][0], 1 + dp[i][j - 1][0][0]);
          dp[i][j][1][1] = min(dp[i][j][1][1], 1 + dp[i][j - 1][0][1]);
        }
      }
    }
  }
  int ans = min({dp[Th][Th][0][0], dp[Th][Th][1][1], dp[Th][Th][0][1] + 1, dp[Th][Th][1][0] + 1});
  cout << ans << '\n';
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL);
  int t; cin >> t;
  for (int it = 1; it <= t; it++) {
    cout << "Case #" << it << ": ";
    solve();
  }
  return 0;
}
