#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int dp[1500][800][2][2];
int dat[1500][2];
int main()
{
	freopen("b-large.in", "r", stdin);
	freopen("outl.txt", "wb", stdout);
	int data;
	scanf("%d", &data);
	for (int p = 1; p <= data; p++)
	{
		int na, nb;
		scanf("%d%d", &na, &nb);
		for (int i = 0; i < 1500; i++)dat[i][0] = dat[i][1] = 1;
		for (int i = 0; i < 1500; i++)for (int j = 0; j < 800; j++)for (int k = 0; k < 2; k++)dp[i][j][k][0] = dp[i][j][k][1] = 10000;
		for (int i = 0; i < na; i++)
		{
			int za, zb;
			scanf("%d%d", &za, &zb);
			for (int j = za; j < zb; j++)dat[j][0] = 0;
		}
		for (int i = 0; i < nb; i++)
		{
			int za, zb;
			scanf("%d%d", &za, &zb);
			for (int j = za; j < zb; j++)dat[j][1] = 0;
		}
		if (dat[1439][0])dp[0][0][0][0] = 0;
		if (dat[1439][1])dp[0][0][1][1] = 0;
		for (int t = 0; t < 2;t++)
		{
			for (int i = 0; i < 1440; i++)
			{
				for (int j = 0; j < 790; j++)
				{
					if (dat[i][0])
					{
						dp[i + 1][j + 1][0][t] = min(dp[i + 1][j + 1][0][t], dp[i][j][0][t]);
						dp[i + 1][j + 1][0][t] = min(dp[i + 1][j + 1][0][t], dp[i][j][1][t] + 1);
					}
					if (dat[i][1])
					{
						dp[i + 1][j][1][t] = min(dp[i + 1][j][1][t], dp[i][j][1][t]);
						dp[i + 1][j][1][t] = min(dp[i + 1][j][1][t], dp[i][j][0][t] + 1);
					}
				}
			}
		}
		int ans = min(dp[1440][720][0][0], dp[1440][720][1][1]);
		printf("Case #%d: %d\n", p, ans);
	}
}