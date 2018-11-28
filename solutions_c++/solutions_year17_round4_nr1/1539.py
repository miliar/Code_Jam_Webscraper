#include <bits/stdc++.h>
using namespace std;

int dp[105][105][105][4];

int dfs(int x, int y, int z, int r, int p) {
	if(x == 0 && y == 0 && z == 0) return 0;
	int &u = dp[x][y][z][r];
	if(~u) return u; 
	u = 0;
	if(x > 0) u = max(u, dfs(x - 1, y, z, (r + 1) % p, p));
	if(y > 0) u = max(u, dfs(x, y - 1, z, (r + 2) % p, p));
	if(z > 0) u = max(u, dfs(x, y, z - 1, (r + 3) % p, p));
	if(r == 0) u++;
	return u;
}

void solve_big(int cases) {
	int n, p;
	scanf("%d%d", &n, &p);
	int c[4];
	memset(c, 0, sizeof(c));
	int x;
	for(int i = 0; i < n; i++) {
		scanf("%d", &x);
		c[x % p]++;
	}
	memset(dp, -1, sizeof(dp));
	int ans = dfs(c[1], c[2], c[3], 0, p);	
	printf("Case #%d: %d\n", cases, c[0] + ans);
}

int main() {
	bool debug = false;
	if(debug) {
		freopen("sample_in.txt", "r", stdin);
	} else {
		freopen("A-large.in", "r", stdin);
		freopen("A-large.ou", "w", stdout);
	}

	int T, cases = 0;
	
	scanf("%d", &T);
	while(T--) {
		solve_big(++cases);
	}
	return 0;
}
