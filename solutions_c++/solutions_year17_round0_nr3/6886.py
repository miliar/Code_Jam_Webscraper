#include <iostream>
#include <set>

#define INF 2000000000000000000

using namespace std;

int main() {
	int t;
	cin >> t;

	for (int c = 1; c <= t; c++) {
		long long n, k;
		cin >> n >> k;

		set<long long> s;
		s.emplace(0);
		s.emplace(n + 1);

		for (int i = 0; i < k; i++) {
			pair<pair<long long, long long>, long long> mx = {{-INF, -INF}, 0};
			for (long long j = 1; j <= n; j++)
				if (s.find(j) == s.end()) {
					auto it_r = s.lower_bound(j);
					auto it_l = prev(it_r);

					long long ls = j - *it_l - 1;
					long long rs = *it_r - j - 1;

					if (min(ls, rs) > min(mx.first.first, mx.first.second))
						mx = {{ls, rs}, j};
					else if (min(ls, rs) == min(mx.first.first, mx.first.second))
						if (max(ls, rs) > max(mx.first.first, mx.first.second))
							mx = {{ls, rs}, j};
				}

			if (i == k - 1)
				cout << "Case #" << c << ": " << max(mx.first.first, mx.first.second) << ' ' << min(mx.first.first, mx.first.second) << endl;

			s.emplace(mx.second);
		}
	}

	return 0;
}
