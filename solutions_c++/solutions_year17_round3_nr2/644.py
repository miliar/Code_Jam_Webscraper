#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long ll;

const int TM = 1441;

int dp[TM][TM][2];
bool busy[2][TM];

int main(void){
  int T;
  cin >> T;
  for (int tt = 0; tt < T; ++tt) {
    cout << "Case #" << tt+1 << ": ";

    for(int i = 0; i < 2; ++i) {
      fill_n(busy[i], TM, false);
    }

    int Ac, Aj; //, C, D;
    cin >> Ac >> Aj;
    vector<int> C(Ac), D(Ac), J(Aj), K(Aj);

    for(int i = 0; i < Ac; ++i) cin >> C[i] >> D[i];
    for(int i = 0; i < Aj; ++i) cin >> J[i] >> K[i];
    for(int i = 0; i < Ac; ++i) fill_n(busy[0] + C[i], D[i] - C[i], true);
    for(int i = 0; i < Aj; ++i) fill_n(busy[1] + J[i], K[i] - J[i], true);

    /*/
    for(int i = 0; i < 24; ++i) {
      printf("%3d: ", i);
      for(int j = 0; j < 6; ++j)
        if(busy[0][i*60 + j*10])
          cout << 'C';
        else if(busy[1][i*60 + j*10])
          cout << 'J';
        else
          cout << '-';
      cout << endl;
    }
    //*/

    int res = 1440;
    for(int k = 0; k < 2; ++k) {
      for(int i = 0; i < TM; ++i)
        for(int j = 0; j < TM; ++j)
          dp[i][j][0] = dp[i][j][1] = TM;

      if(busy[k][0]) continue;

      dp[0][0][k] = 1;
      for(int time = 1; time < TM; ++time) {
        for(int came = 0; came <= min(time, TM/2); ++came) {
          if(!busy[0][time]) {
            dp[time][came][0] = min(dp[time][came][0], dp[time-1][came][1] + 1);
            if(came > 0) dp[time][came][0] = min(dp[time][came][0], dp[time-1][came-1][0]);
          }
          if(!busy[1][time]) {
            dp[time][came][1] = min(dp[time][came][1], dp[time-1][came][1]);
            if(came > 0) dp[time][came][1] = min(dp[time][came][1], dp[time-1][came-1][0] + 1);
          }
        }
      }
      for(int j = 0; j < 2; ++j)
        res = min(res, dp[1440][720][j] - (j == k));
    }

    cout << res << endl;
  }

  return 0;
}
