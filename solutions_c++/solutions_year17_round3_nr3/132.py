
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
#include <cassert>
using namespace std;

using LD = long double;

//Solution for Small dataset 1
int main(void)
{
	int T;
	cin >> T;
	cout << fixed;
	cout.precision(20);
	for (int test = 0; test < T; ++test)
	{
		int n, k;
		cin >> n >> k;
		assert(n == k);
		LD u;
		cin >> u;
		vector<LD>prob;
		LD last = 1.;
		int sink = n - 1;//バグ？
		for (int i = 0; i < n; ++i)
		{
			LD p;
			cin >> p;
			prob.push_back(p);
		}
		sort(prob.begin(), prob.end());
		prob.push_back(1.);
		for (int i = 0; i < n; ++i)
		{
			LD diff = prob[i + 1] - prob[i];
			LD cap = diff * (i + 1);
			if (cap < u)
			{
				u -= cap;
			}
			else
			{
				last = u / (i + 1) + prob[i];
				sink = i;
				break;
			}
		}
		LD ans = 1.;
		for (int i = 0; i <= sink; ++i)
		{
			ans *= last;
		}
		for (int i = sink + 1; i < n; ++i)
		{
			ans *= prob[i];
		}
		cout << "Case #" << test + 1 << ": " << ans << endl;
	}
	return 0;
}
