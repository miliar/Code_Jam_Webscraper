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

const int MAXM = 4;
const int MAXN = 105;

int n, p;
int cnt[MAXM];
int dp[MAXN][MAXN][MAXN][MAXN];

void init()
{
	scanf ("%d%d", &n, &p);
	memset(cnt, 0, sizeof(cnt));
	for (int i = 1; i <= n; i++)
	{
		int q; scanf ("%d", &q);
		cnt[q % p]++;
	}
}

inline int get_sum(int c[])
{
	int res = 0;
	for (int i = 0; i < p; i++)
	{
		res += c[i] * i;
	}
	return res % p;
}

int calc_dp(int c[])
{
	int* st = &dp[c[0]][c[1]][c[2]][c[3]];
	if ((*st) != -1)
	{
		return *st;
	}
	*st = 0;
	for (int i = 0; i < p; i++)
	{
		if (c[i])
		{
			c[i]--;
			int sum = get_sum(c);
			int res = calc_dp(c);
			c[i]++;
			if (!sum)
			{
				res++;
			}
			*st = max(*st, res);
		}
	}
	//printf("%d %d %d   %d\n", c[0], c[1], c[2], *st);
	return *st;
}

void solve()
{
	init();
	memset(dp, -1, sizeof(dp));
	dp[0][0][0][0] = 0;
	printf("Case #%d: %d\n", test, calc_dp(cnt));
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