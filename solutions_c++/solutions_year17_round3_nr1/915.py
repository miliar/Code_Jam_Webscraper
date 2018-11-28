#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

#define PI 3.14159265358979323846

using namespace std;

double Solve(int N, int K, vector<pair<long long, long long>>& rhs)
{
	sort(rhs.begin(), rhs.end());
	
	vector<vector<long long>> dp(K+1, vector<long long>(N));
	for (int i = 0; i < N; ++i)
	{
		dp[1][i] = 2 * rhs[i].first * rhs[i].second;
	}

	for (int i = 2; i <= K; ++i)
	{
		for (int j = i - 1; j < N; ++j)
		{
			for (int k = 0; k < j; ++k)
			{
				dp[i][j] = max(dp[i][j], dp[i - 1][k] + 2 * rhs[j].first * rhs[j].second);
			}
		}
	}

	for (int i = 0; i < N; ++i)
	{
		dp[K][i] += rhs[i].first * rhs[i].first;
	}

	return *max_element(dp[K].begin(), dp[K].end()) * PI;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		int N, K;
		scanf("%d %d", &N, &K);

		vector<pair<long long, long long>> rhs;
		for (int j = 0; j < N; ++j)
		{
			int R, H;
			scanf("%d %d", &R, &H);
			rhs.push_back(make_pair(R, H));
		}
		
		printf("Case #%d: %.9f\n", i, Solve(N, K, rhs));
	}
	
	return 0;
}
