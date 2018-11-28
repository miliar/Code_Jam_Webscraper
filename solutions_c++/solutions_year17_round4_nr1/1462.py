#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
	int t, n, p;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n >> p;
		vector<int> g(n);
		int a, b;
		a = b = 0;
		int aa, bb, cc;
		aa = bb = cc = 0;
		int aaa, bbb, ccc, ddd;
		aaa = bbb = ccc = ddd = 0;
		for (int j = 0; j < n; j++) {
			cin >> g[j];
			if (g[j] % 2 == 0) {
				a++;
			}
			else {
				b++;
			}
			if (g[j] % 3 == 0) {
				aa++;
			}
			else if (g[j] % 3 == 1) {
				bb++;
			}
			else {
				cc++;
			}
			if (g[j] % 4 == 0) {
				aaa++;
			}
			else if (g[j] % 4 == 1) {
				bbb++;
			}
			else if (g[j] % 4 == 2) {
				ccc++;
			}
			else {
				ddd++;
			}
		}

		if (p == 2) {
			//cout << a << endl;
			int ans = a;
			ans += b / 2;
			b %= 2;
			if (b > 0) {
				ans++;
			}
			printf("Case #%d: %d\n", i + 1, ans);
		}
		else if (p == 3) {
			int ans = aa;
			int kk = min(bb, cc);
			ans += kk;
			bb -= kk;
			cc -= kk;
			ans += bb / 3;
			bb %= 3;
			ans += cc / 3;
			cc %= 3;
			if (bb > 0) {
				ans++;
			}
			if (cc > 0) {
				ans++;
			}
			printf("Case #%d: %d\n", i + 1, ans);
		}
		else if (p == 4) {
			int ans = aaa;
			int kk = min(bbb, ddd);
			ans += kk;
			bbb -= kk;
			ddd -= kk;
			int b1, b2, c1, c2, d1, d2;
			b1 = b2 = bbb;
			c1 = c2 = ccc;
			d1 = d2 = ddd;
			int ans1, ans2;
			ans1 = ans2 = ans;
			while (c1 > 1) {
				ans1++;
				c1 -= 2;
			}
			while (b1 > 3) {
				ans1++;
				b1 -= 4;
			}
			while (d1 > 3) {
				ans++;
				d1 -= 4;
			}
			while (b1 > 1 && c1 > 0) {
				ans1++;
				b1 -= 2;
				c1--;
			}
			while (d1 > 1 && c1 > 0) {
				ans1++;
				d1 -= 2;
				c1--;
			}
			if (b1 > 0 || c1 > 0 || d1 > 0) {
				ans1++;
			}
			while (b2 > 1 && c2 > 0) {
				ans2++;
				b2 -= 2;
				c2--;
			}
			while (d2 > 1 && c2 > 0) {
				ans2++;
				d2 -= 2;
				c2--;
			}
			while (c2 > 1) {
				ans2++;
				c2 -= 2;
			}
			while (b2 > 3) {
				ans2++;
				b2 -= 4;
			}
			while (d2 > 3) {
				ans2++;
				d2 -= 4;
			}
			if (b2 > 0 || c2 > 0 || d2 > 0) {
				ans2++;
			}
			printf("Case #%d: %d\n", i + 1, max(ans1, ans2));
		}
	}
	return 0;
}