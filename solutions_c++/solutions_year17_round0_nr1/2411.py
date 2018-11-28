#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <tuple>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <unordered_map>
#include <unordered_set>

using namespace std;







int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int qqq;
	cin >> qqq;
	for (int qq = 1; qq <= qqq; qq++)
	{
		cout << "Case #" << qq << ": ";
		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans = 0;
		for (int i = 0; (i + k) <= s.length(); i++)
		{
			if (s[i] == '-')
			{
				ans++;
				for (int j = i; j < i + k; j++)
				{
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';

				}
			}
		}
		int flag = 0;
		for (int i = 0; i < s.length(); i++)
		{
			if (s[i] == '-')
				flag = 1;
		}
		if (flag == 0)
		{
			cout << ans << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}

	}
	return 0;
}