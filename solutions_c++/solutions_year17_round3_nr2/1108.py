#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <stack>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef double DB;

const int MaxN = 1500;
int T, n, m, ans;
int vis[MaxN + 5], dp[3][MaxN + 5][805];

void Solve() {
	memset(dp, 63, sizeof(dp));
	dp[1][0][0] = 0; dp[2][0][0] = 0;
	for(int i = 1; i <= 1440; i++) {
		for(int j = 0; j <= 720; j++) {
			if(j) {
				if(vis[i] == 0) {
					dp[1][i][j] = min(dp[1][i - 1][j - 1], dp[2][i - 1][j - 1] + 1);
					dp[2][i][j] = min(dp[2][i - 1][j], dp[1][i - 1][j] + 1);
				}
				if(vis[i] == 1)
					dp[1][i][j] = min(dp[1][i - 1][j - 1], dp[2][i - 1][j - 1] + 1);
				if(vis[i] == 2)
					dp[2][i][j] = min(dp[2][i - 1][j], dp[1][i - 1][j] + 1);
			}
			else {
				if(vis[i] == 0 || vis[i] == 2) {
					dp[2][i][j] = dp[2][i - 1][j];
				}
			}
		}
	}
	if(vis[1] == 1) {
		if(dp[1][1440][720] <= dp[2][1440][720]) ans = min(ans, dp[1][1440][720]);
		else ans = min(ans, dp[2][1440][720] + 1);
	}
	else {
		if(dp[1][1440][720] <= dp[2][1440][720]) ans = min(ans, dp[1][1440][720] + 1);
		else ans = min(ans, dp[2][1440][720]);
	}
}

int main() 
{
		freopen("A.in", "r", stdin);
		freopen("A.out", "w", stdout);
	scanf("%d", &T); int cas = 0;
	while(T--) {
		scanf("%d%d", &n, &m);
		memset(vis, 0, sizeof(vis));
		for(int i = 1; i <= n; i++) {
			int l, r;
			scanf("%d%d", &l, &r);
			for(int j = l + 1; j <= r; j++) vis[j] = 1;
		}
		for(int i = 1; i <= m; i++) {
			int l, r;
			scanf("%d%d", &l, &r);
			for(int j = l + 1; j <= r; j++) vis[j] = 2;
		}
		ans = 1 << 30;
		if(vis[1] == 0) {
			vis[1] = 1;
			Solve();
			vis[1] = 2;
			Solve();
		}
		else if(vis[1] == 1) {
			Solve();
		}
		else if(vis[1] == 2) {
			Solve();
		}
		printf("Case #%d: %d\n", ++cas, ans);
	} 
		fclose(stdin);
		fclose(stdout);
}
