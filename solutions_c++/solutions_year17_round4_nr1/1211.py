#include <bits/stdc++.h>

using namespace std;

const int MAXN = 105;

int dp[MAXN][MAXN][MAXN][4];

int main() {

  int tc;
  cin >> tc;

  for (int t = 1; t <= tc; t++) {
    cout << "Case #" << t << ": ";
    int n, p;
    cin >> n >> p;

    vector<int> cnts(4);

    for (int i = 0; i < n; i++) {
      int x;
      cin >> x;
      cnts[x % p]++;
    }

    memset(dp, 0, sizeof dp);
    int best = 0;

    for (int c1 = 0; c1 <= cnts[1]; c1++) {
      for (int c2 = 0; c2 <= cnts[2]; c2++) {
        for (int c3 = 0; c3 <= cnts[3]; c3++) {
          bool last = c1 == cnts[1] && c2 == cnts[2] && c3 == cnts[3];
          for (int lo = 0; lo < p; lo++) {
            int &ans = dp[c1][c2][c3][lo];
            if (c1) {
              int olo = (p + lo + (p - 1)) % p;
              ans = max(ans, (lo ? 0 : 1) + dp[c1-1][c2][c3][olo]);
            }
            if (c2) {
              int olo = (p + lo + (p - 2)) % p;
              ans = max(ans, (lo ? 0 : 1) + dp[c1][c2 - 1][c3][olo]);
            }
            if (c3) {
              int olo = (p + lo + (p - 3)) % p;
              ans = max(ans, (lo ? 0 : 1) + dp[c1][c2][c3 - 1][olo]);
            }
          }
          if (last) {
            best = max(best, dp[c1][c2][c3][0]);
          }
        }
      }
    }

    cout << cnts[0] + best << endl;
  }

  return 0;
}
