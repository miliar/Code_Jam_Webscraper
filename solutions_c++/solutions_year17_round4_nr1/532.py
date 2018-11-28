#include <iostream>
#include <cstring>
#include<vector>
using namespace std;
int N,P;
int dp[4][101][101][101];
int have[4][101][101][101];

int rec(int cur, int r1, int r2, int r3, int p) {
  if(r1 == 0 && r2 == 0 && r3 == 0) {
    return 0;
  }
  if(have[cur][r1][r2][r3]) return dp[cur][r1][r2][r3]; 
  int tans = (cur == 0) ? 1 : 0;
  int ans = 0;
  if(r1) ans = max(ans, tans + rec((cur + 1) % p, r1 - 1, r2, r3, p));
  if(r2) ans = max(ans, tans + rec((cur + 2) % p, r1, r2 - 1, r3, p));
  if(r3) ans = max(ans, tans + rec((cur + 3) % p, r1, r2, r3 - 1, p));
  have[cur][r1][r2][r3] = 1;
  dp[cur][r1][r2][r3] = ans;
  return ans;
}

int main() {
  int T;
  cin >> T;
  for(int cz = 1; cz <= T; cz++) {
    cout << "Case #" << cz <<": ";
    cin >> N >> P;
    vector<int> p(4);
    for(int i = 0; i < N; i++) {
      int t; 
      cin >> t;
      p[t % P]++;
    }
    memset(dp, 0, sizeof(dp));
    memset(have, 0, sizeof(have));
    cout << p[0] + rec(0, p[1], p[2], p[3], P) << endl;
  }
}
