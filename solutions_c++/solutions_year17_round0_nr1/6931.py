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


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t, k;
	string pancakes;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		cin >> pancakes >> k;
		bool impossible = false;
		vector<int> flips(1+pancakes.length(), 0);
		int flipsum = 0;
		int ans = 0;
		for (int i = 0; i < pancakes.length(); i++)
		{
			flipsum += flips[i];
			if ((pancakes[i] == '+' && flipsum % 2 != 0) || (pancakes[i]=='-' && flipsum%2==0))
			{
				if (i + k <= pancakes.length())
				{
					flips[i]++;
					flipsum++;
					flips[i + k]--;
					ans++;
				}
				else
				{
					impossible = true;
					break;
				}
			}
		}
		if(impossible)
			cout << "Case #" << cases << ": IMPOSSIBLE" << "\n";
		else
			cout << "Case #" << cases << ": " << ans << "\n";
	}
	return 0;
}