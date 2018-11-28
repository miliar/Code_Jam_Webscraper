#include<bits/stdc++.h>
#define rep(i,n)for(int i=0;i<(n);i++)
using namespace std;
typedef long long ll;

ll dp[20][2][10];
int main() {
	int T; scanf("%d", &T);
	for (int cnt = 1; cnt <= T; cnt++) {
		string s; cin >> s;
		memset(dp, -1, sizeof(dp));
		dp[0][0][0] = 0;
		rep(i, s.size())rep(j, 2)rep(k, 10) {
			int a = (j ? 9 : s[i] - '0');
			for (int t = k; t <= a; t++) {
				dp[i + 1][j || t < a][t] = max(dp[i + 1][j || t < a][t], dp[i][j][k] * 10 + t);
			}
		}
		ll ans = 0;
		rep(i, 10) {
			ans = max(ans, dp[s.size()][0][i]);
			ans = max(ans, dp[s.size()][1][i]);
		}
		printf("Case #%d: %lld\n", cnt, ans);
	}
}