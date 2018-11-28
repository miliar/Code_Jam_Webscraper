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
ll f(ll n){
	ll nn = n;
	int ix = 0;
	int xx = -1;
	while(n > 9){
		int x = n%10;
		n /= 10;
		int y = n%10;
		if(y > x){
			xx = ix;
		}
		ix++;
	}
	if(xx == -1)return nn;
	n = nn;
	FOR(i,1,xx+1){
		n /= 10;
	}
	n--;
	ll x = f(n);
	FOR(i,1,xx+1){
		x = x*10 + 9;
	}
	return x;
}
int main(){
  fast;
  int t;
  cin >> t;
  FOR(_t,1,t){
  	cout << "Case #" << _t << ": ";
 	ll n;cin >> n;
 	cout << f(n) << "\n";  
  }
  return 0;
}