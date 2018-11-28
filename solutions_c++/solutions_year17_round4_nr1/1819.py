#include <bits/stdc++.h>
using namespace::std;

int main() {
	int t, caseno = 0;
	cin >> t;
	while (t--) {
		caseno++;
		int n, p, ans;
		cin >> n >> p;
		int a[4] = {0};
		for (int i = 0; i < n; i++) {
			int temp;
			cin >> temp;
			a[temp % p]++;
		}
		ans = a[0];
		if (p == 2) {
			ans += (a[1] + 1) / 2;
		} else if (p == 3) {
			int mn = min(a[1], a[2]);
			ans += (2 * mn + 1) / 2;
			a[1] -= mn;
			a[2] -= mn;
			mn = max(a[1], a[2]);
			if (mn > 0) {
				ans += (mn - 1) / 3 + 1;
			}
		} else {
			int mn = min(a[1], a[3]);
			ans += (2 * mn + 1) / 2;
			a[1] -= mn;
			a[3] -= mn;
			mn = max(a[1], a[3]);
			ans += (a[2] + 1) / 2;
			if (mn > 0) {
				if (a[2] % 2 == 1)
					mn += 2;
				ans += 1 + (mn - 1) / 4;
			}
		}
		cout << "Case #" << caseno << ": " << ans << endl;
	}
}