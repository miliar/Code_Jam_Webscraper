
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

//Solution A for small and large
int main(void)
{
	int t;
	cin >> t;
	for (int loop = 0; loop < t; ++loop)
	{
		string s; int k;
		cin >> s >> k;
		int n = s.length();
		int ans = 0;
		for (int i = 0; i <= n - k; ++i)
		{
			if (s[i] == '-')
			{
				++ans;
				for (int j = 0; j < k; ++j)
				{
					s[i + j] = ((s[i + j] == '-') ? '+' : '-');
				}
			}
		}
		for (int i = 0; i < n; ++i)
		{
			if (s[i] != '+')
			{
				ans = -1;
			}
		}
		cout << "Case #" << loop + 1 << ": ";
		if (~ans)cout << ans << endl;
		else cout << "IMPOSSIBLE\n";
	}
	return 0;
}
