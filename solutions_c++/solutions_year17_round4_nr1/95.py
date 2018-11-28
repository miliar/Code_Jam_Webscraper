#include <bits/stdc++.h>

using namespace std;

const int MX = 100;

int cnt[4];
int dp[5][4][MX + 1][MX + 1][MX + 1];
bool ok[5][4][MX + 1][MX + 1][MX + 1];

int solve(int p, int s, int c1, int c2, int c3) {
	if (c1 + c2 + c3 == 0) return 0;
	if (ok[p][s][c1][c2][c3] == false) {
		ok[p][s][c1][c2][c3] = true;
		
		int res = 0;
		if (c1 > 0) res = max(solve(p, (s + 1) % p, c1 - 1, c2, c3), res);
		if (c2 > 0) res = max(solve(p, (s + 2) % p, c1, c2 - 1, c3), res);
		if (c3 > 0) res = max(solve(p, (s + 3) % p, c1, c2, c3 - 1), res);
		
		dp[p][s][c1][c2][c3] = res + (s == 0 ? 1 : 0);
	}
	
	return dp[p][s][c1][c2][c3];
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		memset(cnt, 0, sizeof cnt);
		
		int n, p;
		scanf("%d %d", &n, &p);
		for (int i = 0; i < n; i++) {
			int x;
			scanf("%d", &x);
			cnt[x % p]++;
		}
		
		printf("Case #%d: %d\n", t, cnt[0] + solve(p, 0, cnt[1], cnt[2], cnt[3]));
	}

	return 0;
}
