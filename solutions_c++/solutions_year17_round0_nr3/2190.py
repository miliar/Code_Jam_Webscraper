#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i >= (b); --i)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define fi first
#define se second

void test() {
	ll n,k;
	scanf("%lld%lld", &n, &k);
	map<ll,ll> M;
	M[n] = 1;
	while (true) {
		ll val = M.rbegin() -> fi, cnt = M.rbegin() -> se;
		//printf("%lld %lld -> %lld %lld\n", val, cnt, val/2, (val-1)/2);
		if (cnt >= k) {
			printf("%lld %lld\n", val/2, (val-1)/2);
			return;
		}
		k -= cnt;
		M.erase(M.find(val));
		M[val/2] += cnt;
		M[(val-1)/2] += cnt;
	}
}

int main() {
	int ttn;
	scanf("%d", &ttn);
	FORI(i,ttn) {
		printf("Case #%d: ", i);
		test();
	}
	return 0;
}
