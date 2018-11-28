#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int f[1500][1500][2], n, m, color[2000];

int dp(int c1) {
	int total_minite = 24 * 60;
	if (color[0] > 0 && color[0] != c1)
		return 100000;
	for (int i = 0; i <= total_minite; i++) {
		for (int j = 0; j <= total_minite; j++) {
			f[i][j][0] = 100000;
			f[i][j][1] = 100000;
		}
	}
	if (c1 == 1)
		f[1][0][0] = 0;
	else
		f[0][1][1] = 0;
	for (int i = 1; i < total_minite; i++) {
		for (int t1 = 0; t1 <= i; t1++) {
			if (color[i] == 0 || color[i] == 1) {
				f[t1 + 1][i - t1][0] = min(f[t1][i - t1][0], f[t1 + 1][i - t1][0]);
				f[t1 + 1][i - t1][0] = min(f[t1][i - t1][1] + 1, f[t1 + 1][i - t1][0]);
			}

			if (color[i] == 0 || color[i] == 2) {
				f[t1][i - t1 + 1][1] = min(f[t1][i - t1][0] + 1, f[t1][i - t1 + 1][1]);
				f[t1][i - t1 + 1][1] = min(f[t1][i - t1][1], f[t1][i - t1 + 1][1]);
			}
			// printf(" f[%d,%d] = %d %d\n", t1, i - t1, f[t1][i - t1][0], f[t1][i - t1][1]);
		}
	}
	// printf(" %d %d\n", f[total_minite / 2][total_minite / 2][0], f[total_minite / 2][total_minite / 2][1]);
	if (c1 == 1)
		return min(f[total_minite / 2][total_minite / 2][0], f[total_minite / 2][total_minite / 2][1] + 1);
	else
		return min(f[total_minite / 2][total_minite / 2][0] + 1, f[total_minite / 2][total_minite / 2][1]);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; TT++) {
		printf("Case #%d: ", TT);

		memset(color, 0, sizeof(color));
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			int l, r;
			scanf("%d%d", &l, &r);
			for (int j = l; j < r; j++) color[j] = 1;
		}
		for (int i = 0; i < m; i++) {
			int l, r;
			scanf("%d%d", &l, &r);
			for (int j = l; j < r; j++) color[j] = 2;
		}

		int ans = min(dp(1), dp(2));
		printf("%d\n", ans);
	}

	return 0;
}