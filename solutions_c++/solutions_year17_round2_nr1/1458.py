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
const ld EPS = 1e-10;
const ld PI = 3.1415926535897932384626433832795;

const int N = 1000 + 3;

int d, n;
int k[N], s[N];

inline bool read()
{
	if (scanf("%d%d", &d, &n) != 2)
		return false;

	forn(i, n)
		assert(scanf("%d%d", &k[i], &s[i]) == 2);
	
	return true;
}

inline bool check(ld v)
{
	ld t = ld(d) / ld(v);

	forn(i, n)
	{
		if (s[i] >= v - EPS)
			continue;

		ld tt = (ld(k[i]) - ld(0.0)) / (v - ld(s[i]));
		ld d1 = tt * v;
		//ld d2 = ld(k[i]) + tt * ld(s[i]);
	
		if (d1 <= d + EPS)
			return false;

		//if (tt <= t + EPS)
		//	return false;
	}

	return true;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	ld lf = 0.0, rg = ld(1e16);

	forn(it, 5000)
	{
		ld mid = (lf + rg) / ld(2.0);

		if (check(mid))
			lf = mid;
		else
			rg = mid;
	}

	cout << setprecision(6) << fixed;
	cout << lf << endl;
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

