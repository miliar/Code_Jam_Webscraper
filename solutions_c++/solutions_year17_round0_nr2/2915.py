/**
 * Sergey Kopeliovich (burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

void solve() {
	long long x;
	cin >> x;
	string s = to_string(x + 1);
	int n = s.length(), j = 0;
	while (j + 1 < n && s[j + 1] >= s[j])
		j++;
	// printf("j = %d\n", j);
	for (int i = min(n - 1, j + 1); i >= 0; i--) {
		// printf("check i = %d [s = %s] from %c to %c\n", i, s.c_str(), s[i] - 1, s[i - 1]);
		for (char c = s[i] - 1; c >= '0' && (!i || c >= s[i - 1]); c--) {
			if (i == 0 && c == '0')
				continue;
			forn(k, i)
				putchar(s[k]);
			putchar(c);
			forn(k, n - i - 1)
				putchar('9');
			return;
		}
	}
	forn(i, n - 1)
		putchar('9');
}

int main() {
	int tn;
	cin >> tn;
	for (int t = 1; t <= tn; t++) {
		printf("Case #%d: ", t);
		solve();
		puts("");
	}
}
