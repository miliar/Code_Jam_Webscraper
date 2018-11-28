#include <bits/stdc++.h>
using namespace std;
string number;
int dp[20][10][2];

long long dfs(int len, int d, bool limit) {
	if(len == number.length()) return 1;
	if(~dp[len][d][limit]) return dp[len][d][limit];
	long long ans = 0;
	int up = limit ? (number[len] - '0') : 9;
	for(int i = 0; i <= up; i++) {
		if(i >= d) ans += dfs(len + 1, i, limit && (i == up));
	}
	return dp[len][d][limit] = ans;
}


long long solve(long long n) {
	number = "";
	long long t = n;
	while(t > 0) {
		number += '0' + (t % 10);
		t /= 10;
	}
	reverse(number.begin(), number.end());
	int len = number.length();
	memset(dp, -1, sizeof(dp));
	return dfs(0, 0, true);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T, cases = 0;
	long long n;
	cin >> T;
	while(T--) {
		cin >> n;
		long long l = 1, r = n;
		long long tot = solve(n);
		long long ans = 0;
		while(l <= r) {
			long long mid = (l + r) >> 1;
			if(solve(mid) < tot) {
				ans = mid;
				l = mid + 1;
			} else {
				r = mid - 1;
			}
		}
		printf("Case #%d: %I64d\n", ++cases, ans + 1);
	}
	return 0;
}
