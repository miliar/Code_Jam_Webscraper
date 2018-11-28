#include <bits/stdc++.h>
using namespace std;

int ac[1500];
int dp[1500][725][3][3];

int calc(int mn, int f, int t, int s) {

	if (f > 720) return 1e9;
	if (mn == 1440) {
		if (f != 720) return 1e9;
		return t != s;
	}
	int &ret = dp[mn][f][t][s];
	if (ret != -1) return ret;
	ret = 0;
	if (ac[mn] == 2) {
		if (t == 1)
			ret = calc(mn + 1, f + 1, t, s);
		else
			ret = calc(mn + 1, f + 1, 1, s) + 1;

	} else if (ac[mn] == 1) {
		if (t == 1)
			ret = calc(mn + 1, f, 2, s) + 1;
		else
			ret = calc(mn + 1, f, 2, s);

	} else {

		if (t == 1)
			ret = min(calc(mn + 1, f + 1, t, s), calc(mn + 1, f, 2, s) + 1);
		else
			ret = min(calc(mn + 1, f, t, s), calc(mn + 1, f + 1, 1, s) + 1);
	}
	return ret;
}

int main() {

	freopen("readin.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	while (t--) {

		int n, m;
		scanf("%d%d", &n, &m);
		memset(ac, 0, sizeof ac);
		memset(dp, -1, sizeof dp);
		for (int i = 0, a, b; i < n; i++) {
			scanf("%d%d", &a, &b);
			b--;
			for (int j = a; j <= b; j++) {
				ac[j] = 1;
			}
		}
		for (int i = 0, a, b; i < m; i++) {
			scanf("%d%d", &a, &b);
			b--;
			for (int j = a; j <= b; j++) {
				ac[j] = 2;
			}
		}
		int ans = min(calc(0, 0, 1, 1), calc(0, 0, 2, 2));
		static int tc = 1;
		printf("Case #%d: %d\n", tc++, ans);

	}

	return 0;
}
