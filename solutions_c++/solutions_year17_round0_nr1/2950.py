/**
 * Sergey Kopeliovich (burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

void flip( char &c ) {
	c = '+' + '-' - c;
}

void solve() {
	string s;
	int k;
	cin >> s >> k;
	int n = s.length(), ans = 0;
	forn(i, n)
		if (s[i] == '-') {
			// printf("%s %d\n", s.c_str(), i);
			if (i + k > n) {
				puts("IMPOSSIBLE");
				return;
			}
			ans++;
			forn(j, k)
				flip(s[i + j]);
		}
	printf("%d\n", ans);
}

int main() {
	int tn;
	cin >> tn;
	for (int t = 1; t <= tn; t++) {
		printf("Case #%d: ", t);
		solve();
	}
}
