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

li n;

inline bool read()
{
	if (scanf ("%lld", &n) != 1)
		return false;
	return true;
}

li d[20][10][2];
int c[20], szc;

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);
	
	szc = 0;
	while (n) {
		c[szc++] = n % 10;
		n /= 10;
	}
	
	reverse(c, c + szc);
	
	memset(d, -1, sizeof d);
	
	d[0][0][1] = 0;
	forn (i, szc)
		forn (last, 10)
			forn (f, 2) {
				li dv = d[i][last][f];
				if (dv == -1)
					continue;
					
				fore (cur, last, 10) {
					if (f && cur > c[i])
						continue;

					int nf = f & (cur == c[i]);
					d[i + 1][cur][nf] = max(d[i + 1][cur][nf], dv * 10 + cur);
				}
			}
			
	li ans = -1;
	forn (last, 10) {
		ans = max(ans, d[szc][last][0]);
		ans = max(ans, d[szc][last][1]);
	}

	cout << ans << endl;
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
