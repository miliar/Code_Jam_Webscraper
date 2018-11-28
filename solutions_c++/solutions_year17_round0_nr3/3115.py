#include <bits/stdc++.h>
using namespace std;
#define sim template < class c
#define ris return * this
#define dor > debug & operator <<
#define eni(x) sim > typename \
  enable_if<sizeof dud<c>(0) x 1, debug&>::type operator<<(c i) {
sim > struct rge {c b, e; };
sim > rge<c> range(c i, c j) { return rge<c>{i, j}; }
sim > auto dud(c* x) -> decltype(cerr << *x, 0);
sim > char dud(...);
struct debug {
#ifdef LOCAL
~debug() { cerr << endl; }
eni(!=) cerr << boolalpha << i; ris; }
eni(==) ris << range(begin(i), end(i)); }
sim, class b dor(pair < b, c > d) {
  ris << "(" << d.first << ", " << d.second << ")";
}
sim dor(rge<c> d) {
  *this << "[";
  for (auto it = d.b; it != d.e; ++it)
    *this << ", " + 2 * (it == d.b) << *it;
  ris << "]";
}
#else
sim dor(const c&) { ris; }
#endif
};
#define imie(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "

typedef long long ll;

void test_case() {
	map<ll, ll> mapka;
	ll n, k;
	scanf("%lld%lld", &n, &k);
	mapka[n] = 1;
	while(true) {
		debug() << mapka;
		assert(!mapka.empty());
		auto it = mapka.end();
		--it;
		ll len = it -> first;
		assert(len >= 1);
		ll times = it -> second;
		mapka.erase(it);
		if(times >= k) {
			printf("%lld %lld\n", (len + 0) / 2, (len-1) / 2);
			return;
		}
		k -= times;
		mapka[len/2] += times;
		mapka[(len-1)/2] += times;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for(int nr = 1; nr <= T; ++nr) {
		printf("Case #%d: ", nr);
		test_case();
	}
}
