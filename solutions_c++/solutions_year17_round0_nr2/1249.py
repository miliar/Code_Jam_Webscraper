#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL;
typedef pair<int, int> II;

const int N = 20 + 10;
LL dp[N][10];

void Init() {
	dp[0][9] = 1;
	for (int i = 1; i <= 20; ++i) for (int x = 0; x < 10; ++x) {
		dp[i][x] = 0;
		for (int y = x; y < 10; ++y) dp[i][x] += dp[i - 1][y];
	}
}

LL Count(LL N) {
	int a[30], n = 0; a[0] = 0; N++;
	while (N) {
		a[++n] = N % 10;
		N /= 10;
	}
	reverse(a + 1, a + 1 + n);

	LL ans = 0;
	for (int i = 1; i <= n; ++i) {
		for (int d = a[i - 1]; d < a[i]; ++d) ans += dp[n - i + 1][d];
		if (a[i - 1] > a[i]) break;
	}
	return ans;
}

LL Find(LL N) {
	LL l = 1, r = N, f = 1, v = Count(N);
	while (l <= r) {
		LL m = (l + r) >> 1;
		if (Count(m) == v) {
			f = m;
			r = m - 1;
		}
		else l = m + 1;
	}
	return f;
}

int main() {
	int TC; scanf("%d", &TC); Init();
	for (int testID = 1; testID <= TC; ++testID) {
		LL n; scanf("%I64d", &n);
		printf("Case #%d: %I64d\n", testID, Find(n));
	}
	return 0;
}