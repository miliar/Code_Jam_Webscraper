
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
using ll = long long;

//Solution B for small and large
int main(void)
{
	int t;
	cin >> t;
	for (int testcase = 0; testcase < t; ++testcase)
	{
		string n;
		cin >> n;
		reverse(n.begin(), n.end());
		int len = n.size();
		int dec = -1;
		bool tes = true;
		for (int i = len - 1; i > 0; --i)
		{
			if (n[i] > n[i - 1])
			{
				tes = false;
			}
		}
		for (int i = len - 1; i > 0; --i)
		{
			if (n[i] >= n[i - 1])
			{
				dec = i;
				break;
			}
		}
		if (!tes)
		{
			n[dec]--;
			for (int d = dec - 1; d >= 0; --d)
			{
				n[d] = '9';
			}
		}
		reverse(n.begin(), n.end());
		ll ans = stoll(n);
		cout << "Case #" << testcase + 1 << ": " << ans << endl;
	}
	return 0;
}
