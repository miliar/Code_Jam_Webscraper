#include<vector>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
using namespace std;
FILE *fi = freopen("A-large.in", "r", stdin);
FILE *fo = freopen("ALout.txt", "w", stdout);
int N, test, P, dp[102][102][102][4];
int dfs(int a, int b, int c, int r) {
	int &ret = dp[a][b][c][r];
	if (ret != -1) return ret;
	ret = 0;
	if (a > 0) {
		ret = max(ret, dfs(a - 1, b, c, (r + 1) % P));
	}
	if (b > 0) {
		ret = max(ret, dfs(a, b - 1, c, (r + 2) % P));
	}
	if (c > 0) {
		ret = max(ret, dfs(a, b, c - 1, (r + 3) % P));
	}
	if (a != 0 || b != 0 || c != 0) {
		if (r == 0)ret++;
	}
	return ret;
}
int cnt[5];
int main() {
	int lev = 0;
	scanf("%d", &test); while (test--) {
		++lev;
		memset(cnt, 0, sizeof(cnt));
		memset(dp, -1, sizeof(dp));
		scanf("%d %d", &N, &P);
		for (int t, i = 1; i <= N; i++) {
			scanf("%d", &t);
			cnt[t%P]++;
		}
		int ans = dfs(cnt[1], cnt[2], cnt[3], 0);
		ans += cnt[0];
		printf("Case #%d: %d\n", lev, ans);
	}
}