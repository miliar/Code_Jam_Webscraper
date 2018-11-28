#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

long long a, ans;
long long f[20];
int t;

long long solve() {
	int n = 0, i;
	long long ori=a;
	while (a > 0) {
		f[n++] = a % 10;
		a /= 10;
	}
	f[n] = 0;
	for (i = n - 1;i >= 0;--i) {
		if (f[i] < f[i + 1]) break;
	}

	//printf("%d", i);
	if (i < 0) return ori;
	i++;
	--f[i];
	while (i < n - 1 && f[i] < f[i + 1]) {
		i++;
		--f[i];
	}
	long long ret = 0;
	for (int j = n - 1;j >= 0;--j) {
		ret = ret * 10 + (j >= i ? f[j] : 9);
	}

	return ret;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d%*c", &t);
	for (int i = 1;i <= t;++i) {
		scanf("%lld", &a);
		//printf("%lld\n", a);
		ans = solve();
		printf("Case #%d: ", i);
		printf("%lld\n", ans);
	}

	return 0;
}