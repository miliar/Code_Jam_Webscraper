#include<bits/stdc++.h>
using namespace std;
typedef  int ll;
#define OO int(1e9)
#define N 1600
int dp[800][800][2][2], t, res, g = 0, n, m, x, y;
bool b[N][2];
int solve(int fr, int se, int cur,int st)
{
	if (fr > 720 || se > 720)return OO;
	if (b[fr + se][cur])return OO;
	if (fr + se == 1440)
		return (cur!=st);
	ll &r = dp[fr][se][cur][st], c1, c2;
	if (r != -1)return r;
	if (cur)c1 = solve(fr, se + 1, cur,st), c2 = solve(fr + 1, se, 1 - cur,st) + 1;
	else c1 = solve(fr + 1, se, cur,st), c2 = solve(fr, se + 1, 1 - cur,st) + 1;
	return r = min(c1, c2);
}
int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	scanf("%d", &t);
	while (t--)
	{
		memset(dp, -1, sizeof dp);
		memset(b, 0, sizeof b);
		g++;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
		{
			scanf("%d%d", &x, &y);
			for (int j = x; j < y; j++)
				b[j][0] = true;
		}
		for (int i = 0; i < m; i++)
		{
			scanf("%d%d", &x, &y);
			for (int j = x; j < y; j++)
				b[j][1] = true;
		}
		res = min(solve(0, 0, 0,0), solve(0, 0, 1,1));
		if (res == 1)res++;
		printf("Case #%d: %d\n", g, res);
	}
	return 0;
}