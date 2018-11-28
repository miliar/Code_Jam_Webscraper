#include <bits/stdc++.h>

using namespace std;

#define MAXN 2010

int t;
double dis[MAXN], speed[MAXN], dp[MAXN];
long long w[MAXN][MAXN], sum[MAXN];

int main()
{
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		int n, q;
		cin >> n >> q;
		for (int i = 0; i < n; i++)
		{
			dp[i] = 1000000000ll;
			dp[i] = dp[i] * dp[i] + 100ll;
			cin >> dis[i] >> speed[i];
		}
		// cout << "salam 1" << endl;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				cin >> w[i][j];

		for (int i = 0; i < q; i++)
		{
			int x, y;
			cin >> x >> y;
		}

		sum[0] = 0;
		for (int i = 1; i < n; i++)
			sum[i] = sum[i - 1] + w[i - 1][i];
		dp[0] = 0;

		// for (int i = 0; i < n; i++)
			// cout << sum[i] << " ";
		// cout << endl;
		// cout << "salam 2" << endl;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < i; j++)
			{
				long long len = sum[i] - sum[j];
				if (len > dis[j])
					continue;
				dp[i] = min(dp[i], dp[j] + len / speed[j]);
				// cout << i << "->" << j << " " << len << "/" << speed[j] << endl;
			}
			// cout << dp[i] << " ";
		}
		// cout << "salam 3" << endl;
		// cout << endl;
		cout << "Case #" << tt << ": " << setprecision(9) << fixed << dp[n - 1] << endl;
	}
	return 0;
}