#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <numeric>
#include <cctype>
#include <bitset>
#include <cassert>

using namespace std;
#define ll long long
# define M_PI 3.14159265358979323846

bool func(pair<double, double> a, pair<double, double> b)
{
	if (a.first != b.first)
		return a.first < b.first;
	else
		return a.second < b.second;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		int n, k;
		cin >> n >> k;
		vector<pair<double, double> > vals(n);
		for (int i = 0; i < n; i++)
			cin >> vals[i].first >> vals[i].second;
		sort(vals.begin(), vals.end(), func);
		ll total = (1 << n);
		double max_ans = 0;
		for (ll i = 0; i < total; i++)
		{
			int cnt = 0;
			vector<pair<double, double> > temp;
			for (int j = 0; j < n; j++)
			{
				if (i&(1 << j))
				{
					cnt++;
					temp.push_back(vals[j]);
				}
			}
			if (cnt != k)
				continue;
			double ans = M_PI * temp[0].first * temp[0].first + 2 * M_PI*temp[0].first*temp[0].second;
			double prevSurface = M_PI * temp[0].first * temp[0].first;
			for (int j = 1; j < temp.size(); j++)
			{
				double area = M_PI*temp[j].first*temp[j].first;
				ans += area - prevSurface;
				ans += 2 * M_PI * temp[j].first*temp[j].second;
				prevSurface = area;
			}
			max_ans = max(max_ans, ans);
		}
		printf("Case #%d: %.9f\n", cases, max_ans);
	}
	
	return 0;

}