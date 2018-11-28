#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)n; i++)
#define vec vector

int main(void)
{
	int T;
	cin >> T;
	rep(t, T) {
		cout << "Case #" << t + 1 << ": ";
		int n, p;
		cin >>  n >> p;
		vec<int> g(n);
		rep(i, n) cin >> g[i];
		if (p == 2) {
			int even = 0;
			rep(i, n) if (g[i] % 2 == 0) even++;
			cout << even + (n - even + 1) / 2 << endl;
		} else if (p == 3) {
			vec<int> c(3, 0);
			rep(i, n) c[g[i] % 3]++;
			if (c[1] < c[2]) cout << c[0] + c[1] + (c[2] - c[1] + 2) / 3 << endl;
			else cout << c[0] + c[2] + (c[1] - c[2] + 2) / 3 << endl;
		} else {
			vec<int> c(4, 0);
			rep(i, n) c[g[i] % 4]++;
			int ans = c[0] + c[2] / 2 + min(c[1], c[3]);
			int keep = c[1] - c[3];
			if (keep < 0)  keep = - keep;
			if (c[2] % 2 == 0) ans += (keep + 3) / 4;
			else ans += 1 + (keep + 1) / 4;
			cout << ans << endl;
		}
	}

	return 0;
}

