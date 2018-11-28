#include <bits/stdc++.h>

using namespace std;

const int N = 105, INF = int(1e9);

int cnt[4];
int dp[N][N][N][4];

int main() {
  int numTests;
  cin >> numTests;
  for (int t = 0; t < numTests; t++) {
    int n, p;
    cin >> n >> p;
    for (int i = 0; i < 4; i++) {
      cnt[i] = 0;
    }
    for (int i = 0; i < n; i++) {
      int g;
      cin >> g;
      g %= p;
      cnt[g]++;
    } 
    int ans = cnt[0];
    for (int i = 0; i <= cnt[1]; i++) {
      for (int j = 0; j <= cnt[2]; j++) {
        for (int k = 0; k <= cnt[3]; k++) {
          for (int rem = 0; rem < p; rem++) {
            dp[i][j][k][rem] = -INF;
          }
        }
      }
    }
    dp[0][0][0][0] = 1;
    for (int i = 0; i <= cnt[1]; i++) {
      for (int j = 0; j <= cnt[2]; j++) {
        for (int k = 0; k <= cnt[3]; k++) {
          for (int rem = 0; rem < p; rem++) {
            int nxt = (rem + 1) % p, add = 0;
            if (nxt == 0) {
              add = 1;
            }            
            dp[i + 1][j][k][nxt] = max(dp[i][j][k][rem] + add, dp[i + 1][j][k][nxt]);
            add = 0;
            nxt = (nxt + 1) % p;
            if (nxt == 0) {
              add = 1;
            }
            dp[i][j + 1][k][nxt] = max(dp[i][j][k][rem] + add, dp[i][j + 1][k][nxt]);
            add = 0;
            nxt = (nxt + 1) % p;
            if (nxt == 0) {
              add = 1;
            }
            dp[i][j][k + 1][nxt] = max(dp[i][j][k][rem] + add, dp[i][j][k + 1][nxt]);
          }  
        }
      }
    }
    int dpres = 0;
    for (int rem = 0; rem < p; rem++) {
      dpres = max(dpres, dp[cnt[1]][cnt[2]][cnt[3]][rem]);
    }
    if ((cnt[1] + cnt[2] * 2 + cnt[3] * 3) % p == 0) {
      dpres--;
    }
    cout << "Case #" << t + 1 << ": " << ans + dpres << endl;
  }  
  return 0;
}
