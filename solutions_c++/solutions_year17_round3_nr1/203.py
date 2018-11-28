#include <bits/stdc++.h>

#define all(x) x.begin(),x.end()
using namespace std;

typedef long long ll;
typedef long double ld;

int run() {
  ll n, k;
  cin >> n >> k;
  vector<vector<ld>> dp(n, vector<ld>(k + 1, 0));
  vector<vector<ld>> prefmax(n, vector<ld>(k + 1, 0));
  vector<pair<ll, ll>> mas(n);
  for (int i = 0; i < n; ++i) {
    cin >> mas[i].first >> mas[i].second;
  }
  sort(mas.begin(), mas.end());
  for (int i = 0; i < n; ++i) {
    for (int j = 1; j <= k; ++j) {
      if (i != 0)
        dp[i][j] = prefmax[i - 1][j - 1] + 2 * M_PI * mas[i].first * mas[i].second;
      else dp[i][j] = 2 * M_PI * mas[i].first * mas[i].second;
      if (i != 0)
        prefmax[i][j] = max(prefmax[i - 1][j], dp[i][j]);
      else prefmax[i][j] = dp[i][j];
    }
  }
  ld maxans = 0;
  for (int i = 0; i < n; ++i) {
    maxans = max(maxans, dp[i][k] + mas[i].first * mas[i].first * M_PI);
  }
  cout << fixed << setprecision(10) << maxans << endl;
  return 0;
}

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  ll t;
  cin >> t;
  for (int q = 0; q < t; ++q) {
    cout << "Case #" << q + 1 << ": ";
    run();
  }
  return 0;
}