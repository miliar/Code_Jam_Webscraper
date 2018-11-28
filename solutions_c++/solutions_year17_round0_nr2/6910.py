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
	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		string n;
		cin >> n;
		string ans = "";
		bool check = false;
		while (!check)
		{
			check = true;
			for (int i = 1; i < n.length(); i++)
			{
				if (n[i] < n[i - 1])
				{
					n[i - 1]--;
					for (int j = i; j < n.length(); j++)
					{
						n[j] = '9';
					}
					check = false;
				}
			}
		}
		int i = 0;
		while (n[i] == '0')
			i++;
		
		for (; i < n.length(); i++)
			ans += n[i];
		
		cout << "Case #" << cases << ": " << ans << "\n";
	}
	return 0;
}