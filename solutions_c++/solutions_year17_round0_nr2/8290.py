#include "bits/stdc++.h"

using namespace std;

using ll = long long;
using VL = vector<ll>;
using VVL = vector<VL>;

int main(int argc, char const *argv[])
{
  freopen("BL.in", "r", stdin);
  freopen("BL.out", "w", stdout);
  VVL dp(20, VL(12, 0));
  for(int i = 1 ; i <= 9 ; i++)
    dp[1][i] = 1;

  for(int len = 2 ; len<20 ; len++) {
    ll sum = 0;
    for(int stDig = 9 ; stDig >= 1 ; stDig--) {
      dp[len][stDig] = sum + dp[len - 1][stDig];
      sum += dp[len-1][stDig];
    }
  }

  for(int len = 1 ; len < 20 ; len++) {
    for(int d = 1 ; d<=9 ; d++) {
      dp[len][d] += dp[len][d-1];
    }
  }

  int tcase,cas=1;

  cin>>tcase;
  string str;

  while(tcase--) {
    cin>>str;

    long long sol = 0;
    int len = (int)str.size();

    for(int i = 1; i < len ; i++) {
      sol += dp[i][9];
    }
    
    long long tmpsol = 0;

    int last = 1;
    int f = 1;
    string chk = string(len-1,'9');

    for(int i = 0 ; i<len ; i++) {
      int cur = str[i] - '0';
      if(last > cur) {
        f = 0;
        break;
      }
      
      if(last <= cur) {
        long long val = (dp[len-i][cur-1] - dp[len-i][last-1]);
        sol += val;
        if(val) {
          chk = str.substr(0, i);
          chk.push_back((str[i]-1));
          chk += string(len-i-1, '9');
        }
      }
      last = cur;
    }

    sol += f;
    
    if(f) chk = str;

    cout<<"Case #"<<cas++<<": "<<chk<<endl;
  }

  return 0;
}