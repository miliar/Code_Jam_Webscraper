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

const int N = 1000 + 13;
int n, d;
pt a[N];

inline bool read()
{
	if (scanf ("%d%d", &d, &n) != 2)
		return false;
		
	forn (i, n)
		assert(scanf ("%d%d", &a[i].x, &a[i].y) == 2);

	return true;
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);
	
	sort(a, a + n);
	
	ld ans = 0;
	
	ford (i, n) {
		/*int v = -1;
		ld minTime = 1e100;
		for (int j = n - 1; j > i; j--) {
			if (a[j].y >= a[i].y)
				continue;
				
			ld curTime = ld(a[j].x - a[i].x) / (a[i].y - a[j].y);
			if (curTime < minTime || (abs(curTime - minTime) < EPS && a[v].y > a[j].y))
				v = j;
		}
		
		if (v == -1) {*/
			ans = max(ans, ld(d - a[i].x) / a[i].y);
		/*} else {
			
		}*/
	}
	
	printf ("%.15f\n", double(ld(d) / ans));
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
