
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <cmath>
#include <iomanip>

#define M_PI       3.14159265358979323846

using namespace std;

int main(void)
{
	int t, n, k;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i)
	{
		cin >> n >> k;  // read n and then m.
		multimap<int, int, greater<int>> rMap;
		int R, H;
		for (int j = 0; j < n; ++j)
		{
			cin >> R >> H;
			rMap.insert(make_pair(R, H));
		}
		vector<pair<int, int>> sorted;
		multimap<int, int>::iterator it = rMap.begin();
		for (int j = 0; j < n; ++j, ++it)
		{
			sorted.push_back(*it);
		}
		vector<vector<long long>> dp(n + 1, vector<long long>(k + 1, 0));
		for (int j = 1; j < n + 1; ++j)
		{
			for (int l = 1; l < k + 1; ++l)
			{
				if (j < l)
				{
					break;
				}
				if (l == 1)
				{
					long long tmp = pow(sorted[j - 1].first, 2) + (long long)2 * sorted[j - 1].first * sorted[j - 1].second;
					dp[j][l] = max(dp[j - 1][l], tmp);
				}
				else
				{
					long long tmp = (long long)2 * sorted[j - 1].first * sorted[j - 1].second;
					dp[j][l] = max(dp[j - 1][l], dp[j - 1][l - 1] + tmp);
				}
			}
		}
		cout << "Case #" << i << ": " << setiosflags(ios::fixed) << setprecision(9) << (double)dp[n][k] * M_PI << endl;
	}
	//system("pause");

	return 0;
}