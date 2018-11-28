#pragma comment(linker, "/stack:128000000")

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define x first
#define y second
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 100 + 3;

int n, q;
li e[N], s[N];
li d[N][N];

inline bool read()
{
	if (scanf("%d%d", &n, &q) != 2)
		return false;

	forn(i, n)
		assert(cin >> e[i] >> s[i]);

	forn(i, n)
		forn(j, n)
			assert(cin >> d[i][j]);

	return true;
}

li INF64 = li(1e18);
li g[N][N];

ld res[N];

inline ld bfs(int st)
{
	forn(i, n)
		res[i] = ld(1e18);

	res[st] = ld(0.0);
	queue<int> q;
	q.push(st);

	while(!q.empty())
	{
		int v = q.front();
		q.pop();

		forn(to, n)
		{
			if (e[v] < g[v][to])
				continue;

			ld t = ld(g[v][to]) / ld(s[v]);
			if (res[to] > res[v] + t + EPS)
			{
				res[to] = res[v] + t;
				q.push(to);
			}
		}
	}
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	forn(i, n)
		forn(j, n)
		{
			if (i == j)
				g[i][j] = 0;
			else
			if (d[i][j] == -1)
				g[i][j] = INF64;
			else
				g[i][j] = d[i][j];
		}

	forn(i, n)
		forn(j, n)
			forn(k, n)
				g[i][j] = min(g[i][j], g[i][k] + g[k][j]);

	cout << setprecision(10) << fixed;
	forn(it, q)
	{
		int u, v;
		assert(scanf("%d %d", &u, &v) == 2);
		u--, v--;

		bfs(u);

		cout << res[v] << " ";
	}

	puts("");
}

int main()
{
#ifdef HP
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int testCnt;
	assert(cin >> testCnt);

	forn(test, testCnt)
	{
		assert(read());
		solve(test);
	}
	
	return 0;
}

