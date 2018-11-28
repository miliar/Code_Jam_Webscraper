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

const int N = 100 + 2;

int n, p;
int a[N];

inline bool read()
{
	if (scanf("%d%d", &n, &p) != 2)
		return false;

	forn(i, n)
		assert(scanf("%d", &a[i]) == 1);

	return true;
}

const int P = 4;

int c[P];

int z[N][N][N][P];

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	forn(i, P)
		c[i] = 0;

	int start = 0;

	forn(i, n)
	{
		int x = a[i] % p;
		if (x == 0)
			start++;
		else
			c[x]++;		
	}

	memset(z, -1, sizeof(z));

	int maxv = max( c[1], max (c[2], c[3]) );

	z[ c[1] ][ c[2] ][ c[3] ][0] = start;

	ford(a, maxv + 1)
	ford(b, maxv + 1)
	ford(c, maxv + 1)
	forn(l, p)
	{
		int& dv = z[a][b][c][l];

		if (dv == -1)
			continue;

		if (a > 0)
		{
			int add = 1;
			int na = a, nb = b, nc = c, nl = (l + add) % p;
			na--;
			int nval = dv + int(l == 0);
			z[na][nb][nc][nl] = max(z[na][nb][nc][nl], nval);
		}

		if (b > 0)
		{
			int add = 2;
			int na = a, nb = b, nc = c, nl = (l + add) % p;
			nb--;
			int nval = dv + int(l == 0);
			z[na][nb][nc][nl] = max(z[na][nb][nc][nl], nval);
		}

		if (c > 0)
		{
			int add = 3;
			int na = a, nb = b, nc = c, nl = (l + add) % p;
			nc--;
			int nval = dv + int(l == 0);
			z[na][nb][nc][nl] = max(z[na][nb][nc][nl], nval);
		}
	}

	int ans = -1;
	forn(l, p)
		ans = max(ans, z[0][0][0][l]);

	assert(ans >= 0);

	cout << ans << endl;
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

