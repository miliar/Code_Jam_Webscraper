#pragma comment(linker, "/STACK:268435456")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <queue>
#include <iomanip>
#include <assert.h>
#include <stack>
#include <deque>
#include <limits.h>
#include <memory.h>
#include <time.h>
//#include <unordered_map>
//#include <unordered_set>
using namespace std;

void prepare(string q)
{
#ifdef _DEBUG
	//system("color F0");
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
#else
	if (q.size() != 0)
	{
		freopen((q + ".in").c_str(), "r", stdin);
		freopen((q + ".out").c_str(), "w", stdout);
	}
#endif
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	cin.tie(false);
}

void solve()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		string s;
		cin >> s;
		bool ka = false;;
		while (!ka)
		{
			bool ki = false;
			for (int i = 1; i < s.size(); ++i)
			{
				if (!ki)
				{
					if (s[i] < s[i - 1])
					{
						ki = true;
						--s[i - 1];
						--i;
					}
				}
				else
				{
					s[i] = '9';
				}

			}

			ki = false;
			for (int k = 1; k < s.size(); ++k)
				if (s[k] < s[k - 1])
					ki = true;
			if (!ki)
				ka = true;
		}
		reverse(s.begin(), s.end());
		while (s.size()>1 && s.back() == '0')
		{
			s.pop_back();
		}
		reverse(s.begin(), s.end());


		cout << "Case #" << tt << ": " << s << endl;
	}
}

int main()
{
	prepare("");
	solve();
	return 0;
}