#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std;
int k[1100], s[1100];
int d, n;
inline bool check(long double speed) {
	for (int i = 1; i <= n; i++) {
		if (speed <= 1.0 * s[i]) {
			continue;
		}
		long double trf = 1.0 * (d - k[i]) / s[i];
		long double tti = 1.0 * (k[i]) / (speed - s[i]);
		if (trf > tti) {
			return false;
		}
	}
	return true;
}
inline void solve() {
	scanf("%d%d", &d, &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d%d", &k[i], &s[i]);
	}
	long double l = 0, r = 1e18;
	for (int it = 1; it <= 2000; it++) {
		long double mid = (l + r) / 2;
		if (check(mid)) {
			l = mid;
		} else {
			r = mid;
		}
	}
	cout << setprecision(10) << fixed << l << '\n';
}
int main() {
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		printf("Case #%d: ", test);
		solve();
	}
}
