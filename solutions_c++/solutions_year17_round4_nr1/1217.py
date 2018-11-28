#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<utility>
#include<iomanip>

using namespace std;

int dp[3][101][101][101][101];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(12);

  for (int64_t P = 2; P <= 4; ++P) {
    for (int64_t m0 = 0; m0 <= 100; ++m0) {
      for (int64_t m1 = 0; m1 <= 100; ++m1) {
        for (int64_t m2 = 0; m2 <= 100; ++m2) {
          if (m2 > 0 && P <= 2) continue;
          for (int64_t m3 = 0; m3 <= 100; ++m3) {
            if (m3 > 0 && P <= 3) continue;
            if (m0 > 0 || m1 > 0 || m2 > 0 || m3 > 0) {
              dp[P-2][m0][m1][m2][m3] = 1000;
            }
            if (m0 > 0) {
              int64_t over = (m1+2*m2+3*m3)%P;
              if (over == 0) {
                dp[P-2][m0][m1][m2][m3] = min(dp[P-2][m0-1][m1][m2][m3], dp[P-2][m0][m1][m2][m3]);
              } else {
                dp[P-2][m0][m1][m2][m3] = min(dp[P-2][m0-1][m1][m2][m3] + 1, dp[P-2][m0][m1][m2][m3]);
              }
            }
            if (m1 > 0) {
              int64_t over = ((m1 - 1) + 2*m2 + 3*m3)%P;
              if (over == 0) {
                dp[P-2][m0][m1][m2][m3] = min(dp[P-2][m0][m1-1][m2][m3], dp[P-2][m0][m1][m2][m3]);
              } else {
                dp[P-2][m0][m1][m2][m3] = min(dp[P-2][m0][m1-1][m2][m3] + 1, dp[P-2][m0][m1][m2][m3]);
              }
            }
            if (m2 > 0) {
              int64_t over = (m1 + 2*(m2 - 1) + 3*m3)%P;
              if (over == 0) {
                dp[P-2][m0][m1][m2][m3] = min(dp[P-2][m0][m1][m2-1][m3], dp[P-2][m0][m1][m2][m3]);
              } else {
                dp[P-2][m0][m1][m2][m3] = min(dp[P-2][m0][m1][m2-1][m3] + 1, dp[P-2][m0][m1][m2][m3]);
              }
            }
            if (m3 > 0) {
              int64_t over = (m1 + 2*m2 + 3*(m3-1))%P;
              if (over == 0) {
                dp[P-2][m0][m1][m2][m3] = min(dp[P-2][m0][m1][m2][m3-1], dp[P-2][m0][m1][m2][m3]);
              } else {
                dp[P-2][m0][m1][m2][m3] = min(dp[P-2][m0][m1][m2][m3-1] + 1, dp[P-2][m0][m1][m2][m3]);
              }
            }
            //cout << P-2 << "(" << m0 << "," << m1 << "," << m2 << "," << m3 << ")" << dp[P-2][m0][m1][m2][m3] << '\n';
          }
        }
      }
    }
  }

  int64_t T;
  cin >> T;

  for (int64_t t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    int64_t N, P;
    cin >> N >> P;
    int64_t m0=0, m1=0, m2=0, m3=0;
    for (int64_t i = 0; i < N; ++i) {
      int64_t G;
      cin >> G;
      if (G%P == 0) m0++;
      if (G%P == 1) m1++;
      if (G%P == 2) m2++;
      if (G%P == 3) m3++;
    }
    cout << N - dp[P-2][m0][m1][m2][m3] << '\n';
  }

  return 0;
}

