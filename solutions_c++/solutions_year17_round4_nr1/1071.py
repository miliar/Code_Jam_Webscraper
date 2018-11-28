#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef pair<ll,ll> pll;
typedef vector<bool> vb;
const ll oo = 0x3f3f3f3f3f3f3f3f;
const double eps = 1e-9;
#define sz(c) ll((c).size())
#define all(c) begin(c), end(c)
#define FOR(i,a,b) for (ll i = (a); i < (b); i++)
#define FORD(i,a,b) for (ll i = (b)-1; i >= (a); i--)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define xx first
#define yy second
#define has(c,i) ((c).find(i) != end(c))
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

ll dp[4][110][110][110];

int main() {
	ll TC; cin >> TC;
	FOR(tc,1,TC+1) {
		ll n, p; cin >> n >> p;
		vl a(n);
		FOR(i,0,n) {
			cin >> a[i];
			a[i] %= p;
		}
		vl cnt(4);
		FOR(i,0,n) cnt[a[i]]++;
		
		memset(dp,0,sizeof dp);
		FOR(x1,0,cnt[1]+1) FOR(x2,0,cnt[2]+1) FOR(x3,0,cnt[3]+1) FOR(k,0,p) {
			dp[k][x1][x2][x3] = 0;
			if (x1) dp[k][x1][x2][x3] = max(dp[k][x1][x2][x3], !k + dp[(k+1)%p][x1-1][x2][x3]);
			if (x2) dp[k][x1][x2][x3] = max(dp[k][x1][x2][x3], !k + dp[(k+2)%p][x1][x2-1][x3]);
			if (x3) dp[k][x1][x2][x3] = max(dp[k][x1][x2][x3], !k + dp[(k+3)%p][x1][x2][x3-1]);
		}

		cout << "Case #" << tc << ": " << cnt[0] + dp[0][cnt[1]][cnt[2]][cnt[3]] << endl;
	}


}

