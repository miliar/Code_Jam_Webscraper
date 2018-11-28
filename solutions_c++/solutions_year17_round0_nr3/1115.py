#include<bits/stdc++.h>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i < int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;
const ld PI = acosl(ld(-1));

mt19937 mt(time(NULL));

li n, k;

inline bool read()
{
	if (scanf ("%lld%lld", &n, &k) != 2)
		return false;

	return true;
}

map<li, li> q;

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);
	
	q.clear();
	q[-n] = 1;
	
	while (true) {
		li len = -(q.begin()->x), cnt = q.begin()->y;
		q.erase(q.begin());
		li l = (len - 1) >> 1;
		li r = (len - 1) - l;
		if (cnt >= k) {
			printf ("%lld %lld\n", max(l, r), min(l, r));
			return;
		}
		
		k -= cnt;
		
		if (l)
			q[-l] += cnt;
		if (r)
			q[-r] += cnt;
	}
	
	throw;
}

int main()
{
#ifdef SU2_PROJ
	assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif

	cout << setprecision(25) << fixed;
	cerr << setprecision(10) << fixed;
	
	int testCnt;
	assert(scanf ("%d", &testCnt) == 1);

	forn (test, testCnt) {
		assert(read());
		solve(test);
	}

#ifdef SU2_PROJ
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}
