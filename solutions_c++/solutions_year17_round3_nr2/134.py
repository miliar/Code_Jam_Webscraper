
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

struct range
{
	int st, en;
	int per;
};

int main(void)
{
	int T;
	cin >> T;
	for (int test = 0; test < T; ++test)
	{
		int ac, aj;
		cin >> ac >> aj;
		vector<range>sch;
		for (int i = 0; i < ac; ++i)
		{
			int c, d;
			cin >> c >> d;
			sch.push_back({ c,d,0 });
		}
		for (int i = 0; i < aj; ++i)
		{
			int j, k;
			cin >> j >> k;
			sch.push_back({ j,k,1 });
		}
		sort(sch.begin(), sch.end(), [](const range& r1, const range& r2) {return r1.st < r2.st; });
		int num = sch.size();
		vector<int>gap[2];
		int ans = 0;
		int tim[2] = {};
		for (int i = 0; i < num; ++i)
		{
			tim[!sch[i].per] += sch[i].en - sch[i].st;
		}
		for (int i = 0; i < num; ++i)
		{
			int j = (i + 1) % num;
			int ran = sch[j].st - sch[i].en;
			if (ran < 0)ran += 24 * 60;
			if (sch[j].per != sch[i].per)
			{
				//増えない
				ans++;
			}
			else
			{
				//増える
				gap[!sch[i].per].push_back(ran);
			}
		}
		sort(gap[0].rbegin(), gap[0].rend());
		sort(gap[1].rbegin(), gap[1].rend());
		for (int x = 0; x < 2; ++x)
		{
			while (!gap[x].empty() && tim[x] + gap[x].back() <= 720)
			{
				tim[x] += gap[x].back();
				gap[x].pop_back();
			}
			ans += gap[x].size() * 2;
		}
		cout << "Case #" << test + 1 << ": " << ans << endl;
	}
	return 0;
}
