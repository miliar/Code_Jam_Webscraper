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
double EPS = 1e-8;

int main(){
	int mCase;
	scanf("%d", &mCase);
	
	for(int Case = 1; Case <= mCase; Case++){
		int d, n;
		scanf("%d %d", &d, &n);
		vi k(n), s(n);
		rep(i, n) scanf("%d %d", &k[i], &s[i]);

		double ans = 0;
		double l = 0, r = 1e18;
		rep(_, 1024) {
			double m = (l + r) / 2.0;
			bool f = true;
			rep(i, n) {
				if(m - s[i] <= 0.0) continue;
				double t = k[i]/(m-s[i]);
				if(m * t < d) f = false;
			}
			if(f) l = m;
			else r = m;
		}
		ans = l;
		printf("Case #%d: %lf\n", Case, ans);
	}
}