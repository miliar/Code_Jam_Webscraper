#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;

#define SZ(a) (int)(a).size()
typedef long long ll;

int itc;

void solve() {
	ll n, k;
	cin >> n >> k;
	map<ll, ll> cnt = {{n, 1}};
	ll ans;
	while (true) {
		auto it = prev(end(cnt));
		ll x = it->first;
		ll y = it->second;
		if (k <= y) {
			ans = x;
			break;
		}
		k -= y;
		cnt.erase(it);
		cnt[(x-1)/2] += y;
		cnt[x/2] += y;
	}
	printf("%lld %lld\n", ans/2, (ans-1)/2);
}

int main() {
	cin.sync_with_stdio(false);
	int ntc;
	cin >> ntc;
	for (itc = 1; itc <= ntc; itc++) {
		printf("Case #%d: ", itc);
		solve();
	}
}
