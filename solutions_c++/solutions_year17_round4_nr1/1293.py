#include <bits/stdc++.h>
using namespace std;

int p;
int dp[105][105][105][4];
int sol(int i, int j, int k, int md)
{
	if (i < 0 || j < 0 || k < 0)
		return -1000000000;
	if (i == 0 && j == 0 && k == 0)
		return 0;
	if (dp[i][j][k][md] != -1)
		return dp[i][j][k][md];
	int start = 0;
	if (md == 0)
		start++;
	int res = start;

	res = max(res, max(start + sol(i-1, j, k, (md + 1) % p), max(start + sol(i, j - 1, k, (md + 2) % p), start + sol(i, j, k - 1, (md + 3) % p))));
	return dp[i][j][k][md] = res;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; z++)
	{
		memset(dp, -1, sizeof(dp));
		int f[4] = {0};
		int n;
		scanf("%d %d", &n, &p);
		for (int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			f[x%p]++;
		}
		int res = f[0];
		res += sol(f[1], f[2], f[3], 0);
		printf("Case #%d: %d\n", z, res);

	}
}