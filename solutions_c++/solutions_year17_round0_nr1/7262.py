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
const int N = 1e5+10; 
inline int add(int x,int y){
  x += y;
  if(x >= mod) x -= mod;
  return x;
}
inline int mul(int x,int y){
  x = (1LL * x * y) % mod;
  return x;
}
int main(){
  fast;
  int t;
  cin >> t;
  FOR(_t,1,t){
  	cout << "Case #" << _t << ": "; 
  	string s;cin >> s;
  	int n = sz(s);
  	int k;cin >> k;int kk = k + 1;
  	vi v(n);
  	FOR(i,0,n-1){
  		if(s[i] == '-')v[i] = 1;
  	}
  	int ans = 0;
  	FOR(i,0,n-k){
  		if(v[i] == 1){
  			FOR(j,i,i+k-1){
  				v[j] ^= 1;
  			}
  			ans++;
  		}
  	}
  	int flag = 1;
  	FOR(i,n-k+1,n-1){
  		if(v[i] == 1){
  			flag = 0;
  		}
  	}
  	if(flag){
  		cout << ans << "\n";
  	}
  	else{
  		cout << "IMPOSSIBLE\n";
  	}
  }
  return 0;
}