#include <iostream>

using namespace std;

int dp[110][110][110][5];
int cnt[5];

int main()
{
	int tt;
	cin >> tt;
	for (int tc = 1; tc <= tt; tc++)
	{
		int n, p;
		cin >> n >> p;
		for (int i = 0; i < 4; i++)
			cnt[i] = 0;
		for (int i = 0; i < n; i++)
		{
			int g;
			cin >> g;
			cnt[g % p]++;
		}
		for (int i = 0; i <= cnt[1]; i++)
			for (int j = 0; j <= cnt[2]; j++)
				for (int k = 0; k <= cnt[3]; k++)
					for (int cur = 0; cur < p; cur++)
						dp[i][j][k][cur] = -2 * n;
		dp[cnt[1]][cnt[2]][cnt[3]][0] = 0;
		for (int i = cnt[1]; i >= 0; i--)
			for (int j = cnt[2]; j >= 0; j--)
				for (int k = cnt[3]; k >= 0; k--)
					for (int cur = 0; cur < p; cur++)
					{
						if (i)
							dp[i - 1][j][k][(cur + 1) % p] = max(dp[i - 1][j][k][(cur + 1) % p], dp[i][j][k][cur] + (cur == 0));
						if (j)
							dp[i][j - 1][k][(cur + 2) % p] = max(dp[i][j - 1][k][(cur + 2) % p], dp[i][j][k][cur] + (cur == 0));
						if (k)
							dp[i][j][k - 1][(cur + 3) % p] = max(dp[i][j][k - 1][(cur + 3) % p], dp[i][j][k][cur] + (cur == 0));
					}
		int res = 0;
		for (int i = 0; i < p; i++)
			res = max(res, dp[0][0][0][i]);
		cout << "Case #" << tc << ": " << res + cnt[0] << endl;
	}
}
