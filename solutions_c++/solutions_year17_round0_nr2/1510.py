#include <bits/stdc++.h>
using namespace std;

int T;
long long N;
int B[2000];
int cas = 0;
long long dp[30][2][20];
long long p10[200];
long long DP(int p, int up, int last) {
	if(p == 0) return 0;
	long long& ans = dp[p][up][last];
	if(ans != -1) return ans;
	ans = -2;
	for(int i = last; i < 10; i++) {
		if(up && i > B[p]) break;
		long long res = DP(p - 1, up && i == B[p], i);
		if(res < 0) continue;
		ans = max(ans, i * p10[p - 1] + res);
	}
	return ans;
}
int main() {
	freopen("./in.txt", "r", stdin);
	freopen("./out.txt", "w", stdout);
	p10[0] = 1;
	for(int i = 1; i < 30; i++) {
		p10[i] = p10[i - 1] * 10;
	}
	cin >> T;
	while(T--) {
		memset(dp, -1, sizeof dp);
		printf("Case #%d: ", ++cas);
		cin >> N;
		B[0] = 0;
		while(N > 0) {
			B[++B[0]] = N % 10;
			N /= 10;
		}
		printf("%lld\n", DP(B[0], 1, 0));
	}
	return 0;
}
