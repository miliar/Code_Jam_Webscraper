#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
#include <queue>

using namespace std;
using PLL = pair<long long, long long>;

double solve() {
	int n, k;
	cin >> n >> k;

	vector<long long> r(n), h(n);

	priority_queue<PLL> que;
	for (int i = 0; i < n; i++) {
		cin >> r[i] >> h[i];
		que.push(make_pair(2*r[i]*h[i], i));
	}

	vector<int> cake_idx;
	long long max_r = -1;

	while (cake_idx.size() < k) {
		auto p = que.top();
		que.pop();
		cake_idx.emplace_back(p.second);
		if (max_r < r[p.second]) {
			max_r = r[p.second];
		}
	}

	long long area1 = 0;
	for (int idx : cake_idx) {
		area1 += 2LL * r[idx] * h[idx];
// printf("%10lld %10lld\n", r[idx], h[idx]);
	}
	area1 += max_r * max_r;
	int min_area_idx = cake_idx.back();
	long long min_yoko_area = 2LL * r[min_area_idx] * h[min_area_idx];

	long long max_area = area1;
// printf("---\n");
	while (!que.empty()) {
		auto p = que.top();
		que.pop();
		long long rr = r[p.second];
		if (rr < max_r) {
			continue;
		}
// printf("%10lld %10lld\n", r[p.second], h[p.second]);
		long long add = rr * rr + 2LL * rr * h[p.second] - (max_r * max_r);
		// printf("add %lld, r*r %lld, 2rh %lld, %lld \n",
			// add, rr * rr, 2LL * rr * h[p.second], max_r*max_r);
		max_area = max(max_area, area1 - min_yoko_area + add);
	}

	return 1.0 * M_PI * max_area;
}

double solve_small() {
	int n, k;
	cin >> n >> k;

	vector<long long> r(n), h(n);
	for (int i = 0; i < n; i++) {
		cin >> r[i] >> h[i];
	}

	long long max_area = 0;
	for (int i = 0; i < (1 << n); i++) {
		if (__builtin_popcount(i) != k) {
			continue;
		}

		long long area = 0;
		long long max_r = 0;
		for (int j = 0; j < n; j++) {
			if ((i >> j) & 1) {
				max_r = max(max_r, r[j]);
				area += 2LL * r[j] * h[j];
			}
		}
		area += max_r * max_r;
		max_area = max(max_area, area);
	}

	return 1.0 * M_PI * max_area;
}


int main() {

	int t;

	cin >> t;
	vector<double> ans(t, 0);

	for (int i = 0; i < t; i++) {
		// ans[i] = solve_small();
		ans[i] = solve();
	}

	for (int i = 0; i < t; i++) {
		printf("Case #%d: %.9f\n", i + 1, ans[i]);
	}
	return 0;
}
