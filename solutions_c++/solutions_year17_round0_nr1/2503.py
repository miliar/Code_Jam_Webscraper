#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FILE_NAME "A-large"

using namespace std;

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
	
	int numTestCaces = 0;
	cin >> numTestCaces;
	for(int Case = 1; Case <= numTestCaces; ++Case)
	{
		string s;
		int k;
		cin >> s >> k;
		int res = 0;
		for(int i = 0; i < s.size(); ++i)
		{
			if(s[i] == '-')
			{
				++res;
				if(i + k > s.size())
				{
					res = -1;
					break;
				}
				else
					for(int j = i; j < i + k; ++j)
						if(s[j] == '-')
							s[j] = '+';
						else
							s[j] = '-';
			}
		}
		cout << "Case #" << Case << ": ";
		if(res < 0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}

	return 0;
}
