#include <bits/stdc++.h>

using namespace std;

#define PI 3.14159265358979323846

vector<pair<int, int> > a;
long double dp[1010][1010];
int t;

int main()
{
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		long double ans = 0;
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++)
		{
			int r, h;
			cin >> r >> h;
			a.push_back(make_pair(r, h));
		}

		sort(a.begin(), a.end());
		reverse(a.begin(), a.end());

		for (int i = 0; i < n; i++)
		{
			dp[i][1] = 2 * PI * (long double)a[i].first * (long double)a[i].second;
			dp[i][1] += PI * (long double)a[i].first * (long double)a[i].first;
		}

		for (int j = 2; j <= k; j++)
			for (int i = 0; i < n; i++)
			{
				dp[i][j] = 0;
				for (int l = 0; l < i; l++)
					dp[i][j] = max(dp[i][j], dp[l][j - 1] + 2 * PI * (long double)a[i].first * (long double)a[i].second);
			}

		for (int i = 0; i < n; i++)
			ans = max(ans, dp[i][k]);

		cout << "Case #" << tt << ": " << setprecision(9) << fixed << ans << endl;
		a.clear();
	}
	return 0;
}