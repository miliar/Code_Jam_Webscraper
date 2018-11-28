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

int a[7];
int old[7];

inline bool read()
{
	forn(i, 7)
		assert(scanf("%d", &a[i]) == 1);

	return true;
}

// 0  1  2  3  4  5  6
// N, R, O, Y, G, B, V

char ch[] = {'N', 'R', 'O', 'Y', 'G', 'B', 'V'};

struct color
{
	int x;
	char c;

	color(int x = 0, char c = '?'): x(x), c(c) { }
};

inline bool operator< (const color& a, const color& b)
{
	return a.x < b.x;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	forn(i, 7)
		old[i] = a[i];

	int n = a[0];

	fore(f, 1, 6)
	{
		forn(i, 7)
			a[i] = old[i];

		if (a[f] == 0)
			continue;
		
		string ans = "";
		a[f]--;
		char last = ch[f];
		ans.pb(last);

		bool ok = true;

		forn(it, n - 1 - 3)
		{
			int idx = -1;
			int cur = -1;

			fore(i, 1, 6)
			{
				if (ch[i] == last)
					continue;

				if (cur < a[i])
				{
					idx = i;
					cur = a[i];
				}
			}

			if (cur == 0)
			{
				ok = false;
				break;
			}

			assert(idx != -1);
			a[idx]--;
			last = ch[idx];
			ans.pb(last);
		}

		if (!ok)
			continue;
		
		string rem = "";
		fore(i, 1, 6)
			while(a[i] > 0)
			{
				a[i]--;
				rem.pb(ch[i]);
			}

		assert(sz(rem) <= 3);
		assert(sz(ans) + sz(rem) == n);

		sort(all(rem));

		do
		{
			string res = ans + rem;

			ok = true;
			forn(i, n)
			{
				int j = (i + 1) % n;
				if (res[i] == res[j])
				{
					ok = false;
					break;
				}
			}
			
			if (ok)
			{
				cout << res << endl;
				return;
			}

		} while(next_permutation(all(rem)));
	}

	cout << "IMPOSSIBLE" << endl;
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

