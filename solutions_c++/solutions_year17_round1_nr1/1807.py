#define LARGE
//#define SMALL

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

int t, T, R, C, i, j, k, rs;
string s[25];
vector< pair<char, int> > v;


int main()
{
#if defined(LARGE)
    freopen("../A-large.in", "r", stdin);
    freopen("../A-large.out", "w", stdout);
#elif defined(SMALL)
    freopen("../A-small-attempt0.in", "r", stdin);
    freopen("../A-small.out", "w", stdout);
#else
    freopen("input.txt", "r", stdin);
#endif

    cin >> T;

    for(t = 0; t < T; ++t)
    {
		cin >> R >> C;
		for (i = 0; i < R; ++i)
		{
			cin >> s[i];
		}

		rs = -1;
		for (i = 0; i < R; ++i)
		{
			for (j = 0; j < C; ++j)
			{
				if (s[i][j] != '?')
				{
					rs = i;
					break;
				}
			}
			if (rs != -1)
			{
				break;
			}
		}

		for (i = rs; i < R; ++i)
		{
			v.clear();
			v.push_back(make_pair('?', 0));
			for (j = 0; j < C; ++j)
			{
				if (s[i][j] != '?')
				{
					v.push_back(make_pair(s[i][j], j));
				}
			}

			if (v.size() == 1)
			{
				s[i] = s[i - 1];
			}
			else
			{
				for (k = 1; k < v.size(); ++k)
				{
					for (j = v[k - 1].second; j < v[k].second; ++j)
					{
						if (s[i][j] == '?')
						{
							s[i][j] = v[k].first;
						}
					}
				}

				for (j = v[v.size() - 1].second; j < C; ++j)
				{
					if (s[i][j] == '?')
					{
						s[i][j] = v[v.size() - 1].first;
					}
				}
			}
		}
		for (i = 0; i < rs; ++i)
		{
			s[i] = s[rs];
		}


        cout << "Case #" << t+1 << ":\n";
		for (i = 0; i < R; ++i)
		{
			cout << s[i] << "\n";
		}
    }

    return 0;
}
