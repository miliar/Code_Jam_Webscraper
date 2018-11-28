#include<stdio.h>
long long int n;
long long int f(long long int x) {
	if (x == 0)return 0;
	long long int res;
	if (x % 10 < x / 10 % 10)res = f(x / 10 - 1);
	else res = f(x / 10);
	int p = 0;
	while (res * 10 + p < x&&p < 9)p++;
	return res * 10 + p;
}
int main() {
	int tcn;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++) {
		scanf("%lld", &n);
		printf("Case #%d: %lld\n", tc, f(n));
	}
	return 0;
}
