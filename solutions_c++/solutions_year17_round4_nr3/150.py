#pragma comment(linker, "/STACK:256000000")

#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>
#include <assert.h>
#include <time.h>
#include <memory.h>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <algorithm>
#include <random>
#include <bitset>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;
const int INF = (int)(1e9+1e5);
const int64 LINF = (int64)(4e18);
const double EPS = 1e-9;
#define sq(x) ((x)*(x))
#define FAIL() (*(int*)(0))++
const int MOD = 1000000007;
const int BASE = 1000003;

int test;

const int MAXN = 55;

int n, m;
char s[MAXN][MAXN];
int num[MAXN][MAXN];
bool u[MAXN][MAXN];
int t[MAXN][MAXN];
vector <pii> c;
int l;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void init()
{
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; i++)
	{
		scanf ("%s", &s[i][1]);
	}
}

inline bool valid(int x, int y)
{
	return 1 <= x && x <= n && 1 <= y && y <= m && s[x][y] != '#';
}

void get_nums()
{
	memset(num, 0, sizeof(num));
	l = 0;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m;j++)
		{
			if (s[i][j] == '|' || s[i][j] == '-')
			{
				num[i][j] = ++l;
			}
		}
	}
}

void dfs(int x, int y)
{
	c.push_back(pii(x, y));
	u[x][y] = true;
	for (int i = 0; i < 4; i++)
	{
		int xx = x + dx[i];
		int yy = y + dy[i];
		if (valid(xx, yy) && !u[xx][yy])
		{
			dfs(xx, yy);
		}
	}
}

bool check_conn(char sy, int st, int en)
{
	for (int i = 0; i < (int)c.size(); i++)
	{
		int x = c[i].first;
		int y = c[i].second;
		t[x][y] = 0;
	}
	for (int i = 0; i < (int)c.size(); i++)
	{
		int x = c[i].first;
		int y = c[i].second;
		if (num[x][y])
		{
			int nu = num[x][y];
			s[x][y] = sy;
			if (t[x][y])
			{
				return false;
			}
			t[x][y] = nu;
			for (int j = st; j <= en; j++)
			{
				int xx = x, yy = y;
				while (true)
				{
					xx += dx[j];
					yy += dy[j];
					if (!valid(xx, yy))
					{
						break;
					}
					if (t[xx][yy])
					{
						return false;
					}
					t[xx][yy] = nu;
				}
			}
		}
	}
	for (int i = 0; i < (int)c.size(); i++)
	{
		int x = c[i].first, y = c[i].second;
		if (!t[x][y])
		{
			return false;
		}
	}
	return true;
}

bool check(int x0, int y0)
{
	c.clear();
	dfs(x0, y0);
	return check_conn('|', 0, 1) || check_conn('-', 2, 3);
}

void solve()
{
	init();
	get_nums();
	bool fail = false;
	memset(u, 0, sizeof(u));
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			if (s[i][j] != '#' && !u[i][j])
			{
				if (!check(i, j))
				{
					fail = true;
				}
			}
		}
	}
	printf("Case #%d: %s\n", test, (fail ? "IMPOSSIBLE" : "POSSIBLE"));
	if (!fail)
	{
		for (int i = 1; i <= n; i++)
		{
			printf("%s\n", s[i] +1);
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
#ifdef _MY_DEBUG
	freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
#else
#endif

	srand(333);
	int tests = 1; scanf ("%d", &tests);
	for (test = 1; test <= tests; test++)
	{
		solve();
	}

	return 0;
}