#include <bits/stdc++.h>
using namespace std;

int dp[105][105][105][4];
int n, p;

int solve(int a, int b, int c, int x) {
	if(a + b + c == 0) {
		return 0;
	}

	int &ret = dp[a][b][c][x];
	if(ret != -1) return ret;

	ret = -1e9;
	if(a) ret = max(ret, solve(a-1,b,c,(x + 1) % p));
	if(b) ret = max(ret, solve(a,b-1,c,(x + 2) % p));
	if(c) ret = max(ret, solve(a,b,c-1,(x + 3) % p));
	if(x == 0) ret++;

	return ret;
}

int work() {
	memset(dp, -1, sizeof dp);
	cin >> n >> p;
	int nol = 0;
	int sisa[5] = {0};

	for(int i = 0 ; i < n ; i++) {
		int x; cin >> x;
		sisa[x % p]++;
	}

	int ret = sisa[0];
	ret += solve(sisa[1], sisa[2], sisa[3], 0);

	return ret;
}

int main() {
	int t; cin >> t;
	for(int tc = 1 ; tc <= t ; tc++) {
		int ret = work();

		printf("Case #%d: %d\n", tc, ret);
	}
	return 0;
}