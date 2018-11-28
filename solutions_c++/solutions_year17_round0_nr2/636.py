#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

long long solve(long long n) {
	while (1) {
		auto tmp = n;
		int n_div = 0;
		int prev = 10;

		bool ok = true;
		while (tmp > 0) {
			int now = tmp % 10;

			if (now > prev) {
				for (int i = 0; i < n_div; i++) {
					tmp = tmp * 10;
				}
				tmp--;
				n = tmp;
				ok = false;
				break;
			}

			tmp /= 10;
			n_div++;
			prev = now;
		}

		if (ok) {
			break;
		}
	}

	return n;
}

int main() {
	int t;
	long long n;

	cin >> t;
	vector<long long> ans(t, 0);

	for (int i = 0; i < t; i++) {
		cin >> n;
		ans[i] = solve(n);
	}

	for (int i = 0; i < t; i++) {
		printf("Case #%d: %lld\n", i + 1, ans[i]);
	}
	return 0;
}
