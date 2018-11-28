#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<int, ll> pil;
typedef pair<ll, int> pli;
typedef vector<int> VI;
#define pb push_back
#define xx first
#define yy second
#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define FORB(i,a,b) for(int i=int(b)-1;i>=int(a);i--)
	
int main() {
	int T; cin >> T;
	FOR(t,1,T+1) {
		ll n, k, a, b;
		cin >> n >> k;
		pll odd, even;
		if (n&1) odd={n,1L},even={n+1,0L};
		else even = {n,1L},odd={n+1,0L};
		while (1) {
			if (odd.xx > even.xx) {
				if (k <= odd.yy) {
					a = b = odd.xx/2;
					break;
				} 
				k -= odd.yy;
				if (k <= even.yy) {
					a = (even.xx-1)/2, b = even.xx/2;
					break;
				}
				k -= even.yy;
			} else {
				if (k <= even.yy) {
					a = (even.xx-1)/2, b = even.xx/2;
					break;
				}
				k -= even.yy;
				if (k <= odd.yy) {
					a = b = odd.xx/2;
					break;
				}
				k -= odd.yy;
			}
			pll ot={0,0}, et={0,0};
			ll e1, e2, o1;
			e1 = even.xx/2; e2 = e1-1; o1 = odd.xx/2;
			
			if (e1&1) ot.xx=e1, et.xx=e2;
			else ot.xx=e2, et.xx=e1;
			
			ot.yy += even.yy, et.yy += even.yy;
			if (o1&1) ot.yy += 2*odd.yy;
			else et.yy += 2*odd.yy;
			
			odd = ot, even = et;
		}
		cout << "Case #" << t << ": " << b << ' ' << a << endl;
	}
	return 0;
}