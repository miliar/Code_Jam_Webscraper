#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <list>
#include <map>
#include <algorithm>
#include <functional>
#include <climits>
#include <random>

using namespace std;

bool isValid(vector<string> &g, char c)
{
	int x1 = -1, y1 = -1, x2 = -1, y2 = -1;
	int cnt = 0;
	for (int i = 0; i < g.size(); i++)
	{
		for (int j = 0; j < g[i].size(); j++)
		{
			if (g[i][j] == c)
			{
				cnt++;

				if (x1 == -1 || x1 > j)
				{
					x1 = j;
				}
				
				if (x2 == -1 || x2 < j)
				{
					x2 = j;
				}

				if (y1 == -1 || y1 > i)
				{
					y1 = i;
				}
				
				
				if (y2 == -1 || y2 < i)
				{
					y2 = i;
				}
			}
		}
	}
	
	for (int i = y1; i <= y2; i++)
	{
		for (int j = x1; j <= x2; j++)
		{
			if (g[i][j] != c && g[i][j] != '?')
				return false;
		}
	}
	for (int i = y1; i <= y2; i++)
	{
		for (int j = x1; j <= x2; j++)
		{
			if (g[i][j] == '?')
				g[i][j] = c;
		}
	}

	return true;
}
void solve()
{
	int r, c;
	vector<string> g;
	string u;

	cin >> r >> c;
	for (int i = 0; i < r; i++)
	{
		string s;
		cin >> s;
		g.push_back(s);
		for (int j = 0; j < s.length(); j++)
		{
			if (s[j] != '?' && u.find(s[j]) == string::npos)
			{
				u += s[j];
			}
		}
	}
	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			if (g[i][j] == '?')
			{
				for (int k = 0; k < u.length(); k++)
				{
					g[i][j] = u[k];
					if (isValid(g, u[k]))
						break;
				}
			}
		}
	}
	for (int i = 0; i < r; i++)
	{
		cout << "\n";
		cout << g[i];
	}
}
int main()
{
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++)
	{
		cout << "Case #" << c << ": ";
		solve();
		cout << "\n";
	}
}