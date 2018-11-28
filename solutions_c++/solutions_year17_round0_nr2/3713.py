
#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define pii pair<int, int>
#define pll pair<long long, long long>
#define V  vector
#define pb  push_back
#define mp  make_pair
#define pq priority_queue
#define FIN(x) freopen(x,"r",stdin)
#define FOUT(x) freopen(x,"w",stdout)
#define ALL(x) x.begin(),x.end()
#define M(a,x) memset(a,x,sizeof(a))
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define scs(x) scanf("%s",x);
#define SZ(x) (int)x.size()
#define print(x) printf("%d",x);
#define nl printf("\n")
#define fr first
#define se second
#define printl(x) printf("%lld",x)
#define F(i,a,n) for(int i=a;i<n;i++)
#define INF 4000000000000000000LL
#define LL long long

const int N = 1e5+5;
LL dp[22][2][10];
vector < char > ans;
string s;
LL num;
string f(long long num) {
  string ret = "";
  while(num) {
    ret += (num % 10 +'0');
    num /= 10;
  }
  reverse(ret.begin(),ret.end());
  return ret;
}
bool solve(int pos,int tight,int last) {
  if(pos == s.size()) {
    return true;
  }
  if(dp[pos][tight][last] != -1) return dp[pos][tight][last];
  if(tight == 0) {
    char temp = '9';
    ans.pb(temp);
    if(solve(pos+1,0,9)) return true;
    ans.pop_back();
  }
  else {
    if(s[pos]-'0' >= last) {
      ans.pb(s[pos]);
      if(solve(pos+1,1,s[pos]-'0')) return dp[pos][tight][last] = true;
      ans.pop_back();
    }
    for(int i = s[pos]-'0'-1; i>=last ; i--) {
      ans.push_back(char(i+'0'));
      if(solve(pos+1,0,i)) return dp[pos][tight][last] = true;
      ans.pop_back();
    }
  }
  return dp[pos][tight][last] = false;
}
int cs = 0;
int main() {
  FIN("lg2.in");
  FOUT("lg2.out");
  int t;
  S(t);
  while(t--) {
//  F(i,1,100001) {
    cin >> num;
//    num = i;
    s = f(num);
    M(dp,-1);
    ans.clear();
    if(solve(0,1,0)) {
      reverse(ans.begin(),ans.end());
      while(ans.size() && ans.back() == '0') ans.pop_back();
      reverse(ans.begin(),ans.end());
      if(!ans.size()) ans.pb('0');
      printf("Case #%d: ",++cs);
      for(auto x : ans) cout << x;
      cout << endl;
    }
  }
}
