#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve() {
  int n, q;
  cin >> n >> q;
  vector <double> e(n), s(n);
  for (int i = 0; i < n; ++i) {
    cin >> e[i] >> s[i];
  }
  vector <vector <double> > dist(n, vector <double>(n, 0));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      cin >> dist[i][j];
      if (dist[i][j] < 0) {
        dist[i][j] = 1e18;
      }
    }
  }
  for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
      }
    }
  }
  for (int i = 0; i < q; ++i) {
    int start, finish;
    cin >> start >> finish;
    --start, --finish;
    vector <double> dp(n, 1e18);
    vector <bool> u(n);
    dp[start] = 0;
    for (int step = 0; step < n; ++step) {
      int v = -1;
      for (int i = 0; i < n; ++i) {
        if (u[i])
          continue;
        if (dp[i] < 1e18 && (v == -1 || dp[v] > dp[i])) {
          v = i;
        }
      }
      if (v == -1) {
        break;
      }
      u[v] = 1;
      for (int to = 0; to < n; ++to) {
        if (dist[v][to] > e[v])
          continue;
        dp[to] = min(dp[to], dp[v] + dist[v][to] / s[v]);
      }
    }
    cout << dp[finish] << ' ';
  }
  cout << endl;
  return;
}

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
#endif
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);
  cout.precision(10);
  cout << fixed;
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }
}