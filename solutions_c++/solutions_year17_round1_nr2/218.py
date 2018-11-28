#include <bits/stdc++.h>

using namespace std;

namespace Solve {

	typedef pair<long, long> pll;

	const double EPS = 1e-7;

	long unit[64];
	long cnt[64][64];
	long ptr[64];

	inline long getMax(const long &amount, const long &unit) {
		return (long) floor(amount * 1.0L / unit / 0.9L + EPS);
	}

	inline long getMin(const long &amount, const long &unit) {
		return (long) (ceil(amount * 1.0L / unit / 1.1L - EPS) + EPS);
	}

	void main() {
		ios::sync_with_stdio(false);
		register long i, j;
		long T;
		cin >> T;
		for (long t = 1; t <= T; ++ t) {
			long n, p;
			cin >> n >> p;
			for (i = 0; i < n; ++ i) {
				cin >> unit[i];
			}
			for (i = 0; i < n; ++ i) {
				for (j = 0; j < p; ++ j) {
					cin >> cnt[i][j];
				}
				sort(cnt[i], cnt[i] + p);
			}
			memset(ptr, 0, sizeof ptr);
			long now = 1;
			for (i = 0; i < n; ++ i) {
				long cur = getMin(cnt[i][0], unit[i]);
				if (now < cur) now = cur;
			}
			long ans = 0;
			for (;;) {
				bool valid = true;
				for (i = 0; i < n; ++ i) {
					long mi = getMin(cnt[i][ptr[i]], unit[i]), mx = getMax(cnt[i][ptr[i]], unit[i]);
					if (mi > now) {
						now = mi;
						valid = false;
						break;
					}
					if (mx < now || mx < mi) {
						++ ptr[i];
						valid = false;
						if (ptr[i] >= p) goto print;
						break;
					}
				}
				if (valid) {
					++ ans;
					for (i = 0; i < n; ++ i) {
						if ((++ ptr[i]) >= p) goto print;
					}
				}
			}
print:
			cout << "Case #" << t << ": " << ans << endl;
		}
	}
}

int main(void) {
	Solve::main();
	return 0;
}
