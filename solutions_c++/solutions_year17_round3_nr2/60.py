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

const int MAXT = 1440;

int test;
int dp[MAXT + 1][MAXT][2][2];
int n, m;
vector <pii> vn, vm;
bool bn[MAXT + 1], bm[MAXT + 1];

void init()
{
	scanf ("%d%d", &n, &m);
	vn.clear();
	vm.clear();
	for (int i = 1; i <= n; i++)
	{
		pii p; scanf ("%d%d", &p.first, &p.second);
		vn.push_back(p);
	}
	for (int i = 1; i <= m; i++)
	{
		pii p; scanf ("%d%d", &p.first, &p.second);
		vm.push_back(p);
	}
	sort(vn.begin(), vn.end());
	sort(vm.begin(), vm.end());
}

void solve()
{
	init();
	memset(bn, 0, sizeof(bn));
	for (int i = 0; i < (int)vn.size(); i++)
	{
		for (int j = vn[i].first + 1; j <= vn[i].second; j++)
		{
			bn[j] = true;
		}
	}
	memset(bm, 0, sizeof(bm));
	for (int i = 0; i < (int)vm.size(); i++)
	{
		for (int j = vm[i].first + 1; j <= vm[i].second; j++)
		{
			bm[j] = true;
		}
	}
	memset(dp, 63, sizeof(dp));
	dp[0][0][0][0] = dp[0][0][1][1] = 0;
	for (int i = 1; i <= MAXT; i++)
	{
		for (int j = 0; j <= min(i, MAXT / 2); j++)
		{
			if (j > 0 && !bn[i])
			{
				for (int h = 0; h < 2; h++)
				{
					if (i == MAXT && h == 1)
					{
						continue;
					}
					dp[i][j][h][0] = min(dp[i - 1][j - 1][h][0], dp[i - 1][j - 1][h][1] + 1);
				}
			}
			if (j < i && !bm[i])
			{
				for (int h = 0; h < 2; h++)
				{
					if (i == MAXT && h == 0)
					{
						continue;
					}
					dp[i][j][h][1] = min(dp[i - 1][j][h][0] + 1, dp[i - 1][j][h][1]);
				}
			}
			//printf("%d-%d ", dp[i][j][0], dp[i][j][1]);
		}
		//printf("\n");
	}
	int ans = min(dp[MAXT][MAXT / 2][0][0], dp[MAXT][MAXT / 2][1][1]);
	printf("Case #%d: %d\n", test, ans);
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