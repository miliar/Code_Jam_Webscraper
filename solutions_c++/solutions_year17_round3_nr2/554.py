#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <functional>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <cassert>

using namespace std;

#define sqr(x) ((x)*(x))

pair<pair<int, int>, int> arr[1001];
int dp[1450][740][2][2];
int pos[1450];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	long double PI = 3.141592653589;
	for (int T = 0; T < t; T++)
	{
		cout << "case #" << T + 1 << ": ";
		int N, K;
		cin >> N >> K;
		for (int i = 0; i <= 1440; i++)
			pos[i] = 0;
		int cnt = 0;
		for (int i = 0; i < N; i++)
		{
			cin >> arr[i].first.first >> arr[i].first.second;
			for (int j = arr[i].first.first + 1; j <= arr[i].first.second; j++)
			{
				pos[j] = 1;
				cnt++;
			}
		}
		for (int i = 0; i < K; i++)
		{
			cin >> arr[i].first.first >> arr[i].first.second;
			for (int j = arr[i].first.first + 1; j <= arr[i].first.second; j++)
			{
				pos[j] = 2;
				cnt++;
			}
		}

		for (int i = 0; i <= 1440; i++)
			for (int j = 0; j <= 720; j++)
				for (int cur = 0; cur < 2; cur++)
					for (int st = 0; st < 2; st++)
						dp[i][j][cur][st] = 200000;
		dp[0][0][0][0] = 0;
		dp[0][0][1][1] = 0;

		for (int i = 0; i < 1440; i++)
			for (int j = 0; j <= 720; j++)
				for (int cur = 0; cur < 2; cur++)
					for (int st = 0; st < 2; st++)
					{
						if (i + 1 != 1440)
						{
							if (pos[i + 1] != cur + 1)
								dp[i + 1][j + cur][cur][st] = min(dp[i + 1][j + cur][cur][st], dp[i][j][cur][st]);
							if (pos[i + 1] != !cur + 1)
								dp[i + 1][j + !cur][!cur][st] = min(dp[i + 1][j + !cur][!cur][st], dp[i][j][cur][st] + 1);
						}
						else
						{
							if (pos[i + 1] != cur + 1)
								dp[i + 1][j + cur][cur][st] = min(dp[i + 1][j + cur][cur][st], dp[i][j][cur][st] + (st != cur));
							if (pos[i + 1] != !cur + 1)
								dp[i + 1][j + !cur][!cur][st] = min(dp[i + 1][j + !cur][!cur][st], dp[i][j][cur][st] + 1 + (st != !cur));
						}
					}
		int best = 20000;
		for (int cur = 0; cur < 2; cur++)
			for (int st = 0; st < 2; st++)
				best = min(dp[1440][720][cur][st], best);
		cout << best;
		cout << endl;
	}
}