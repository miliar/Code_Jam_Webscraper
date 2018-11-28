#pragma region Template
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <utility>
#include <stack>
#include <set>
#include <algorithm>
#include <bitset>
#include <functional>
#include <ctime>
#include <cassert>
#include <valarray>
#include <unordered_map>
#include <unordered_set>
#include <random>
#include <complex>
#include <regex>
#pragma comment(linker, "/STACK:167772160")

using namespace std;
#define mp make_pair
#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define print_var(x) cerr << #x << " : " << (x) << endl
#define print_array(arr, len) {cerr << #arr << " : "; for(int i = 0; i < len; ++i) cerr << arr[i] << ' '; cerr << endl;}
#define print_2d_array(arr, len1, len2) {cerr << #arr << endl; for(int i = 0; i < len1; ++i, cerr << endl) for(int j = 0; j < len2; ++j) cerr << arr[i][j] << ' ';}
#define print_iterable(i) {cerr << #i << " : "; for(auto e : i) cerr << e << ' '; cerr << endl;}
#define print_new_line() cerr << endl
#else
#define eprintf(...) (void)0
#define print_var(x) (void)0
#define print_array(arr, len) {}
#define print_2d_array(arr, len1, len2) {}
#define print_iterable(i) {}
#define print_new_line() (void)0
#endif

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<ll, ll> pll;

const int INF = (int)1e9 + 10;
const ll LINF = ll(2e18) + 10;
const double PI = acosl(-1);
const double eps = 1e-8;
const ld EPS = 1e-12;
#pragma endregion

#ifdef LOCAL
#define ERR_CATCH
#endif

#define MULTITEST
#define CASES

const int T = 1440;
const int MUST = T / 2;
bool busy[2][T];
int dp[2][MUST+1][2];
int tdp[MUST+1][2];

void relax(int& a, int b)
{
	a = min(a, b);
}

void calc_dp(int dp[MUST + 1][2])
{
	for (int ti = 0; ti < T; ++ti)
	{
		for (int i = 0; i <= MUST; ++i)
			for (int who : {0, 1})
				tdp[i][who] = INF;
		for (int i = 0; i <= MUST; ++i)
			for (int who : {0, 1})
			{
				if (!busy[who][ti] && i + 1 <= MUST)
					relax(tdp[i+1][who], dp[i][who]);
				if (!busy[!who][ti] && ti + 1 - i <= MUST && ti + 1 - i >= 0)
					relax(tdp[ti + 1 - i][!who], dp[i][who] + 1);
			}
		for (int i = 0; i <= MUST; ++i)
			for (int who : {0, 1})
				dp[i][who] = tdp[i][who];
	}
}

void solve()
{
	memset(busy, 0, sizeof busy);
	int sz[2];
	scanf("%d%d", &sz[0], &sz[1]);
	for (int it = 0; it < 2; ++it)
	{
		for (int i = 0; i < sz[it]; ++i)
		{
			int a, b;
			scanf("%d%d", &a, &b);
			for (int j = a; j < b; ++j)
				busy[it][j] = true;
		}
	}
	for (int b : {0, 1})
		for (int i = 0; i <= MUST; ++i)
			for (int who : {0, 1})
				dp[b][i][who] = INF;
	dp[0][0][0] = 0;
	dp[1][0][1] = 0;
	calc_dp(dp[0]);
	calc_dp(dp[1]);
	int ans = min({ dp[0][MUST][0], dp[1][MUST][1], dp[0][MUST][1] + 1, dp[1][MUST][0] + 1 });
	printf("%d\n", ans);
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#ifdef NOERR
	freopen("err.txt", "w", stderr);
#endif
#else
	//freopen("sum.in", "r", stdin);
	//freopen("sum.out", "w", stdout);
#endif


#ifdef ERR_CATCH
	try
	{
#endif

#ifdef ST
		while (true)
			solve();
#endif
#ifdef CASES
#define MULTITEST
#endif
#ifdef MULTITEST
		int t;
		scanf("%d", &t);
		for (int i = 0; i < t; ++i)
		{
#ifdef CASES
			printf("Case #%d: ", i + 1);
#endif
			solve();
#ifdef CASES
			eprintf("Passed case #%d:\n", i + 1);
#endif
		}
#else
		solve();
#endif

#ifdef ERR_CATCH
	}
	catch (logic_error e)
	{
		print_var(e.what());
		puts("___________________________________________________________________________");
		exit(0);
	}
#endif

	eprintf("\n\nTime: %.3lf\n", double(clock()) / CLOCKS_PER_SEC);
}
