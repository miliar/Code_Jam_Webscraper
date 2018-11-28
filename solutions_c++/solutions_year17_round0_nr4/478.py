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

#define CASES

const int N = 310;

int n, m;
int mt1[N], mt2[N];
bool can[N];
bool used[N];
vector<int> edges[N];
char f[N][N], f1[N][N];
vector<int> vs;

bool dfs(int v)
{
	if (used[v])
		return false;
	used[v] = true;
	for(auto e : edges[v])
		if (mt2[e] == -1)
		{
			mt2[e] = v;
			mt1[v] = e;
			return true;
		}
	for (auto e : edges[v])
		if (dfs(mt2[e]))
		{
			mt2[e] = v;
			mt1[v] = e;
			return true;
		}
	return false;
}

void kuhn()
{
	memset(mt1, -1, sizeof mt1);
	memset(mt2, -1, sizeof mt2);
	for (bool step = true; step;)
	{
		step = false;
		memset(used, false, sizeof used);
		for (auto v : vs)
			if (mt1[v] == -1 && dfs(v))
				step = true;
	}
}

void solve_diag()
{
	for (int s = 0; s < 2 * n - 1; ++s)
	{
		can[s] = true;
		for (int i = 0; i < n; ++i)
		{
			int j = s - i;
			if (0 <= j && j < n)
				can[s] &= f1[i][j] == '.' || f1[i][j] == 'x';
		}
	}

	vs.clear();
	for (int s = 0; s < 2 * n - 1; ++s)
	{
		int ok = true;
		edges[s].clear();
		for (int i = 0; i < n; ++i)
		{
			int j = i + (n - 1) - s;
			if (0 <= j && j < n)
				ok &= f1[i][j] == '.' || f1[i][j] == 'x';
		}
		if (!ok)
			continue;
		vs.push_back(s);
		for (int i = 0; i < n; ++i)
		{
			int j = i + (n - 1) - s;
			if (!(0 <= j && j < n))
				continue;
			int s2 = i + j;
			if (can[s2])
				edges[s].push_back(s2);
		}
	}

	kuhn();

	for (auto s1 : vs)
	{
		if (mt1[s1] == -1)
			continue;
		for (int i = 0; i < n; ++i)
		{
			int j = i + (n - 1) - s1;
			if (!(0 <= j && j < n))
				continue;
			int s2 = i + j;
			if (mt1[s1] == s2)
			{
				if (f1[i][j] == '.')
					f1[i][j] = '+';
				else
					f1[i][j] = 'o';
			}
		}
	}
}

void solve_hor()
{
	for (int j = 0; j < n; ++j)
	{
		can[j] = true;
		for (int i = 0; i < n; ++i)
			can[j] &= f1[i][j] == '.' || f1[i][j] == '+';
	}

	vs.clear();
	for (int i = 0; i < n; ++i)
	{
		int ok = true;
		edges[i].clear();
		for (int j = 0; j < n; ++j)
			ok &= f1[i][j] == '.' || f1[i][j] == '+';
		if (!ok)
			continue;
		vs.push_back(i);
		for (int j = 0; j < n; ++j)
			if (can[j])
				edges[i].push_back(j);
	}

	kuhn();
	for (auto x : vs)
		if (mt1[x] != -1)
		{
			int y = mt1[x];
			if (f1[x][y] == '.')
				f1[x][y] = 'x';
			else
				f1[x][y] = 'o';
		}
}

void solve()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			f[i][j] = '.';
	for (int i = 0; i < m; ++i)
	{
		char buf[10];
		int x, y;
		scanf("%s%d%d", buf, &x, &y);
		--x, --y;
		f[x][y] = buf[0];
	}
	memcpy(f1, f, sizeof f);

	solve_hor();
	solve_diag();

	int changed = 0;
	int score = 0;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
		{
			if (f1[i][j] == 'o')
				score += 2;
			else if (f1[i][j] != '.')
				++score;
			if (f1[i][j] != f[i][j])
				++changed;
		}
	printf("%d %d\n", score, changed);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			if (f1[i][j] != f[i][j])
				printf("%c %d %d\n", f1[i][j], i + 1, j + 1);
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
		eprintf("Passed case #%d: %.3lf\n", i + 1, double(clock()) / CLOCKS_PER_SEC);
#endif
	}
#else
	solve();
#endif

	eprintf("\n\nTime: %.3lf", double(clock()) / CLOCKS_PER_SEC);
}