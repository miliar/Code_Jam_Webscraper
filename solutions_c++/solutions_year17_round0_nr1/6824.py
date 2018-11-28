#include <bits/stdc++.h>
using namespace std;

string s;
int t, k, n;

int main() {
	cin >> t;
	for (int p = 0; p < t; p++) {
		cin >> s >> k;
		n = s.length();
		int ans = 0;
		int imp = 0;
		for (int i = 0; i <= n - k; i++) {
			if (s[i] == '+') continue;
			else {
				int j = 0;
				while (j < k) {
					if (s[i + j] == '-') s[i + j] = '+';
					else s[i + j] = '-';
					j++;
				}
				ans += 1;
			}
		}

		for (int i = n - k; i < n; i++) {
			if (s[i] == '-') {
				imp = 1;
			}
		}

		if (imp) {
			printf("Case #%d: IMPOSSIBLE\n", p + 1);
		}
		else {
			printf("Case #%d: %d\n", p + 1, ans);
		}
	}
}