#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef long long ll;
typedef vector <ll> vl;
typedef vector <pair <ll, ll>> vll;

const int inf = 5000;

int dp[2][2000][2000];
bool b0[2000], b1[2000];

void solve(int nn)
{
	int n, m;
	int temp1, temp2;
	fill(b0, b0 + 2000, true);
	fill(b1, b1 + 2000, true);
	for (int i = 0; i < 2000; i++)
	{
		for (int j = 0; j < 2000; j++)
		{
			dp[0][i][j] = inf;
			dp[1][i][j] = inf;

		}
	}
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> temp1 >> temp2;
		for (int j = temp1; j < temp2; j++)
			b0[j] = false;
	}

	for (int i = 0; i < m; i++)
	{
		cin >> temp1 >> temp2;
		for (int j = temp1; j < temp2; j++)
			b1[j] = false;
	}

	int ans = inf;

	if (b0[0])
	{
		dp[0][0][1] = 0;
		for (int i = 1; i <= 24 * 60; i++)
		{
			for (int j = 0; j <= 24 * 60; j++)
			{
				if (b0[i])
					dp[0][i][j + 1] = min(dp[0][i - 1][j], dp[1][i - 1][j] + 1);
				if (b1[i])
					dp[1][i][j] = min(dp[1][i - 1][j], dp[0][i - 1][j] + 1);
			}
		}
		ans = min(ans, min(dp[0][24 * 60 - 1][720], dp[1][24 * 60 - 1][720] + 1));
		for (int i = 0; i < 2000; i++)
		{
			for (int j = 0; j < 2000; j++)
			{
				dp[0][i][j] = inf;
				dp[1][i][j] = inf;

			}
		}
	}

	if (b1[0])
	{
		dp[1][0][0] = 0;
		for (int i = 1; i <= 24 * 60; i++)
		{
			for (int j = 0; j <= 24 * 60; j++)
			{
				if (b0[i])
					dp[0][i][j + 1] = min(dp[0][i - 1][j], dp[1][i - 1][j] + 1);
				if (b1[i])
					dp[1][i][j] = min(dp[1][i - 1][j], dp[0][i - 1][j] + 1);
			}
		}
		ans = min(ans, min(dp[0][24 * 60 - 1][720] + 1, dp[1][24 * 60 - 1][720]));
	}


	cout << "Case #" << nn + 1 << ": " << ans;
	cout << endl;
	return;

}

int main()
{
	ios::sync_with_stdio(false);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		solve(i);
	return 0;
}