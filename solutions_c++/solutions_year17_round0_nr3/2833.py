#include <bits/stdc++.h>

#define ll long long

using namespace std;

void solve(int id) {
	ll n, k;
	cin >> n >> k;

	map<ll, ll> a;
	a[n] = 1;

	while (true) {
		auto it = --a.end();
		if (it->second < k) {
			if (it->first % 2 == 1) {
				a[it->first / 2] += it->second * 2;
			} else {
				a[it->first / 2] += it->second;
				a[it->first / 2 - 1] += it->second;
			}
			k -= it->second;
			a.erase(it);
		} else {
			break;
		}
	}

	auto ans = a.rbegin();
	pair<ll, ll> res = {0, 0};
	if (ans->first % 2 == 1) {
		res = {ans->first / 2, ans->first / 2};
	} else {
		res = {ans->first / 2, ans->first / 2 - 1};
	}

	printf("Case #%d: ", id);
	cout << res.first << ' ' << res.second << '\n';
}

int main() {
	int t;
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		solve(i);
	}

	return 0;
}

// 0....0
// 0.0..0
// 0.00.0
// 0000.0

// 0.....0
// 0,,0,,0
// 00,0,,0
// 00,00,0

// 0......0
// 0..0...0