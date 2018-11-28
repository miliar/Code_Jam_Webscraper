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

const int MAXN = 1005;

int n, c, m;
pii p[MAXN];
int mx[MAXN];
bool was[MAXN][MAXN];
bool used[MAXN];
int cnt[MAXN][MAXN];

void init()
{
	scanf ("%d%d%d", &n, &c, &m);
	for (int i = 1; i <= m;i++)
	{
		scanf ("%d%d", &p[i].first, &p[i].second);
	}
}

bool check(int cnt)
{
	memset(was, 0, sizeof(was));
	memset(used, 0, sizeof(used));
	int all = 0;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= cnt; j++)
		{
			for (int h = 1; h <= m; h++)
			{
				if (used[h])
				{
					continue;
				}
				if (p[h].first < i)
				{
					return false;
				}
				if (was[j][p[h].second])
				{
					continue;
				}
				++all;
				used[h] = true;
				was[j][p[h].second] = true;
				break;
			}
		}
	}
	return all == m;
}

void solve()
{
	init();
	sort(p + 1, p + m + 1);
	int mn = 0;
	memset(mx, 0, sizeof(mx));
	memset(cnt, 0, sizeof(cnt));
	for (int i = 1; i <= m; i++)
	{
		mn = max(mn, ++mx[p[i].second]);
		cnt[p[i].second][p[i].first]++;
	}
	int rides = mn;
	int all = 0;
	for (int i = 1; i < MAXN; i++)
	{
		for (int j = 1; j <= c; j++)
		{
			all += cnt[j][i];
		}
		rides = max(rides, (all + i - 1) / i);
	}
	int prom = 0;
	for (int i = 2; i < MAXN; i++)
	{
		int cn = 0;
		for (int j = 1; j <= c; j++)
		{
			cn += cnt[j][i];
		}
		prom += max(0, cn - rides);
	}
	printf("Case #%d: %d %d\n", test, rides, prom);
	/*int l = mn, r = 1000, cnt = -1;
	while (l <= r)
	{
		int mid = (l + r) >> 1;
		if (check(mid))
		{
			cnt = mid;
			r = mid - 1;
		}
		else
		{
			l = mid + 1;
		}
	}*/
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