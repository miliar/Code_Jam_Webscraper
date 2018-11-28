#include "bits/stdc++.h"
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;

#define fill(a,x) memset(a,x,sizeof(a)) 
#define pb push_back
#define sz(x) (int)x.size()
#define all(x) x.begin(),x.end() 
#define F first
#define S second
#define FOR(i,a,b) for(int i = a; i<=b; ++i)
#define NFOR(i,a,b) for(int i = a; i>=b; --i)
#define fast ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0)
const ll INF = 1e18;
const int mod = 1e9+7;
const int N = 1e3+10; 
inline int add(int x,int y){
  x += y;
  if(x >= mod) x -= mod;
  return x;
}
inline int mul(int x,int y){
  x = (1LL * x * y) % mod;
  return x;
}
ll dp[N][N];
ll r[N],h[N];
ll DP(int n,int k){
  if(n == -1)return 0;
  if(k == 0)return 0;
  ll &ret = dp[n][k];
  if(k == 1){
    return ret = max(DP(n-1,k),2*r[n]*h[n]);
  }
  ret = DP(n-1,k);
  ret = max(ret,DP(n-1,k-1) + 2*r[n]*h[n]);
}
int main(){
  fast;
  int t;
  cin >> t;
  FOR(_t,1,t){
    int n,k;
    cin >> n >> k;
    fill(dp,-1);
    cout << "Case #" << _t << ": ";
    cout <<  fixed << setprecision(12);
    ll ans = 0;
    vector<pair<ll,ll> > lol(n);
    FOR(i,0,n-1)cin >> lol[i].F >> lol[i].S;
    sort(all(lol));
    FOR(i,0,n-1){
      r[i] = lol[i].F;
      h[i] = lol[i].S;
    }
    FOR(i,0,n-1){
      ans = max(ans,r[i]*r[i] + 2*r[i]*h[i]+ DP(i-1,k-1));
    }
    cout << 1.0*2*acos(0)*ans << "\n";
  }
  return 0;
}