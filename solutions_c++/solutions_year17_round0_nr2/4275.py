#include <cstdio>

typedef long long lli;

lli solve(lli);
bool is_tidy(lli);

int main() {
	int tc;
	scanf("%d", &tc);
	
	for (int t = 1; t <= tc; ++t) {
		lli x;
		scanf("%lld", &x);
		const lli ans = solve(x);
		printf("Case #%d: %lld\n", t, ans);
	}

	return 0;
}

bool is_tidy(lli x) {
	int l = 9;
	while (x > 0) {
		const int p = x % 10;
		if (p > l) return false;
		l = p;
		x /= 10;
	}

	return true;
}

lli solve(lli x) {
	int cnt = 0;
	while(!is_tidy(x)) {
		while (x % 10 == 0) {
			++cnt;
			x /= 10;
		}
		--x;
	}
	while(cnt--) {
		x = x * 10 + 9;
	}
	return x;
}