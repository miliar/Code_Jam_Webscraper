#include <bits/stdc++.h>
using namespace std;


void solve(long long n, long long k) {
		long long p = 1, b1, b2, sum;
		for (p = 0; p < 64; p++) {
			b1 = (1LL<<p) - 1;
			b2 = (1LL<<(p + 1)) - 1;
			if (k > b1 && k <= b2) {
				break;
			}
		}

		sum = n - b1;
		b2 = 1LL<<p;

		long long div = sum / b2, add = sum % b2;
		if (k - (b1) <= add) {
			div++;
		}

		long long mind, maxd;
		if (div & 1) {
			mind = div>>1;
			maxd = div>>1;
		} else {
			mind = (div>>1) - 1;
			maxd = div>>1;
		}

		cout << maxd << ' ' << mind << "\n";
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int t;
	cin >> t;
	for (int id = 1; id <= t; id++) {
		long long n, k;
		cin >> n >> k;
		cout << "Case #" << id << ": ";
		solve(n, k);
	}

	return 0;
}