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

long long n;
int a[N];

long long solve() {
	int len = 0;
	while (n) {
		a[len++] = n % 10;
		n /= 10;
	}
	for (int i = 0; i < len; i++) {
		for (int d = a[i]; d >= 0; d--) {
			if (i && d == a[i]) continue;
			if (i + 1 < len && d < a[i + 1]) continue;
			bool flag = true;
			for (int k = i + 1; k + 1 < len; k++) {
				if (a[k] < a[k + 1]) flag = false;
			}
			if (flag) {
				long long nn = 0;
				a[i] = d;
				for (int j = len - 1; j >= 0; j--) {
					nn = nn * 10 + a[j];
				}
				return nn;
			}
		}
		a[i] = 9;
	}
	assert(false);
}

int main() {
	int test;
	scanf("%d", &test);
	while (test--) {
		cin >> n;
		static int test_count = 0;
		printf("Case #%d: ", ++test_count);
		cout << solve() << endl;
	}
	return 0;
}
