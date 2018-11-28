#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second

const int kMaxN = 1005;
const double PI = acos(-1.0);

pii v[kMaxN];
ll dp[kMaxN][kMaxN];

int main() {
  cin.sync_with_stdio(false);

  int t;
  cin >> t;

  for (int T = 1; T <= t; T++) {
    int n, k;
    cin >> n >> k;

    for (int i = 1; i <= n; i++) {
      cin >> v[i].fi >> v[i].se;
    }

    sort(v + 1, v + n + 1);
    reverse(v + 1, v + n + 1);

    for (int i = 0; i <= n; i++) {
      for (int j = 0; j <= k; j++) {
        dp[i][j] = 0;
      }
    }

    for (int i = 1; i <= n; i++) {
      dp[i][1] = max(dp[i - 1][1], 1LL * v[i].fi * v[i].fi + 2LL * v[i].fi * v[i].se);
      for (int j = 2; j <= k; j++) {
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + 2LL * v[i].fi * v[i].se);
      }
    }

    cout << "Case #" << T << ": ";
    cout << fixed << setprecision(9) << 1.0 * dp[n][k] * PI << '\n';
  }

  return 0;
}
