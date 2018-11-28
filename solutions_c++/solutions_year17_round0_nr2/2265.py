#include <cstdio>
#include <string>

bool isTidy(long long n) {
	if (n <= 0) {
		return false;
	}
	std::string s = std::to_string(n);
	for (int i = 1; i < (int)s.size(); i++) {
		if (s[i] < s[i - 1]) {
			return false;
		}
	}
	return true;
}

long long solveOne(long long n) {
	if (isTidy(n)) {
		return n;
	}
	long long r = 1;
	for (int i = 0; i < 17; i++) {
		r *= 10;
		long long c = n - n % r - 1;
		if (isTidy(c)) {
			return c;
		}
	}
	throw 1;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		long long n;
		scanf("%lld", &n);
		printf("Case #%d: %lld\n", i, solveOne(n));
	}
	return 0;
}
