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

const int N = 100 + 1;
int n, p;
int a[N];

inline void gen() {
	n = 100, p = 4;
	forn (i, n)
		a[i] = mt() % p;
}

inline bool read() {
	//gen();
	//return true;
	
	if (scanf ("%d%d", &n, &p) != 2)
		return false;
	
	forn (i, n)
		assert(scanf ("%d", &a[i]) == 1);
			
	return true;
}

int d[N][N][N][4];
int c[4];

inline void solve(int test) {
	printf ("Case #%d: ", test + 1);
	
	forn (i, 4)
		c[i] = 0;
	
	forn (i, n) {
		a[i] %= p;
		c[ a[i] ]++;
	}
		
	forn (i, n + 1)
		forn (j, n + 1)
			forn (k, n + 1)
    			forn (it, p)
    				d[i][j][k][it] = -1;
						
	d[0][0][0][0] = c[0];
						
	forn (i, c[1] + 1)
		forn (j, c[2] + 1)
			forn (k, c[3] + 1)
    			forn (last, p) {
    				int dv = d[i][j][k][last];
    				if (dv == -1)
    					continue;
    					
    				int add = (last == 0);    					
    					
    				if (i < c[1]) {
    					int nlast = (last + 1) % p;
    					d[i + 1][j][k][nlast] = max(d[i + 1][j][k][nlast], dv + add);
    				}
    				if (j < c[2]) {
    					int nlast = (last + 2) % p;
    					d[i][j + 1][k][nlast] = max(d[i][j + 1][k][nlast], dv + add);
    				}
    				if (k < c[3]) {
    					int nlast = (last + 3) % p;
    					d[i][j][k + 1][nlast] = max(d[i][j][k + 1][nlast], dv + add);
    				}    				
    			}
    			
    int ans = 0;
    forn (i, p)
    	ans = max(ans, d[ c[1] ][ c[2] ][ c[3] ][i]);
    			
    printf ("%d\n", ans);
}

int main() {
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
