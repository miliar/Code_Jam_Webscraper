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

const int N = 1000 + 3;

int n, c, m;
pt b[N];

inline bool read()
{
	if (scanf("%d%d%d", &n, &c, &m) != 3)
		return false;

	forn(i, m)
	{
		int p, x;
		assert(scanf("%d%d", &p, &x) == 2);
		p--, x--;

		b[i] = mp(p, x);
	}

	return true;
}

int cnt[N], sum[N];
int res;

int used[N];

inline bool check(int k)
{
	res = 0;
	memset(cnt, 0, sizeof(cnt));
	memset(sum, 0, sizeof(sum));
	memset(used, 0, sizeof(used));

	forn(i, m)
	{
		int p = b[i].ft, x = b[i].sc;

		if (sum[p] < k && cnt[x] < k)
		{
			sum[p]++;
			cnt[x]++;
			used[i] = true;
		}
		else
			continue;
	}

	int ptr = 0;
	
	forn(i, m)
	{
		if (used[i])
			continue;

		int p = b[i].ft, x = b[i].sc;

		if (cnt[x] == k)
			return false;

		while(ptr < p && sum[ptr] == k)
			ptr++;

		if (ptr >= p)
			return false;

		res++;
		sum[ptr]++;
		cnt[x]++;
	}

	return true;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	int lf = 0, rg = c;
	rg = N;
	while(lf != rg)
	{
		int mid = (lf + rg) >> 1;

		if (check(mid))
			rg = mid;
		else
			lf = mid + 1;
	}

	assert(check(lf));

	cout << lf << " " << res << endl;
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

