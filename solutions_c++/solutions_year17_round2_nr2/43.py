#include<stdio.h>
#include<string.h>
int n, m;
int a[6];
char p[10] = "ROYGBV";
char ans[1010];
int main() {
	int tcn;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++) {
		scanf("%d", &n);
		for (int i = 0; i < 6; i++) {
			scanf("%d", &a[i]);
		}
		int flag = 0;
		for (int i = 0; i < 6; i += 2) {
			if (a[(i + 3) % 6] > 0 && a[(i + 3) % 6] >= a[i]) {
				if (a[i] == a[(i + 3) % 6] && a[i] * 2 == n) {
					for (int j = 0; j < n; j++) {
						if (j % 2 == 0)ans[j] = p[i];
						else ans[j] = p[(i + 3) % 6];
					}
					ans[n] = 0;
					printf("Case #%d: %s\n", tc, ans);
				}
				else {
					printf("Case #%d: IMPOSSIBLE\n", tc);
				}
				flag = 1;
				break;
			}
		}
		if (flag)continue;
		for (int i = 0; i < 6; i += 2) {
			a[i] -= a[(i + 3) % 6];
		}
		m = a[0] + a[2] + a[4];
		for (int i = 0; i < 6; i += 2) {
			if (a[i] * 2 > m) {
				printf("Case #%d: IMPOSSIBLE\n", tc);
				flag = 1;
				break;
			}
		}
		if (flag)continue;
		ans[0] = 0;
		int ansl = 0;
		for (int x = 0; x < m; x++) {
			int t = -1;
			for (int i = 0; i < 6; i += 2) {
				if (x != 0 && ans[ansl - 1] == p[i])continue;
				if (t == -1 || a[i] > a[t] || (a[i] == a[t] && ans[0] == p[i])) {
					t = i;
				}
			}
			ans[ansl] = p[t];
			ansl++;
			a[t]--;
			while (a[(t + 3) % 6] > 0) {
				a[(t + 3) % 6]--;
				ans[ansl] = p[(t + 3) % 6];
				ansl++;
				ans[ansl] = p[t];
				ansl++;
			}
		}
		ans[n] = 0;
		printf("Case #%d: %s\n", tc, ans);
	}
	return 0;
}
