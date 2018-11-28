#include<stdio.h>
#include<string.h>
int d,n;
int k[1010];
int s[1010];
int main() {
	int tcn;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++) {
		scanf("%d%d", &d, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d%d", &k[i], &s[i]);
		}
		double ans = 1e99;
		for (int i = 0; i < n; i++) {
			if (d / ans < ((double)d - k[i]) / s[i]) {
				ans = d / (((double)d - k[i]) / s[i]);
			}
		}
		printf("Case #%d: %.30f\n", tc, ans);
	}
	return 0;
}
