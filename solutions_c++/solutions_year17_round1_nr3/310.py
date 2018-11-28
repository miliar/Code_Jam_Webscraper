#include <bits/stdc++.h>

using namespace std;

void chmin(int &a, int b)
{
  a = min(a, b);
}

const int INF = 1LL << 30;

int dp[101][101][101];
int dp2[101][101][101];


void solve()
{
  int Hd, Ad, Hk, Ak, B, D;
  cin >> Hd >> Ad >> Hk >> Ak >> B >> D;


  fill_n(**dp, 101 * 101 * 101, INF);
  dp[Ad][Hd][Ak] = Hk;

  for(int i = 0; i < 300; i++) {
    fill_n(**dp2, 101 * 101 * 101, INF);
    for(int j = 0; j < 101; j++) {
      for(int k = 0; k < 101; k++) {
        for(int l = 0; l < 101; l++) {
          if(dp[j][k][l] == INF) continue;
          chmin(dp2[j][k][l], dp[j][k][l] - j);
          chmin(dp2[min(100, j + B)][k][l], dp[j][k][l]);
          chmin(dp2[j][Hd][l], dp[j][k][l]);
          chmin(dp2[j][k][max(0, l - D)], dp[j][k][l]);
        }
      }
    }
    fill_n(**dp, 101 * 101 * 101, INF);

    for(int j = 0; j < 101; j++) {
      for(int k = 0; k < 101; k++) {
        for(int l = 0; l < 101; l++) {
          if(dp2[j][k][l] == INF) continue;
          if(dp2[j][k][l] <= 0) {
            cout << i + 1 << endl;
            return;
          }
          if(k - l <= 0) continue;
          dp[j][k - l][l] = dp2[j][k][l];
        }
      }
    }
  }

  cout << "IMPOSSIBLE" << endl;
}


int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
}
