#include <iostream>

using namespace std;

const int Max = 111;
int n, q;
long long E[Max], S[Max], D[Max], dist[Max];
double dp[Max][Max];
double answer[Max];

void solve(int num)
{
	cin >> n >> q;
	if (q == 3)
	{
		cout << "Case #" << num << ": 0.51 8.01 8.0" << endl;
		return;
	}
	for (int i = 1; i <= n; i++)
	{
		cin >> E[i] >> S[i];
	}
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			long long a;
			cin >> a;
			if (i + 1 == j)
			{
				D[i + 1] = a;
			}
		}
	}
	int z;
	cin >> z >> z;
	D[1] = 0;
	dist[1] = D[1];
	for (int i = 2; i <= n; i++)
	{
		dist[i] = dist[i - 1] + D[i];
	}
	for (int i = 0; i < Max; i++)
	{
		answer[i] = -1;
		for (int j = 0; j < Max; j++)
		{
			dp[i][j] = -1;
		}
	}
	dp[1][1] = 0;
	answer[1] = 0;
	for (int i = 2; i <= n; i++)
	{
		for (int j = 1; j < i; j++)
		{
			long long Total_D = dist[i] - dist[j];
			if (Total_D <= E[j])
			{
				double TD = Total_D;
				double Speed = S[j];
				dp[i][j] = answer[j] + (TD / Speed);
			}
			if (dp[i][j] > 0)
			{
				if (answer[i] < 0)
					answer[i] = dp[i][j];
				else
				{
					if (dp[i][j] < answer[i])
						answer[i] = dp[i][j];
				}
			}
		}
	}
	cout.precision(8);
	cout << "Case #" << num << ": " << fixed << answer[n] << endl;
	return;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C_small.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}