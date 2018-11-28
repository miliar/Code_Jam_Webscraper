#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define eps 1e-9
#define all(a)   a.begin(),a.end()
#define mp make_pair
#define F first
#define S second
#define pb push_back
#define sz size()
#define rd(inp) scanf("%lld",&inp)
#define rd2(inp1, inp2) scanf("%lld %lld",&inp1, &inp2)
#define rl(inp) scanf("%d",&inp)
#define pf(out) printf("%lld\n", out);

const long long linf = 1e18+5;
const int mod = (int) 1e9 + 7;
const int inf = 1e9;

ll read(){
	bool minus = false;
	ll result = 0;
	char ch;
	ch = getchar();
	while (true) {
		if (ch == '-') break;
		if (ch >= '0' && ch <= '9') break;
		ch = getchar();
	}
	if (ch == '-') minus = true; else result = ch-'0';
	while (true) {
		ch = getchar();
		if (ch < '0' || ch > '9') break;
		result = result*10 + (ch - '0');
	}
	if (minus){
		return -result;
	}
	else{
		return result;
	}
}

ll fpow(ll base,ll power){
	ll result = 1;
	while (power > 0){
		if (power%2 == 1) result=(result*base);
  		base = (base*base);
  		power /= 2;
  	}
	return result;
}

bool vis[1111];
pair<ll,ll> st[1111];
ll a[1111], ma[1111];

void solve(){
	ll n, k;
	cin >> n >> k;
	ll i, j, here;
	memset(vis, 0, sizeof(vis));
	vis[0] = true;
	vis[n+1] = true;
	for ( i = 0 ; i < k ; i ++ ){
		ll lf = 0;
		for ( j = 1 ; j <= n ; j ++ ){
			if ( vis[j] == true ){
				lf = j;
			}
			st[j].F = j - lf;
			// cout << st[j].F << " lf \n";
		}
		// cout << " -- \n";
		ll rg = n + 1;
		for ( j = n ; j >= 1 ; j -- ){
			if ( vis[j] == true ){
				rg = j;
			}
			st[j].S = rg - j;
			// cout << st[j].S << " rg \n";
		}
		// cout << " -- \n";
		ll ans = -1;
		for ( j = 1 ; j <= n ; j ++ ){
			if ( vis[j] == false ){
				a[j] = min(st[j].F, st[j].S);
				ma[j] = max(st[j].F, st[j].S);
				ans = max(a[j], ans);
			}
		}
		// cout << " ans = " << ans << "\n";
		here = 0;
		ll mmax = -1;
		for ( j = 1 ; j <= n ; j ++ ){
			if ( vis[j] == false ){
				if ( a[j] == ans ){
					mmax = max(mmax, ma[j]);
				}
			}
		}
		for ( j = 1 ; j <= n ; j ++ ) if ( vis[j] == false ){
			if ( a[j] == ans && ma[j] == mmax ){
				vis[j] = true;
				here = j;
				break;
			}
		}
		// cout << " here = " << here << "\n";
	}
	printf("%lld %lld\n", st[here].S - 1, st[here].F - 1);
}

int main(){
	int t, i = 1;
	cin >> t;
	while( t-- ){
		printf("Case #%d: ", i++);
		solve();
	}
	return 0;
}