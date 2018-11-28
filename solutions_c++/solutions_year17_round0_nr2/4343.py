#include <bits/stdc++.h>

using namespace std;

char s[111];

long long calc(char s[]) {
	int n = strlen(s);
	long long ans = 0;
	bool consecutiveNines = false;
	for (int i = 0; i < n; ++i) {
		if (consecutiveNines) {
			ans = ans * 10 + 9;
		} else {
			int use = -1;
			bool existGreater = false;
			for (int j = i + 1; use == -1 && j < n; ++j) {
				if (s[j] > s[i]) {
					existGreater = true;
				} else if (s[j] < s[i]) {
					if (existGreater) {
						use = s[i] - '0';
					} else {
						use = s[i] - 1 - '0';
					}
				}
			}
			if (use == -1) use = s[i] - '0';
			if (use != s[i] - '0') {
				consecutiveNines = true;
			}
			ans = ans * 10 + use;
		}
	}
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		scanf("%s", s);
		printf("Case #%d: %lld\n", tc, calc(s));
	}
	return 0;
}