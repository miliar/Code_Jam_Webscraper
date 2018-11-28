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

const int MAXN = 1005;

struct pancake
{
	int r, h;
	double c;

	bool operator < (const pancake &oth) const
	{
		return r < oth.r;
	}
};

int test;
double dp[MAXN][MAXN][2];
int n, k;
pancake p[MAXN];

void init()
{
	scanf ("%d%d", &n, &k);
	for (int i = 1; i <= n; i++)
	{
		scanf ("%d%d", &p[i].r, &p[i].h);
	}
}

void solve()
{
	init();
	for (int i = 1; i <= n; i++)
	{
		p[i].c = 2.0 * M_PI * p[i].r * p[i].h;
	}
	sort(p + 1, p + n + 1);
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			dp[i][j][1] = dp[i - 1][j - 1][0] + p[i].c;
			dp[i][j][0] = max(dp[i][j][1], dp[i - 1][j][0]);
		}
	}
	double ans = 0.0;
	for (int i = k; i <= n; i++)
	{
		ans = max(dp[i][k][1] + M_PI * p[i].r * p[i].r, ans);
	}
	printf("Case #%d: %.10lf\n", test, ans);
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