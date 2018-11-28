
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

//Solution for Problem B
//small+large

vector<int>col;
//dep回で満遍なく配ることができるか？
//駄目な場合：-1　いい場合：promoteする最小回数
int cond(int dep)
{
	vector<int>tmp = col;
	int n = tmp.size();
	int ret = 0;
	for (int i = 0; i < n; ++i)
	{
		while (tmp[i] > dep)
		{
			bool slot = false;
			//後ろに見ていく
			for (int j = i - 1; j >= 0; --j)
			{
				if (tmp[j] < dep)
				{
					tmp[j]++;
					tmp[i]--;
					ret++;
					slot = true;
					break;
				}
			}
			if (!slot)
			{
				return -1;
			}
		}
	}
	return ret;
}

int main(void)
{
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		int n, c, m;
		cin >> n >> c >> m;
		col.clear();
		col.resize(n);
		map<int, int>gec;
		for (int i = 0; i < m; ++i)
		{
			int p, b;
			cin >> p >> b;
			--p; --b;
			col[p]++;
			gec[b]++;
		}
		int ans = 0;
		for (int i = 0; i < c; ++i)
		{
			ans = max(ans, gec[i]);
		}
		int lo = ans - 1, hi = m;
		int second = -1;
		while (lo + 1 < hi)
		{
			int md = (lo + hi) / 2;
			int ret = cond(md);
			if (ret < 0)
			{
				lo = md;
			}
			else
			{
				second = ret;
				hi = md;
			}
		}
		if (second == -1)
		{
			second = cond(hi);
		}
		cout << "Case #" << t << ": " << hi << " " << second << endl;
	}
	return 0;
}
