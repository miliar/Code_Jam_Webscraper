#include <bits/stdc++.h>
using namespace std;

#define int long long

map<int, int> mp;

int calc(int n) {
	if (n <= 1) {
		return 0;
	}
	if (mp.count(n)) {
		return mp[n];
	}
	return mp[n] = calc(n / 2) + calc((n + 1) / 2) + 1;
}

pair<int, int> go(int n, int k) {
	if (k == 1) {
		return {n / 2, (n - 1) / 2};
	}
	int val = calc(n);
	if (val < k) {
		return {0, 0};
	}
	--k;
	int l = (n - 1) / 2;
	int r = n / 2;
	if (l < r) {
		if (k % 2 == 0) {
			return go(l, k / 2);
		} 
		return go(r, (k + 1) / 2);
	} else {
		if (k % 2 == 0) {
			return go(r, k / 2); 
		} 
		return go(l, (k + 1) / 2);
	}
}

void solve() {
	int n, k;
	cin >> n >> k;
	auto result = go(n, k);
	cout << result.first << ' ' << result.second << '\n';
}

main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}