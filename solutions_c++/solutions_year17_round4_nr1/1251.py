#include<bits/stdc++.h>
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3f
#define MOD 1000000007
#define EPS (1e-10)
#define rep(i,n)for(int i=0;i<(n);i++)
using namespace std;
typedef long long ll;
typedef pair<int, int>P;

int g[100];
int cnt[4];
signed main() {
	int T; scanf("%d", &T);
	for (int Case = 1; Case <= T; Case++) {
		int n, p; scanf("%d%d", &n, &p);
		memset(cnt, 0, sizeof(cnt));
		rep(i, n) {
			scanf("%d", &g[i]); g[i] %= p;
			cnt[g[i]]++;
		}
		vector<vector<vector<vector<int>>>>dp(cnt[0] + 1, vector<vector<vector<int>>>(cnt[1] + 1, vector<vector<int>>(cnt[2] + 1, vector<int>(cnt[3] + 1))));
		rep(i, cnt[0] + 1)rep(j, cnt[1] + 1)rep(k, cnt[2] + 1)rep(t, cnt[3] + 1) {
			int a = (p - (j + 2 * k + 3 * t) % p) % p;
			if (i < cnt[0])dp[i + 1][j][k][t] = max(dp[i + 1][j][k][t], dp[i][j][k][t] + (a == 0));
			if (j < cnt[1])dp[i][j + 1][k][t] = max(dp[i][j + 1][k][t], dp[i][j][k][t] + (a == 0));
			if (k < cnt[2])dp[i][j][k + 1][t] = max(dp[i][j][k + 1][t], dp[i][j][k][t] + (a == 0));
			if (t < cnt[3])dp[i][j][k][t + 1] = max(dp[i][j][k][t + 1], dp[i][j][k][t] + (a == 0));
		}
		printf("Case #%d: %d\n", Case, dp[cnt[0]][cnt[1]][cnt[2]][cnt[3]]);
	}
}