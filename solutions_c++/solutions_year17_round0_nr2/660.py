#include <bits/stdc++.h>
  
using namespace std;
  
#define rep(i,n) REP(i,0,n)
#define REP(i,s,e) for(int i=(s); i<(int)(e); i++)
#define pb push_back
#define all(r) r.begin(),r.end()
#define rall(r) r.rbegin(),r.rend()
#define fi first
#define se second
  
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
 
const int INF = 1e9;
const ll MOD = 1e9 + 7;
const ll LINF = 1e18;
double EPS = 1e-8;


int main(){
	int mCase;
	scanf("%d", &mCase);
	set<ll> st;
	set<ll> tmp[2];
	tmp[0].insert(0);
	for(int i = 0; i < 18; i++) {
		int nxt = (i+1)&1;
		tmp[nxt].clear();
		for(auto& p : tmp[i&1]) {
			for(int i = p%10; i<= 9; i++) {
				ll v = p * 10 + i;
				if(v != 0 && v < LINF) tmp[nxt].insert(v);
				st.insert(-v);
			}
		}
	}
	
	for(int Case = 1; Case <= mCase; Case++){
		ll n;
		scanf("%ld", &n);
		ll ans = 1LL;
		//for(auto&p : st) cout << p << endl;
		ans = -(*st.lower_bound(-n));
		printf("Case #%d: %ld\n", Case, ans);
	}
}