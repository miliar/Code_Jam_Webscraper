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

pair<long double, long double> arr[1001];
long double dp[1001][1001];

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
		for (int i = 0; i < N; i++)
			cin >> arr[i].first >> arr[i].second;
		sort(arr, arr + N, greater<pair<long double, long double>>());
		for (int i = 0; i < N; i++)
			for (int j = 0; j < K; j++)
				dp[i][j] = -1;
		dp[0][0] = 0;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < K; j++)
				if (dp[i][j] != -1)
				{
					if (dp[i][j] == 0)
					{
						dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j] + PI * sqr(arr[i].first) + arr[i].second * 2 * PI * arr[i].first);
						dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
					}
					else
					{
						dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j] + arr[i].second * 2 * PI * arr[i].first);
						dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
					}
				}
		long double best = 0;
		for (int i = 1; i <= N; i++)
			best = max(dp[i][K], best);
		printf("%.10f", best);
		cout << endl;
	}
}