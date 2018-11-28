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
#include <unordered_map>
#include <unordered_set>
using namespace std;

void prepare(string q)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	if (q.size() != 0)
	{
		freopen((q + ".in").c_str(), "r", stdin);
		freopen((q + ".out").c_str(), "w", stdout);
	}
#endif
	cin.sync_with_stdio(0);
	cout.sync_with_stdio(0);
	cin.tie(0);
}
int n, m;
vector <string> g;
bool ki;
bool us[256];

void rec(int x, int y)
{
	if (ki)
		return;
	if (y == m)
	{
		++x;
		y = 0;
	}
	if (x == n)
	{
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				if (g[i][j] == '?')
					return;
			}
		for (int i = 0; i < n; ++i)
			cout << g[i] << endl;
		ki = true;
		return;
	}
	if (g[x][y] == '?')
	{
		for (int a = 0; a <= x; ++a)
			for (int b = 0; b <= y; ++b)
				for (int d = x + 1; d <= n; ++d)
					for (int e = y + 1; e <= m; ++e)
					{
						char c = '#';
						int _x, _y;
						bool ka = false;

						for (int k = a; k < d; ++k)
							for (int l = b; l < e; ++l)
							{
								if (c != '#' && g[k][l] != '?')
									ka = true;
								if (c == '#' && g[k][l] != '?')
								{
									c = g[k][l];
									_x = k;
									_y = l;

								}
							}

						if (!ka && c != '#' && !us[c])
						{
							us[c] = true;
							for (int k = a; k < d; ++k)
								for (int l = b; l < e; ++l)
								{
									g[k][l] = c;
								}
							rec(x, y + 1);
							for (int k = a; k < d; ++k)
								for (int l = b; l < e; ++l)
								{
									if (_x == k && _y == l) continue;
									g[k][l] = '?';
								}
							us[c] = false;
						}

					}
	}
	else
	{
		rec(x, y + 1);
	}
}

void solve()
{
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		cout << "Case #" << test << ":\n";
		cin >> n >> m;
		g.resize(n);
		memset(us, 0, sizeof(us));
		ki = false;
		for (int i = 0; i < n; ++i)
			cin >> g[i];
		rec(0, 0);

		
		
	}
}

int main()
{
	prepare("");
	solve();
	return 0;
}