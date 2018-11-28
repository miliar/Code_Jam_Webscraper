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
//#define NOERR
#endif

#define MULTITEST
#define CASES

const int N = 2010;

struct Edge
{
	int cap, flow;
	int to;
	int link;
	int rem() const
	{
		return cap - flow;
	}
	Edge(int _to, int _cap) : to(_to), cap(_cap), flow() {}
};

const int S = 0;
const int T = 1;
int n, m, c;
vector<Edge> go[N];
vector<pii> to_inc;
bool used[N];
int cnt[N];

void add_edge(int from, int to, int cap)
{
	go[from].emplace_back(to, cap);
	go[to].emplace_back(from, 0);
	go[from].back().link = go[to].size() - 1;
	go[to].back().link = go[from].size() - 1;
}

bool dfs(int v)
{
	if (v == T)
		return true;
	if (used[v])
		return false;
	used[v] = true;
	for(auto& e : go[v])
		if (e.rem() > 0 && dfs(e.to))
		{
			++e.flow;
			--go[e.to][e.link].flow;
			return true;
		}
	return false;
}

void solve()
{
	scanf("%d%d%d", &n, &c, &m);
	memset(cnt, 0, sizeof cnt);
	for (int i = 0; i < N; ++i)
		go[i].clear();
	to_inc.clear();
	for (int i = 0; i < c; ++i)
	{
		add_edge(S, i + 2, 1);
		to_inc.emplace_back(S, go[S].size() - 1);
	}
	for (int i = 0; i < n; ++i)
	{
		add_edge(i + 2 + c, T, 1);
		to_inc.emplace_back(i + 2 + c, go[i + 2 + c].size() - 1);
		if (i > 0)
			add_edge(i + 2 + c, i + 1 + c, INF);
	}
	for (int i = 0; i < m; ++i)
	{
		int b, p;
		scanf("%d%d", &p, &b);
		--b, --p;
		++cnt[p];
		add_edge(b + 2, p + 2 + c, 1);
	}
	int now = 1;
	for (int i = 0; i < m; ++i)
	{
		memset(used, false, sizeof used);
		if (!dfs(S))
		{
			--i;
			for (auto p : to_inc)
				++go[p.first][p.second].cap;
			//print_var("INC");
			++now;
		}
	}
	int add = 0;
	for (int i = 0; i < n; ++i)
		add += max(0, cnt[i] - now);
	printf("%d %d\n", now, add);
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
		char endl1[5];
		fgets(endl1, 5, stdin);
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