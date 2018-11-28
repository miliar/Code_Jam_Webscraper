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

string s;

inline bool read()
{
	if (!(cin >> s))
		return false;

	return true;
}

const int L = 22, D = 10;

string z[L][D][2];

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	forn(len, L)
		forn(last, D)
			forn(eq, 2)
				z[len][last][eq] = "";

	fore(last, 1, (s[0] - '0'))
		z[1][last][last == (s[0] - '0')] = char(int('0') + last);

	fore(len, 1, sz(s) - 1)
		forn(last, D)
			forn(eq, 2)
			{
				if (z[len][last][eq] == "")
					continue;

				int to = D - 1;
				if (eq)
					to = (s[len] - '0');

				fore(next, last, to)
				{
					string dig = string(1, char(int('0') + next));
					int neq = eq && (next == to);
					z[len + 1][next][neq] = max(z[len + 1][next][neq], z[len][last][eq] + dig);
				}
			}

	string ans = "";

	forn(last, D)
		forn(eq, 2)
			ans = max(ans, z[sz(s)][last][eq]);

	if (ans == "")
	{
		assert(sz(s) >= 2);
		ans = string(sz(s) - 1, '9');
	}

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

