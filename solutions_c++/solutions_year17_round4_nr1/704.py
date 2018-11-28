
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

//solution for Problem A
//small+large
int main(void)
{
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		int n, p;
		cin >> n >> p;
		vector<int>g;
		map<int, int>dict;
		for (int i = 0; i < n; ++i)
		{
			int gg;
			cin >> gg;
			g.push_back(gg % p);
			dict[gg % p]++;
		}
		int ans = -1;
		if (p == 2)
		{
			ans = dict[0] + (dict[1] + 1) / 2;
		}
		else if (p == 3)
		{
			ans = dict[0];
			int par = min(dict[1], dict[2]);
			dict[1] -= par; dict[2] -= par;
			ans += par;
			int lef = max(dict[1], dict[2]);
			ans += (lef + 2) / 3;
		}
		else//p == 4
		{
			ans = dict[0];
			//(1,3)
			int par = min(dict[1], dict[3]);
			dict[1] -= par; dict[3] -= par;
			ans += par;
			int lef = max(dict[1], dict[3]);
			while (dict[2] > 0 && lef > 1)
			{
				lef -= 2;
				dict[2]--;
				ans++;
			}
			if (dict[2] > 1)
			{
				dict[2] -= 2;
				ans++;
			}
			if (lef > 3)
			{
				lef -= 4;
				ans++;
			}
			if (lef || dict[2])
			{
				ans++;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
