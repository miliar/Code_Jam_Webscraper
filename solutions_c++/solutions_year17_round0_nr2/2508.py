#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
typedef long long ll;
const ll mod = 1e9+7;

void solve(int case_num){
  printf("Case #%d: ",case_num);
  string n;
  cin >> n;
  int size = (int)n.size();
  ll dp[20][10][2];
  fill(dp[0][0], dp[0][0]+20*10*2, (ll)-1);
  dp[0][0][0] = 0;
  for(int i = 0;i < size;++i){
    int num = n[i] - '0';
    for(int j = 0;j < 10;++j){
      for(int k = j;k < 10;++k){
        if(dp[i][j][1] != -1){
          ll next1 = dp[i][j][1] * 10 + k;
          dp[i+1][k][1] = max(dp[i+1][k][1],next1);
        }
        if(dp[i][j][0] != -1){
          ll next0 = dp[i][j][0] * 10 + k;
          if(k < num){
            dp[i+1][k][1] = max(dp[i+1][k][1],next0);
          }else if(k == num){
            dp[i+1][k][0] = max(dp[i+1][k][0],next0);
          }
        }
      }
    }
  }
  ll res = 0;
  for(int i = 0;i < 10;++i){
    res = max(res,dp[size][i][0]);
    res = max(res,dp[size][i][1]);
  }
  cout << res << endl;
}


int main(void){
  int n;
  cin >> n;
  for(int i = 0;i < n;++i){
    solve(i+1);
  }
  return 0;
}
