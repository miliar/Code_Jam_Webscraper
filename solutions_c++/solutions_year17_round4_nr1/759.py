#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define ll long long
#define pii pair<int,int>

int N,P,T;

ifstream fin("A.in");
ofstream fout("A.out");

int dp[105][105][105];
int vals[5];

int main() {
  fin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cout << "Working on Case #" << tt << "\n";
    fin >> N >> P;
    for (int i = 0; i < P; i++) vals[i] = 0;
    for (int i = 0; i < N; i++) {
      int a;
      fin >> a;
      vals[a%P]++;
    }
    if (P == 2) {
      fout << "Case #" << tt << ": " << (vals[0]+(vals[1]+1)/2) << "\n";
      continue;
    }
    int ans = 0;
    ans += vals[0];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        for (int k = 0; k < N; k++) dp[i][j][k] = 0;
      }
    }
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (P == 3) {
          if (i > 0) dp[i][j][0] = max(dp[i][j][0],dp[i-1][j][0]);
          if (j > 0) dp[i][j][0] = max(dp[i][j][0],dp[i][j-1][0]);
          int temp = min(i,j);
          temp += (i-temp)/3 + (j-temp)/3;
          dp[i+1][j+1][0] = max(dp[i+1][j+1][0],dp[i][j][0]+1);
          dp[i+3][j][0] = max(dp[i+3][j][0],dp[i][j][0]+1);
          dp[i][j+3][0] = max(dp[i][j+3][0],dp[i][j][0]+1);
        }
        else {
          for (int k = 0; k < N; k++) {
            if (i > 0) dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k]);
            if (j > 0) dp[i][j][k] = max(dp[i][j][k],dp[i][j-1][k]);
            if (k > 0) dp[i][j][k] = max(dp[i][j][k],dp[i][j][k-1]);
            dp[i][j+2][k] = max(dp[i][j+2][k],dp[i][j][k]+1);
            dp[i+1][j][k+1] = max(dp[i+1][j][k+1],dp[i][j][k]+1);
            dp[i+2][j+1][k] = max(dp[i+2][j+1][k],dp[i][j][k]+1);
            dp[i][j+1][k+2] = max(dp[i][j+1][k+2],dp[i][j][k]+1);
            dp[i][j][k+4] = max(dp[i][j][k+4],dp[i][j][k]+1);
            dp[i+4][j][k] = max(dp[i+4][j][k],dp[i][j][k]+1);
          }
        }
      }
    }
    int toadd = dp[vals[1]][vals[2]][vals[3]];
    if (vals[1] > 0) toadd = max(toadd,dp[vals[1]-1][vals[2]][vals[3]]+1);
    if (vals[2] > 0) toadd = max(toadd,dp[vals[1]][vals[2]-1][vals[3]]+1);
    if (vals[3] > 0) toadd = max(toadd,dp[vals[1]][vals[2]][vals[3]-1]+1);
    ans += toadd;
    fout << "Case #" << tt << ": " << ans << "\n";
  }
  return 0;
}