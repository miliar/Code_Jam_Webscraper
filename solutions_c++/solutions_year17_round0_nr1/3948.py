#include <cstdio>
#include <iostream>

using namespace std;

int t, k;
string s;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	cin >> t;
	for (int it = 1; it <= t; ++it) {
		cin >> s >> k;
		int ans = 0, n = s.length();
		for (int i = 0; i <= n - k; ++i) {
			if (s[i] == '-') {
				for (int j = i; j < i + k; ++j) {
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
				ans++;
			}			
		}

		bool ok = true;
		for (int i = 0; i < n; ++i)
			if (s[i] == '-')
				ok = false;

		printf("Case #%d: ", it);
		if (ok) {
			printf("%d\n", ans);			
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
}