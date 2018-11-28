#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
string s;
long long k;
ll dp[20][10][2];
ll solve(long long idx, long long bk, bool chk){
  if(idx == s.size())
    return dp[idx][bk][chk] = 1;
  ll &ret = dp[idx][bk][chk];
  if(~ret)
    return ret;
  ret = 0;
  for(long long i = bk; i <= (chk?9:(s[idx] - '0')); i++){
    ret |= solve(idx + 1, i, chk|(i != (s[idx] - '0')));
  }
  return ret;
}
void trace(long long idx, long long bk, bool chk){
  if(idx == s.size()){
    return;
  }

  for(long long i = (chk?9:(s[idx] - '0')); i >= bk; i--){
    //cout << dp[idx + 1][i][chk|(i!=(s[idx] - '0'))] << endl;
    if(dp[idx + 1][i][chk|(i!=(s[idx] - '0'))] == 1){
      if(i)
        cout << i;
      trace(idx + 1, i, chk |(i != (s[idx] - '0')));
      break;
    }
  }

}
int main(){
  freopen("B-large.in","r",stdin);
  freopen("out.out","w",stdout);
  long long t;
  cin >> t;
  long long cas = 0;
  while(t--){
    cin >> s;
    memset(dp, -1, sizeof dp);
    printf("Case #%d: ", ++cas);
    solve(0,0,0);
    trace(0,0,0);
    puts("");
  }


  return 0;
}
