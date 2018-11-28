#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;
set<char> used;

bool check(int l, int r, int row, vector<string>&v)
{
	for (int i = l; i <= r; ++i)
	{
		if (v[row][i] != '?')
			return false;
	}
}

void fill(int i, int j, vector<string> & v)
{
	char c = v[i][j];
	int l = j, r = j;
	while (l > 0)
	{
		if (v[i][l - 1] == '?')
			l--;
		else
			break;
	}
	while (r < v[i].size() - 1)
	{
		if (v[i][r + 1] == '?')
			r++;
		else
			break;
	}
	int u = i, d = i;
	while (u > 0)
	{
		if (check(l, r, u - 1, v))
			u--;
		else
			break;
	}

	while (d < v.size() - 1)
	{
		if (check(l, r, d + 1, v))
			d++;
		else
			break;
	}
	for (int i = u; i <= d; ++i)
	{
		for (int j = l; j <= r; ++j)
		{
			v[i][j] = c;
		}
	}
	used.insert(c);
}

int main() {
#ifdef _CONSOLE
	freopen("A-large (3).in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		used.clear();
		int n, m;
		cin >> n >> m;
		vector<string> v(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i];
		}

		
		for (int i = 0; i < v.size(); ++i)
		{
			for (int j = 0; j < v[i].size(); ++j)
			{
				if (v[i][j] != '?' && used.find(v[i][j]) == used.end())
				{
					fill(i, j, v);
				}
			}
		}
		printf("Case #%d:\n", t);
		for (int i = 0; i < v.size(); ++i)
		{
			cout << v[i] << "\n";
		}

			
	}

	return 0;
}