#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

int main() {
  ios::sync_with_stdio(false);

  int t;
  cin >> t;

  for (int cs = 0; cs < t; cs++) {
    int n, p;
    cin >> n >> p;

    vector<int> v = {0, 0, 0, 0};
    int ans = 0;

    for (int i = 0; i < n; i++) {
      int x;
      cin >> x;
      v[x % p]++;
    }

    int a = v[1], b = v[2], c = v[3];

    vector <vector <vector <vector <int>>>> dp(a + 2, vector <vector <vector <int>>>(b + 2, vector <vector <int>>(c + 2, vector <int> (p, numeric_limits<int>::min()))));
    dp[0][0][0][0] = v[0];

    for (int i = 0; i <= a; i++) {
      for (int j = 0; j <= b; j++) {
        for (int k = 0; k <= c; k++) {
          for (int s = 0; s < p; s++) {
            dp[i + 1][j][k][(s + 1) % p] = max(dp[i + 1][j][k][(s + 1) % p], dp[i][j][k][s] + (s == 0));
            dp[i][j + 1][k][(s + 2) % p] = max(dp[i][j + 1][k][(s + 2) % p], dp[i][j][k][s] + (s == 0));
            dp[i][j][k + 1][(s + 3) % p] = max(dp[i][j][k + 1][(s + 3) % p], dp[i][j][k][s] + (s == 0));
            if (i == a && j == b && k == c) {
              ans = max(ans, dp[i][j][k][s]);
            }
          }
        }
      }
    }

    cout << "Case #" << cs + 1 << ": " << ans << endl;
  }

  return 0;
}
