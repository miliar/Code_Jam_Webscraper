#include <iostream>
#include <queue>
#include <functional>
#include <algorithm>
#include <unordered_map>
using namespace std;

typedef long long ll;
pair<ll, ll> solve(ll n, ll k) {
	pair<ll, ll> ret;
	priority_queue<ll> pq; // size
	unordered_map<ll, ll> size_cnt;
	pq.push(n);
	size_cnt[n] = 1;
	while(k) {
		ll pq_top = pq.top();
		pq.pop();
		ll half_size = pq_top / 2;
		ll asign_cnt = min(k, size_cnt[pq_top]);
		k -= asign_cnt;
		if (pq_top % 2) {
			if (size_cnt.count(half_size) == 0) {
				pq.push(half_size);
			}
			size_cnt[half_size] += asign_cnt * 2;
			if (k == 0) {
				ret = { half_size, half_size };
			}
		}
		else {
			if (size_cnt.count(half_size) == 0) {
				pq.push(half_size);
			}
			size_cnt[half_size] += asign_cnt;
			if (size_cnt.count(half_size - 1) == 0) {
				pq.push(half_size - 1);
			}
			size_cnt[half_size - 1] += asign_cnt;
			if (k == 0) {
				ret = { half_size, half_size - 1 };
			}
		}
	}
	return ret;
}

int main() {
	ll t, n, k;
	cin >> t;
	for (ll tloop = 1; tloop <= t; ++tloop) {
		cin >> n >> k;
		cerr << n << ' ' << k << endl;
		auto ans = solve(n, k);
		cout << "Case #" << tloop << ": " << ans.first << " " << ans.second << endl;
	}
}