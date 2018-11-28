#include <bits/stdc++.h>

using namespace std;

const int DAY = 24 * 60;
const int INF = int(1e9);

int used[DAY + 1];
int dp[DAY + 1][DAY + 1][2];

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    for (int j = 0; j <= DAY; j++) {
      used[j] = 0;
      for (int k = 0; k <= j; k++) {
        dp[j][k][0] = dp[j][k][1] = INF;
      }  
    }
    int ac, aj;
    cin >> ac >> aj;
    for (int j = 0; j < ac; j++) {
      int l, r;
      cin >> l >> r;
      for (int k = l; k < r; k++) {
        used[k] = 1;
      }
    }
    for (int j = 0; j < aj; j++) {
      int l, r;
      cin >> l >> r;
      for (int k = l; k < r; k++) {
        used[k] = 2;
      }
    }
    /*for (int j = 0; j < DAY; j++) {
      cout << used[j] << " ";
    }
    cout << endl;*/
    dp[0][0][0] = 0;
    for (int j = 0; j < DAY; j++) {
      for (int k = 0; k <= j; k++) {
        for (int t = 0; t < 2; t++) {
          if (dp[j][k][t] == INF) {
            continue;
          }
          //cout << j << " " << k << " " << t << endl;
          if (!used[j] || used[j] == t + 1) {
            dp[j + 1][k + t][t] = min(dp[j + 1][k + t][t], dp[j][k][t]);
            //cout << "\t" << j + 1 << " " << k + t << " " << t << endl;
          }
          if (!used[j] || used[j] == 2 - t) {
            dp[j + 1][k + 1 - t][1 - t] = min(dp[j + 1][k + 1 - t][1 - t], dp[j][k][t] + 1);
            //cout << "\t" << j + 1 << " " << k + 1 - t << " " << 1 - t << endl;
          }

        }
      }
    }
    int res0 = min(dp[DAY][DAY / 2][0], dp[DAY][DAY / 2][1] + 1);
    for (int j = 0; j <= DAY; j++) {      
      for (int k = 0; k <= j; k++) {
        dp[j][k][0] = dp[j][k][1] = INF;
      }  
    }    
    dp[0][0][1] = 0;
    for (int j = 0; j < DAY; j++) {
      for (int k = 0; k <= j; k++) {
        for (int t = 0; t < 2; t++) {
          if (dp[j][k][t] == INF) {
            continue;
          }
          //cout << j << " " << k << " " << t << endl;
          if (!used[j] || used[j] == t + 1) {
            dp[j + 1][k + t][t] = min(dp[j + 1][k + t][t], dp[j][k][t]);
            //cout << "\t" << j + 1 << " " << k + t << " " << t << endl;
          }
          if (!used[j] || used[j] == 2 - t) {
            dp[j + 1][k + 1 - t][1 - t] = min(dp[j + 1][k + 1 - t][1 - t], dp[j][k][t] + 1);
            //cout << "\t" << j + 1 << " " << k + 1 - t << " " << 1 - t << endl;
          }
        }
      }
    }
    int res1 = min(dp[DAY][DAY / 2][0] + 1, dp[DAY][DAY / 2][1]);
    /*for (int j = 0; j <= DAY; j++) {      
      for (int k = 0; k <= j; k++) {
        printf("(%d, %d) ", dp[j][k][0], dp[j][k][1]);
      }
      puts("");
    }*/    
    cout << "Case #" << i + 1 << ": " << min(res0, res1) << endl;
  }
}