#include <bits/stdc++.h>
using namespace std;

long long N;
string NS;
long long pw[20];
long long dp[20][10][2];
long long sol(int i, int lst, int less)
{
	if (i == 19)
		return 0;
	if (dp[i][lst][less] != -1)
		return dp[i][lst][less];
	int end = 9;
	if (!less)
		end = NS[i] - '0';
	dp[i][lst][less] = -5;
	for (int j = lst; j <= end; j++)
	{
		int nl = less || (j < end);
		if (nl)
			nl = 1;
		long long nxt = sol(i + 1, j, nl);
		if (nxt >= 0)
			dp[i][lst][less] = max(dp[i][lst][less], j * pw[18 - i] + nxt);
	}
	return dp[i][lst][less];
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	pw[0] = 1;
	for (int i = 1; i < 18; i++)
		pw[i] = 10 * pw[i-1];
	for (int z = 1; z <= T; z++)
	{
		memset(dp, -1, sizeof(dp));
		scanf("%lld", &N);
		long long N2 = N;
		NS = "";
		for (int i = 0; i < 19; i++)
		{
			NS += '0' + N2 % 10;
			N2 /= 10;
		}
		reverse(NS.begin(), NS.end());
		printf("Case #%d: %lld\n", z, sol(0, 0, 0));
	}
}