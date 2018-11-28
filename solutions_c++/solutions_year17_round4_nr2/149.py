#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <map>

int solve(int testcase) {
	int n, c, m;
	std::cin >> n >> c >> m;

	std::vector<int> dup(c);
	std::vector<int> freq(n);
	std::vector<int> p(m), b(m);
	for (int i = 0; i < m; i++) {
		std::cin >> p[i] >> b[i];
		p[i]--;
		b[i]--;
		dup[b[i]]++;
		freq[p[i]]++;
	}

	int ok = 1000;
	int ng = *max_element(dup.begin(), dup.end()) - 1;

	int cnt;
	auto f = [&](int mid) {
		int left = 0;
		cnt = 0;
		for (int i = n - 1; i >= 0; i--) {
			int use = std::min(mid, freq[i]);
			int use2 = std::min(left, mid - use);
			left -= use2;
			cnt += use2;
			left += freq[i] - use;
		}
		if (left > 0) {
			ng = mid;
		} else {
			ok = mid;
		}
	};
	while (ok - ng > 1) {
		int mid = (ok + ng) / 2;
		f(mid);
	}
	f(ok);
	printf("Case #%d: %d %d\n", testcase, ok, cnt);
}

int main() {
	int T;
	std::cin >> T;
	for (int i = 0; i < T; i++) {
		solve(i + 1);
	}
}
