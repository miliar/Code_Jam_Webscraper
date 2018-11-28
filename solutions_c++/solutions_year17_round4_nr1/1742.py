#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int n, p;
		cin >> n >> p;

		vector<int> c(p);
		for (int i = 0; i < n; ++i) {
			int g;
			cin >> g;
			++c[g % p];
		}

		int ans = c[0];
		if (p == 2) {
			ans += (c[1] + 1) / 2;
		} else if (p == 3) {
			int m = min(c[1], c[2]);
			ans += m;
			c[1] -= m;
			c[2] -= m;
			if (c[1] > 0) {
				ans += (c[1] + 2) / 3;
			} else if (c[2] > 0) {
				ans += (c[2] + 2) / 3;
			}
		} else if (p == 4) {
			int m = min(c[1], c[3]);
			ans += m;
			c[1] -= m;
			c[3] -= m;
			ans += c[2] / 2;
			c[2] = c[2] % 2;
			if (c[2] > 0 && c[1] > 1) {
				++ans;
				c[2] = 0;
				c[1] -= 2;
			} else if (c[2] > 0 && c[3] > 1) {
				++ans;
				c[2] = 0;
				c[3] -= 3;
			}
			if (c[1] > 0) {
				ans += (c[1] + 3) / 4;
			} else if (c[3] > 0) {
				ans += (c[3] + 3) / 4;
			}
		}

		cout << "Case #" << test << ": " << ans << endl;
	}
}
