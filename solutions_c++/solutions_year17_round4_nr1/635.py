#include <bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)

const int INF = 0x3f3f3f3f;
int n, P, c[5], dp[111][111][111];
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		cin >> n >> P;
		memset(c, 0, sizeof c);
		For(i,1,n) {
			int x;
			cin >> x;
			++c[x % P];
		}
		int ans = c[0];
		memset(dp, -INF, sizeof dp);
		dp[0][0][0] = 0;
		For(i,0,c[1]) For(j,0,c[2]) For(k,0,c[3]) if (dp[i][j][k] < 0) {
			int taken = (c[1] - i) * 1 + (c[2] - j) * 2 + (c[3] - k) * 3;
			int add = 0;
			if (taken % P == 0) add = 1;
			if (i) dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k]);
			if (j) dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k]);
			if (k) dp[i][j][k] = max(dp[i][j][k], dp[i][j][k - 1]);
			dp[i][j][k] += add;
		}
		ans += dp[c[1]][c[2]][c[3]];
		printf("Case #%d: %d\n", TK, ans);
	}
	return 0;
}