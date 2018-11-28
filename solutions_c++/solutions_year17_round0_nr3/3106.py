#include <bits/stdc++.h>

using namespace std;

#define INF 0x3f3f3f3f
#define NSYNC ios::sync_with_stdio(false)
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define FOR0(i,b) for(int i=0; i<(b); ++i)
#define DBG(x) cout << #x << " == " << x << endl
#define DBGV(v) for(int x : v) cout << x << " "; cout << endl
#define DBGP(x,y) cout << "(" << x << ", " << y << ")" << endl
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define sz(a) (int)((a).size())
#define all(c) (c).begin(),(c).end()
#define R(x) scanf(" %d",&(x))
#define RR(x,y) scanf(" %d %d",&(x), &(y))
#define CLR(v) memset(v, 0, sizeof(v))
#define SET(v) memset(v, -1, sizeof(v))

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

ll n,k;

unordered_set<ll> migue;
void genmigue(ll x) {
	if (migue.count(x)) return;
	migue.insert(x);
	if (x>1) {
		ll aux = x-1;
		genmigue(aux/2);
		if (aux&1) genmigue(aux/2+1);
	}
}

unordered_map<ll, ll> dp;
ll qtd(ll x) {
	if (x<=0 || x>n || !migue.count(x)) return 0;
	auto it = dp.find(x);
	if (it != dp.end()) return it->second;
	ll ans =  qtd(2*x) + 2*qtd(2*x+1) + qtd(2*x+2);
	return dp[x] = ans;
}

map<ll, ll> vals;
void gen(ll x) {
	if (vals.count(x)) return;
	vals[x] = qtd(x);

	if (x>1) {
		ll aux = x-1;
		gen(aux/2);
		if (aux&1) gen(aux/2+1);
	}
}

pair<ll, ll> solve() {
	vals.clear();
	migue.clear();
	dp.clear();
	dp[n] = 1;
	genmigue(n);
	gen(n);
	ll tot = 0;
	for (auto p = vals.rbegin(); p != vals.rend(); ++p) {
		tot += p->second;
		if (tot >= k) {
			ll sz = p->first;
			ll l = (sz-1)/2;
			ll r = (sz-1)/2 + (sz&1 ? 0 : 1);
			return {max(l,r), min(l,r)};
		}
	}
}

int main() {
	NSYNC;
	int t;
	cin >> t;
	FOR0(i,t) {
		cin >> n >> k;
		auto ans = solve();
		cout << "Case #" << i+1 << ": " << ans.first << " " << ans.second << endl;
	}
	return 0;
}
