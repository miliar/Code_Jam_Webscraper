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
#define ll long long

int main()
{
	freopen("B-small-attempt6.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		int ac, aj;
		cin >> ac >> aj;
		vector<pair<int,int> > v1(2), v2(2);
		for (int i = 0; i < ac; i++)
		{
			cin >> v1[i].first >> v1[i].second;
		}
		for (int i = 0; i < aj; i++)
		{
			cin >> v2[i].first >> v2[i].second;
		}

		if (ac == 2 || aj == 2)
		{
			if (ac == 2)
			{
				int s1, f1, s2, f2;
				s1 = min(v1[0].first, v1[1].first);
				s2 = max(v1[0].first, v1[1].first);
				f1 = min(v1[0].second, v1[1].second);
				f2 = max(v1[0].second, v1[1].second);
				if ((f2 - s1 <= 720) || (1440 - s2 + f1 <= 720))
					printf("Case #%d: 2\n", cases);
				else
					printf("Case #%d: 4\n", cases);
			}
			else
			{
				int s1, f1, s2, f2;
				s1 = min(v2[0].first, v2[1].first);
				s2 = max(v2[0].first, v2[1].first);
				f1 = min(v2[0].second, v2[1].second);
				f2 = max(v2[0].second, v2[1].second);
				if ((f2 - s1 <= 720) || (1440 - s2 + f1 <= 720))
					printf("Case #%d: 2\n", cases);
				else
					printf("Case #%d: 4\n", cases);
			}
		}
		else
			printf("Case #%d: 2\n", cases);
	}
	
	return 0;

}