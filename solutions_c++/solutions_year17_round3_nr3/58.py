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

const int MAXN = 55;

int test;
int n, k;
double u, p[MAXN];

void init()
{
	scanf ("%d%d%lf", &n, &k, &u);
	for (int i = 1; i <= n; i++)
	{
		scanf ("%lf", &p[i]);
	}
}

void solve()
{
	init();
	sort(p + 1, p + n + 1);
	p[n + 1] = 1.0;
	for (int i = 1; i <= n && u > EPS; i++)
	{
		double d = min(p[i + 1] - p[i], u / i);
		//printf("%.3lf\n", d);
		for (int j = 1; j <= i; j++)
		{
			p[j] += d;
			u -= d;
		}
	}
	double ans = 1.0;
	for (int i = 1; i <= n; i++)
	{
		ans *= p[i];
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