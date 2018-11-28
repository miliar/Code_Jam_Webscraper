#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;

typedef long long ll;
map<ll, ll> s;
typedef map<ll, ll>::iterator iter;

int main() {
	int t;
	scanf("%d", &t);
	for (int id = 1; id <= t; ++id) {
		ll n, k;
		scanf("%I64d%I64d", &n, &k);
		s.clear();
		s[n] = 1;
		
		while (k > 1) {
			iter i = --s.end();
			ll num = min(i->second, k - 1);
			ll llen = (i->first - 1) / 2;
			ll rlen = (i->first - 1) - llen;
			if (llen) s[llen] += num;
			if (rlen) s[rlen] += num;
			if (!(i->second -= num)) {
				s.erase(i);
			}
			k -= num;
		}
		
		iter i = --s.end();
		ll llen = (i->first - 1) / 2;
		ll rlen = (i->first - 1) - llen;
		printf("Case #%d: %I64d %I64d\n", id, rlen, llen);
	}
}