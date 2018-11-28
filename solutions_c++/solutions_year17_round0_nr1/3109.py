#include <bits/stdc++.h>
using namespace std;

char change (const char &c) {
	return (c == '+') ? '-' : '+';
}

int main () {
	int test; cin >> test;
	for (int t = 1; t <= test; ++t) {
		string s; int k; cin >> s >> k;
		printf("Case #%d: ", t);
		int ans = 0;
		for (int i = 0; i <= s.length() - k; ++i) {
			if (s[i] == '-') {
				++ans;
				for (int j = 0; j < k; ++j) {
					s[i + j] = change(s[i + j]);
				}
			}
		}
		for (int i = 0; i < s.length(); ++i)
			if (s[i] == '-')
				ans = -1;
		if (ans == -1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}
	return 0;
}