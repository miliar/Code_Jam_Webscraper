#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main() {
  int T;
  cin >> T;

  for(int t = 0; t < T; t++) {
    int N, P;
    cin >> N >> P;

    vector<int> peopleInGroupModP(4, 0);

    for(int i = 0; i < N; i++) {
      int G;
      cin >> G;
      peopleInGroupModP[G % P] += 1;

    }





    int dp[peopleInGroupModP[1] + 1][peopleInGroupModP[2] + 1][peopleInGroupModP[3] + 1][P];

    for(int i = 0; i <= peopleInGroupModP[1]; i++) {
      for(int j = 0; j <= peopleInGroupModP[2]; j++) {
        for(int k = 0; k <= peopleInGroupModP[3]; k++) {
          for(int l = 0; l < P; l++) {
            dp[i][j][k][l] = -1;
          }
        }
      }
    }

    dp[peopleInGroupModP[1]][peopleInGroupModP[2]][peopleInGroupModP[3]][0] = peopleInGroupModP[0];

    for(int i = peopleInGroupModP[1]; i >= 0; i--) {
      for(int j = peopleInGroupModP[2]; j >= 0; j--) {
        for(int k = peopleInGroupModP[3]; k >= 0; k--) {
          int l = (peopleInGroupModP[1] - i);
          if(P > 2) {
            l +=  (peopleInGroupModP[2] - j) * 2;
          }
          if(P > 3) {
            l += (peopleInGroupModP[3] - k) * 3;
          }
          l %= P;


          if(i < peopleInGroupModP[1] && dp[i + 1][j][k][(l - 1 + P) % P] != -1) {
            if((l - 1 + P) % P == 0) {
              dp[i][j][k][l] = max(dp[i][j][k][l], dp[i + 1][j][k][(l - 1 + P) % P] + 1);
            }else {
              dp[i][j][k][l] = max(dp[i][j][k][l], dp[i + 1][j][k][(l - 1 + P) % P]);
            }
          }

          if(P > 2 && j < peopleInGroupModP[2] && dp[i][j + 1][k][(l - 2 + P) % P] != -1) {
            if((l - 2 + P) % P == 0) {
              dp[i][j][k][l] = max(dp[i][j][k][l], dp[i][j + 1][k][(l - 2 + P) % P] + 1);
            }else {
              dp[i][j][k][l] = max(dp[i][j][k][l], dp[i][j + 1][k][(l - 2 + P) % P]);
            }
          }

          if(P > 3 && k < peopleInGroupModP[3] && dp[i][j][k + 1][(l - 3 + P) % P] != -1) {
            if((l - 3 + P) % P == 0) {
              dp[i][j][k][l] = max(dp[i][j][k][l], dp[i][j][k + 1][(l - 3 + P) % P] + 1);
            }else {
              dp[i][j][k][l] = max(dp[i][j][k][l], dp[i][j][k + 1][(l - 3 + P) % P]);
            }
          }

        }
      }
    }

    int ans = 0;

    for(int l = 0; l < P; l++) {
      // cout << dp[0][0][0][l] << endl;
      ans = max(ans, dp[0][0][0][l]);
    }
    cout << "Case #" << t + 1 << ": ";
    cout << ans << endl;

  }

}
