#include <iostream>
#include <cmath>
#include <vector>
#include <sstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <iomanip>

# define M_PI           3.14159265358979323846 

using namespace std;

double dp[1001][1001];

double solve(vector<pair<double, double> >& v, int _i, int K, int& _total)
{
	if (K == 0)
		return 0;

	if (_i >= (int)v.size())
	{
		return -10000;
	}

	if (dp[_i][K] != -1)
		return dp[_i][K];

	double temp = 0;
	if (K == _total)
		temp = M_PI * v[_i].first * v[_i].first;

	double res = 2 * M_PI * v[_i].first * v[_i].second + temp + solve(v, _i + 1, K - 1, _total);
	
	res = max(res, solve(v, _i + 1, K, _total));

	dp[_i][K] = res;

	return res;
}

int main(int argc, char* argv[])
{
	freopen("in.txt", "r+", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		int N, K;
		cin >> N >> K;

		for (int i = 0; i < 1001; ++i)
		{
			for (int j = 0; j < 1001; ++j)
				dp[i][j] = -1;
		}

		vector<pair<double, double> > rhv;

		for (int i = 0; i < N; ++i)
		{
			double r, h;
			cin >> r >> h;
			rhv.push_back(make_pair(r, h));
		}

		sort(rhv.rbegin(), rhv.rend(), [](auto &left, auto &right) {
			return left.first < right.first;
		});

		double res = solve(rhv, 0, K, K);

		cout << "Case #" << (t + 1) << ": " << fixed << setprecision(9) << res << endl;
	}

	return 0;
}