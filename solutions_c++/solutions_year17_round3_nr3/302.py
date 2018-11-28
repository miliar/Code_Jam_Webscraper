#include <iostream>
using namespace std;
using DB = double;

const int MAXN = 55;

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int T; cin >> T;
	for (int kase = 1; kase <= T; ++kase) {
		int n, k; cin >> n >> k;
		DB u, p[MAXN];
		cin >> u;
		for (int i = 0; i < n; ++i)
			cin >> p[i];
		DB l = 0.0, r = 1;
		DB sum = 0;
		do {
			DB m = (l + r) / 2;
			sum = 0;
			for (int i = 0; i < n; ++i)
				if (m > p[i]) sum += m - p[i];
			if (sum > u)
				r = m;
			else l = m;
		} while ((sum - u) > 1e-10 || (r - l) > 1e-11);
		DB ans = 1;
		for (int i = 0; i < n; ++i)
			if (p[i] > l)
				ans *= p[i];
			else ans *= l;
		printf("Case #%d: %.10lf\n", kase, ans);
	}

	return 0;
}
