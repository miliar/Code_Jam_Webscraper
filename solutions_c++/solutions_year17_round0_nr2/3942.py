#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll N;
int L;
vector<int> digit;
//ll dp[20][11][2];
ll solve(int pos,int lastdigit,int isEqual,ll val) {
  if(pos == L) {
     //dp[pos][lastdigit][isEqual] = val;
     return val;
  }
  //if(dp[pos][lastdigit][isEqual] != -1) return dp[pos][lastdigit][isEqual];
  ll res = 0;
  if(pos == 0) {
     for(int i=lastdigit;i<=digit[pos];i++) {
          if(i < digit[pos]) {
               res = max(res,solve(pos+1,i,0,val*10+i));
          }
          else {
               res = max(res,solve(pos+1,i,1,val*10+i));
          }
     }
  }
  else {
     if(isEqual == 0) {
        for(int i=lastdigit;i<10;i++) {
           res = max(res,solve(pos+1,i,0,val*10+i));
        }
     }
     else {
        for(int i=lastdigit;i<=digit[pos];i++) {
           if(i < digit[pos]) res = max(res,solve(pos+1,i,0,val*10+i));
           else res = max(res,solve(pos+1,i,1,val*10+i));
        }
     }
  }
  //dp[pos][lastdigit][isEqual] = res;
  return res;
}
int main() {
  freopen("B-large.in","r",stdin);
  freopen("ans.txt","w",stdout);
  int T;
  cin >> T;
  for(int tt=1;tt<=T;tt++) {
     printf("Case #%d: ",tt);
     cin >> N;
     ll M = N;
     digit.clear();
     while(M) {
          int d = M%10;
          M /= 10;
          digit.push_back(d);
     }
     reverse(digit.begin(),digit.end());
     L = digit.size();
     //memset(dp,-1,sizeof dp);
     ll res = solve(0,0,0,0);
     cout << res << endl;
  }
  return 0;
}
