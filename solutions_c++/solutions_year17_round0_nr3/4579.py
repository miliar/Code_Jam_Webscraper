#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define pb emplace_back

using namespace std;

typedef long long ll;

void solve() {
	ll n, k;
	cin >> n >> k;
	map<ll, ll> cnt;
	cnt[n] = 1;
	while (true) {
		auto it = --cnt.end();
		ll sz = it->first, q = it->second;
		ll l = (sz - 1) / 2, r = sz - 1 - (sz - 1) / 2;
		if (q >= k) {
			cout << r << " " << l << "\n";
			return;
		}
		k -= q;
		cnt.erase(it);
		cnt[l] += q;
		cnt[r] += q;
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
  return 0;
}
