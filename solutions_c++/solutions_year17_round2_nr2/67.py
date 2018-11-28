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
int n;
int r, o, y, g, b, v;

inline void gen() {
	r = rand() % 10;
	y = rand() % 10;
	b = rand() % 10;
	o = rand() % 10;
	g = rand() % 10;
	v = rand() % 10;
	n = r + y + b + o + g + v;
	cout << n << ' ' << r << ' ' << o << ' ' << y << ' ' << g << ' ' << b << ' ' << v << endl;
}

inline bool read()
{
//	gen();
//	return true;
	
	if (!(cin >> n >> r >> o >> y >> g >> b >> v))
		return false;

	return true;
}

inline int mask (char c) {
	if (c == 'B')
		return 1;
	if (c == 'Y')
		return 2;
	if (c == 'R')
		return 4;
	if (c == 'O')
		return 2 + 4;
	if (c == 'G')
		return 1 + 2;
	if (c == 'V')
		return 1 + 4;
		
	throw;
}

inline bool norm (char c1, char c2) {
	return (mask(c1) & mask(c2)) == 0;
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);
	
	if (n == o + b && o == b) {
		forn (i, n / 2) {
			putchar('O');
			putchar('B');
		}
		puts("");
		return;
	}
	
	if (n == o + b && o == b - 1) {
		puts("IMPOSSIBLE");
		return;
	}
	
	if (n == g + r && g == r) {
		forn (i, n / 2) {
			putchar('G');
			putchar('R');
		}
		puts("");
		return;
	}

	if (n == g + r && g == r - 1) {
		puts("IMPOSSIBLE");
		return;
	}
	
	if (n == v + y && v == y) {
		forn (i, n / 2) {
			putchar('V');
			putchar('Y');
		}
		puts("");
		return;
	}	
	
	if (n == v + y && v == y - 1) {
		puts("IMPOSSIBLE");
		return;
	}	
	
	int oldO = o, oldG = g, oldV = v;
	
	while (o) {
		if (b < 2) {
			puts("IMPOSSIBLE");
			return;
		}
		
		b -= 2;
		o--;
		b++;
	}
	
	while (g) {
		if (r < 2) {
			puts("IMPOSSIBLE");
			return;
		}
		
		r -= 2;
		g--;
		r++;
	}	
	
	while (v) {
		if (y < 2) {
			puts("IMPOSSIBLE");
			return;
		}
		
		y -= 2;
		v--;
		y++;
	}
	
	vector<pair<int, char> > c;
	c.pb(mp(b, 'B'));
	c.pb(mp(y, 'Y'));
	c.pb(mp(r, 'R'));
	
	n = b + y + r;
	
	sort(all(c));
	if (n != 1 && c[0].x + c[1].x < c[2].x) {
		puts("IMPOSSIBLE");
		return;
	}
	
	string ans;
	ans.resize(n);
	
	if (n == 1) {
		forn (i, 3)
			if (c[i].x)
				ans[0] = c[i].y;
	} else {
    	forn (i, n)
    		ans[i] = 0;

    	int pos = 0;
    	forn (i, c[2].x) {
    		ans[pos] = c[2].y;
    		pos += 2;
    	}
	
    	int it = 0;
    	
    	ford (i, n) {
    		if (ans[i] != 0)
    			continue;
    			
    		while (true) {
    			if (c[it].x) {
    				ans[i] = c[it].y;
    				c[it].x--;
    				it ^= 1;
    				break;
    			}
    			
    			it ^= 1;
    		}
    	}
    }
	
	while (oldO) {
		forn (i, sz(ans))
			if (ans[i] == 'B') {
				ans.insert(ans.begin() + i + 1, 'B');
				ans.insert(ans.begin() + i + 1, 'O');
				break;
			}
		oldO--;
	}
	
	while (oldG) {
		forn (i, sz(ans))
			if (ans[i] == 'R') {
				ans.insert(ans.begin() + i + 1, 'R');
				ans.insert(ans.begin() + i + 1, 'G');
				break;
			}
		oldG--;
	}

	while (oldV) {
		forn (i, sz(ans))
			if (ans[i] == 'Y') {
				ans.insert(ans.begin() + i + 1, 'Y');
				ans.insert(ans.begin() + i + 1, 'V');
				break;
			}
		oldV--;
	}	
	
	//cerr << ans << endl;
	
	forn (i, sz(ans)) {
		int ni = (i == sz(ans) - 1 ? 0 : i + 1);
		assert(norm(ans[i], ans[ni]));
	}
	
	printf ("%s\n", ans.c_str());
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
