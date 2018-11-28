#include <iostream>

using namespace std;


typedef pair<int, int> pii;

const int DAYMIN = 24 * 60;
const int MAXAL = 720;
const int MAXN = 210;

pii a[MAXN], b[MAXN];
int tsk[DAYMIN + 10];

int dp[DAYMIN + 10][MAXAL + 10][2];

int main()
{
	int tt;
	cin >> tt;
	for (int tc = 1; tc <= tt; tc++)
	{
		int n, m;
		cin >> n >> m;
		int mn = DAYMIN;
		for (int i = 0; i < n; i++)
		{
			cin >> a[i].first >> a[i].second;
			mn = min(a[i].first, mn);
		}
		for (int i = 0; i < m; i++)
		{
			cin >> b[i].first >> b[i].second;
			mn = min(b[i].first, mn);
		}
		for (int i = 0; i < DAYMIN; i++)
			tsk[i] = 0;
		for (int i = 0; i < n; i++)
			for (int j = a[i].first; j < a[i].second; j++)
				tsk[j - mn] = 1;
		for (int i = 0; i < m; i++)
			for (int j = b[i].first; j < b[i].second; j++)
				tsk[j - mn] = 2;
		for (int j = 0; j <= MAXAL; j++)
			dp[0][j][0] = dp[0][j][1] = DAYMIN;
		if (tsk[0] == 1)
			dp[0][0][1] = 0;
		else
			dp[0][1][0] = 0;
		for (int i = 1; i < DAYMIN; i++)
			for (int j = 0; j <= MAXAL; j++)
			{
				dp[i][j][0] = dp[i][j][1] = DAYMIN;
				if (tsk[i] == 0 || tsk[i] == 2)
				{
					if (j > 0)
					{
						dp[i][j][0] = min(dp[i][j][0], dp[i - 1][j - 1][0]);
						dp[i][j][0] = min(dp[i][j][0], dp[i - 1][j - 1][1] + 1);
					}
				}
				if (tsk[i] == 0 || tsk[i] == 1)
				{
					dp[i][j][1] = min(dp[i][j][1], dp[i - 1][j][1]);
					dp[i][j][1] = min(dp[i][j][1], dp[i - 1][j][0] + 1);
				}
			}
		cout << "Case #" << tc << ": ";
		if (tsk[0] == 1)
			cout << min(dp[DAYMIN - 1][MAXAL][0] + 1, dp[DAYMIN - 1][MAXAL][1]) << "\n";
		else
			cout << min(dp[DAYMIN - 1][MAXAL][0], dp[DAYMIN - 1][MAXAL][1] + 1) << "\n";

	}
}
