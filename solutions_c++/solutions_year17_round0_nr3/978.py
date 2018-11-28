#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define rrep(i, a, b) for(int i = (a) - 1; i >= int(b); --i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define all(v) (v).begin(), (v).end()
#define what_is(x) cerr << #x << " is " << x << endl;

typedef double fl;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

ll minDiff;
map<ll, ll> cache;

ll steps(ll N){
	if(cache.count(N))
		return cache[N];
	ll ans=0;
	if(N >= minDiff){
		ans = 1 + steps(N/2) + steps((N+1)/2);
	}
	cache[N]=ans;
	return ans;
}

void solve(){
	ll N, K;
	scanf("%lld%lld", &N, &K);
	ll lo=2, hi=N+2;
	while(hi-lo > 1){
		cache.clear();
		minDiff = (lo+hi)/2;
		if(steps(N+1) >= K){
			lo = minDiff;
		}
		else{
			hi = minDiff;
		}
	}
	printf("%lld %lld\n", (lo-1)/2, (lo-2)/2);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int i=1; i <= T; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}
