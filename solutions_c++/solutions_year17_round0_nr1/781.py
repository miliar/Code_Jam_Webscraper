#include <bits/stdc++.h>

using namespace std;

const int N = 1e3 + 7;

int solve(char *s, int n, int k) {
	int ret = 0;
	for (int i = 0; i < n; i++) {
		if (s[i] == '-') {
			if (i + k > n) return -1;
			ret++;
			for (int j = i; j < i + k; j++) {
				s[j] = (s[j] == '+' ? '-' : '+');
			}
		}
	}
	return ret;
}

int main() {
	int test;
	scanf("%d", &test);
	while (test--) {
		static char s[N];
		int k;
		scanf("%s %d", s, &k);
		int n = strlen(s);
		static int test_count = 0;
		printf("Case #%d: ", ++test_count);
		int t = solve(s, n, k);
		if (t == -1) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", t);
		}
	}
	return 0;
}
