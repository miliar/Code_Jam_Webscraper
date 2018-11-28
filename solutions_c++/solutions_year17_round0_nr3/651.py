#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>

using namespace std;
using PLL = pair<long long, long long>;

void show(map<long long, long long> &m) {
	cout << string(20, '-') << endl;
	for (auto p : m) {
		printf("%10lld %10lld\n", p.first, p.second);
	}
}

PLL solve(long long n, long long k) {
	long long l, r;

	map<long long, long long> vacants;
	vacants[n] = 1;

	while (k > 0) {
		// show(vacants);
		auto it = vacants.end();
		it--;
		auto len = it->first;
		auto n_vacants = it->second;

		len--;
		l = len / 2;
		r = len - l;

		auto n_done = min(n_vacants, k);
		vacants[l] += n_done;
		vacants[r] += n_done;
		k -= n_done;
		it->second -= n_done;

		if (it->second == 0) {
			vacants.erase(it);
		}
	}
	// show(vacants);

	return make_pair(r, l);
}

int main() {
	int t;
	long long n, k;

	cin >> t;
	vector<PLL> ans(t);

	for (int i = 0; i < t; i++) {
		cin >> n >> k;
		ans[i] = solve(n, k);
	}

	for (int i = 0; i < t; i++) {
		printf("Case #%d: %lld %lld\n", i + 1, ans[i].first, ans[i].second);
	}
	return 0;
}
