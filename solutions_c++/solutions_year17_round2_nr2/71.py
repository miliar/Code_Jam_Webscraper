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

#define MULTITEST
#define CASES

const int N = 1010;
int rsz;
bool ybig = false;
bool rbig = false;
bool bbig = false;
int r, o, y, g, b, v;

vector<char> make_res(int y, char yc, int r, char rc, int b, char bc)
{
	auto res = vector<char>(y, yc);
	vector<char> tmp;
	for (int i = 0; i < r; ++i)
	{
		tmp.push_back(res.back());
		res.pop_back();
		tmp.push_back(rc);
	}
	for (auto e : res)
		tmp.push_back(e);
	res.clear();
	res.swap(tmp);
	for (int i = 0; i < b; ++i)
	{
		tmp.push_back(bc);
		tmp.push_back(res.back());
		res.pop_back();
	}
	reverse(res.begin(), res.end());
	for (auto e : res)
		tmp.push_back(e);
	res.clear();
	res.swap(tmp);
	return res;
}

void solve()
{
	int n;
	scanf("%d", &n);
	scanf("%d%d%d%d%d%d", &r, &o, &y, &g, &b, &v);
	y -= v;
	if (y < 0 || (y == 0 && v != 0 && n != 2 * v))
	{
		puts("IMPOSSIBLE");
		return;
	}
	r -= g;
	if (r < 0 || (r == 0 && g != 0 && n != 2 * g))
	{
		puts("IMPOSSIBLE");
		return;
	}
	b -= o;
	if (b < 0 || (b == 0 && o != 0 && n != 2 * o))
	{
		puts("IMPOSSIBLE");
		return;
	}
	auto mx = max({ y, r, b });
	if (mx * 2 > (y + r + b))
	{
		puts("IMPOSSIBLE");
		return;
	}
	ybig = false;
	rbig = false;
	bbig = false;
	vector<char> res;
	if (y == mx)
		res = make_res(y, 'Y', r, 'R', b, 'B');
	else if (r == mx)
		res = make_res(r, 'R', y, 'Y', b, 'B');
	else
		res = make_res(b, 'B', r, 'R', y, 'Y');
	if (n == 2 * v)
	{
		for (int i = 0; i < v; ++i)
			printf("%s", "YV");
	}
	else if (n == 2 * g)
	{
		for (int i = 0; i < g; ++i)
			printf("%s", "RG");
	}
	else if (n == 2 * o)
	{
		for (int i = 0; i < o; ++i)
			printf("%s", "BO");
	}
	else
	{
		for(auto e : res)
		{
			printf("%c", e);
			if (e == 'Y' && !ybig)
			{
				for (int i = 0; i < v; ++i)
					printf("%s", "VY");
				ybig = true;
			}
			else if (e == 'R' && !rbig)
			{
				for (int i = 0; i < g; ++i)
					printf("%s", "GR");
				rbig = true;
			}
			else if(!bbig)
			{
				for (int i = 0; i < o; ++i)
					printf("%s", "OB");
				bbig = true;
			}
		}
	}
	puts("");
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


#ifdef LOCAL
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

#ifdef LOCAL
	}
	catch (logic_error e)
	{
		print_var(e.what());
		puts("___________________________________________________________________________");
		exit(0);
	}
#endif

	eprintf("\n\nTime: %.3lf", double(clock()) / CLOCKS_PER_SEC);
}