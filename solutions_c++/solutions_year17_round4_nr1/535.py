#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T; cin >> T;
	for (int ks = 1; ks <= T; ++ks) {
		int n, p, c[4]; cin >> n >> p;
		memset(c, 0, sizeof c);

		for (int i = 0; i < n; ++i) {
			int k; cin >> k;
			++c[k % p];
		}
		int ans = 0;
		if (p == 2) {
			ans = c[0] + (c[1] + 1) / 2;
		}
		if (p == 3) {
			int t1 = min(c[1], c[2]);
			int t2 = c[1] < c[2] ? (c[2] - c[1] + 2) / 3 : (c[1] - c[2] + 2) / 3;
			ans = c[0] + t1 + t2;
		}
		if (p == 4) {
			int t1 = min(c[1], c[3]);
			int t2 = c[2] / 2, t3, t4 = 0;
			c[2] = c[2] % 2;
			if (c[1] < c[3]) {
				c[3] -= c[1];
				t3 = c[3] / 4;
				c[3] %= 4;
				if (c[2] == 0) {
					if (c[3] != 0)
						t4 = 1;
				} else {
					if (c[3] == 3)
						t4 = 1;
				}
			} else {
				c[1] -= c[3];
				t3 = c[1] / 4;
				c[1] %= 4;
				if (c[2] == 0) {
					if (c[1] != 0)
						t4 = 1;
				} else {
					if (c[1] == 3)
						t4 = 1;
				}
			}
			ans = c[0] + t1 + t2 + t3 + c[2] + t4;
		}
		cout << "Case #" << ks << ": " << ans << endl;
	}

	return 0;
}

