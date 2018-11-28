#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for(int i=(a);i<(b);i++)
#define MOD 1000000007
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef long double ld;
#define PI ((ld)acos(-1.))
#define asdf(x...) fprintf(stderr, x)

int T;
ll N, K, ansa, ansb;

map<ll, ll> m;
void f (ll i) {
	if (m.count(-i) || i <= 0ll) return;
	m[-i] = 0ll;
	if (i&1) f(i/2);
	else f(i/2), f(i/2 - 1);
}

int main () {
	scanf("%d", &T);
	fo(t, 1, T+1) {
		//REMEMBER CLEAR DS
		m.clear();
		ansa = -1, ansb = -1;
		//REMEMBER CLEAR DS
		asdf("Doing case %d... ", t);

		scanf("%lld %lld", &N, &K);
		f(N), m[-N] = 1ll;
		for (auto i : m) {
			ll v = -i.first, cnt = i.second;

			ll a = v/2ll, b = (v-1)/2ll;

			//printf("sz %lld, num %lld (%lld %lld)\n", v, cnt, a, b);

			K -= cnt;
			if (K <= 0) {
				ansa = a, ansb = b;
				break;
			}

			if (a) m[-a] += cnt;
			if (b) m[-b] += cnt;
		}

		printf("Case #%d: %lld %lld\n", t, ansa, ansb);
		asdf("%lld %lld\n", ansa, ansb);
	}
	return 0;
}
