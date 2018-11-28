#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

typedef long long ll;
map<pair<ll,ll>,ll> memo;
ll n, k;

ll c(ll n, ll x) {
	if (n < x + 1) return 0;
	if (memo.find(make_pair(n, x)) == memo.end())
		memo[make_pair(n, x)] = 1 + c((n - 1) / 2, x) + c(n / 2, x);
	return memo[make_pair(n, x)];
}

int main() {
	int t;
	cin >> t; for (int u = 0; u < t; u++) {
		cin >> n >> k;
		ll lo = 0, hi = n, mid;
		while (lo+1 < hi) {
			mid = (lo + hi) / 2;
			if (c(n, mid) < k) hi = mid; else lo = mid;
//			cout << mid << "->" << c(n, mid) << endl;
		}
		cout << "Case #" << (u + 1) << ": " << ((lo + 1) / 2) << " " << ((lo) / 2) << endl;
	}
	return 0;
}
