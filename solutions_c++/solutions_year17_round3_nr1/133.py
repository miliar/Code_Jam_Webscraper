
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <unordered_set>
#include <unordered_map>
using namespace std;

using LL = long long;

using FL = long double;

const FL PI = acos(-1);

int main(void)
{
	int t;
	cin >> t;
	cout << fixed;
	cout.precision(20);
	for (int test = 0; test < t; ++test)
	{
		int n, k;
		cin >> n >> k;
		vector<pair<LL, LL>>pank;
		for (int i = 0; i < n; ++i)
		{
			int rr, hh;
			cin >> rr >> hh;
			pank.push_back({ rr,hh });
		}
		sort(pank.begin(), pank.end());
		priority_queue<LL, vector<LL>, greater<LL>>que;
		LL sidesum = 0;
		for (int i = 0; i < k; ++i)
		{
			LL side = 2 * pank[i].first * pank[i].second;
			que.push(side);
			sidesum += side;
		}
		FL ans = sidesum * PI + pank[k - 1].first * pank[k - 1].first * PI;
		for (int i = k; i < n; ++i)
		{
			FL bottom = pank[i].first * pank[i].first * PI;
			LL disc = que.top();
			que.pop(); sidesum -= disc;
			LL side = 2 * pank[i].first * pank[i].second;
			que.push(side);
			sidesum += side;
			ans = max(ans, sidesum * PI + bottom);
		}
		cout << "Case #" << test + 1 << ": " << ans << endl;
	}
	return 0;
}
