#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

#define REP(i,b) for (int i = 0; i < (b); i++)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

typedef long long ll;

int main() {
	int tcs;
	scanf("%d", &tcs);
	FOR(tc, 1, tcs) {
		printf("Case #%d: ", tc);
		ll n, k;
		scanf("%lld%lld", &n, &k);
		map<ll, ll> m;
		m[n] = 1LL;
		ll pos = 0;
		while (pos < k) {
			auto it = m.end();
			it--;
			ll s1 = (it->first - 1) / 2, s2 = it->first / 2;
			ll count = it->second;
			m[s1] += count;
			m[s2] += count;
			m.erase(it);
			pos += count;
			if (pos >= k) {
				printf("%lld %lld\n", s2, s1);
				break;
			}
		}
	}
	return 0;
}
