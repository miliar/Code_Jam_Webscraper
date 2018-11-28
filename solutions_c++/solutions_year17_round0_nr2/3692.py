#include <bits\stdc++.h>
#define RUN_TEST
using namespace std;

unsigned long long N;

unsigned long long DFS(unsigned long long &value, int threshold, unsigned long long multiplier) {
	if (multiplier == 0) {
		return value;
	}

	for (int i = 9; i >= threshold; i--) {
		if (value + multiplier * i <= N) {
			value += multiplier * i;
			if (DFS(value, i, multiplier / 10))
				return value;
			value -= multiplier * i;
		}
	}
	return 0;
}

unsigned long long solve() {
	unsigned long long ans = 0, mul = 1;
	while (N / mul >= 10)
		mul *= 10;

	while (mul > 0) {
		for (int i = 9; i >= 1; i--) {
			if (i * mul <= N) {
				ans += i * mul;
				if (DFS(ans, i, mul / 10))
					return ans;
				ans -= i * mul;
			}
		}
		mul /= 10;
	}

	puts("Not Possible");
}

int main() {
#ifdef RUN_TEST
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, c = 1;
	scanf("%d", &T);
	while (T--) {
		cin >> N;
		printf("Case #%d: %llu\n", c++, solve());
	}
	return 0;
}