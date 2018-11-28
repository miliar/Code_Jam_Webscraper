#include <iostream>
#include <vector>
#include <array>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

array<array<double, 1001>, 1001> dp;

void print(int n)
{
  for(int i = 1; i <= n; i++)
  {
	for(int j = 1; j <= n; j++)
	{
	  cout << dp[i][j] << " ";
	}
	cout << endl;
  }
}


int main()
{
  cout << setprecision(12);
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
	for(auto &v : dp)
	{
	  fill(v.begin(), v.end(), 0);
	}

	int n, k;
	cin >> n >> k;
	vector<pair<double, double>> ps(n);
	
	for(int i = 0; i < n; i++)
	{
	  cin >> ps[i].first >> ps[i].second;
	}

	sort(ps.begin(), ps.end(), greater<pair<double, double>>());
	
	for(int i = 1; i <= n; i++)
	{
	  dp[i][1] = max(dp[i-1][1], M_PI * ps[i-1].first * ps[i-1].first + 2 * M_PI * ps[i-1].first * ps[i-1].second);
	}
	
	for(int j = 2; j <= k; j++)
	{
	  for(int i = 1; i <= n; i++)
	  {
		dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 2 * M_PI * ps[i-1].first * ps[i-1].second);
	  }
	}
	
	cout << "Case #" << t << ": " << dp[n][k] << endl;
  }
}
