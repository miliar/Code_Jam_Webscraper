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

const int N = 100 + 3;
int n, cntq;
int e[N], s[N];
int d[N][N];

inline bool read()
{
	if (scanf ("%d%d", &n, &cntq) != 2)
		return false;
		
	forn (i, n)
		assert(scanf ("%d%d", &e[i], &s[i]) == 2);
		
	forn (i, n)
		forn (j, n)
			assert(scanf ("%d", &d[i][j]) == 1);

	return true;
}

inline bool operator < (const pair<ld, pt>& a, const pair<ld, pt>& b) {
	if (abs(a.x - b.x) < EPS)
		return a.y < b.y;
		
	return a.x < b.x;
}

li dist[N][N];
ld z[N][N];
int used[N][N];
set<pair<ld, pt> > q;

inline void update (int v, int h, ld val) {
	if (z[v][h] > val) {
		if (z[v][h] < 1e99)
			q.erase(mp(z[v][h], mp(v, h)));
		z[v][h] = val;
		q.insert(mp(val, mp(v, h)));
	}
}

inline void solve(int test)
{
	printf ("Case #%d:", test + 1);
	
	forn (i, n) {
		forn (j, n) {
			if (d[i][j] == -1)
				dist[i][j] = INF64;
			else
				dist[i][j] = d[i][j];
		}
		
		dist[i][i] = 0;
	}
	
	forn (t, n)
		forn (i, n)
			forn (j, n)
				dist[i][j] = min(dist[i][j], dist[i][t] + dist[t][j]);
				
	forn (it, cntq) {
		int ss, tt;
		assert(scanf ("%d%d", &ss, &tt) == 2);
		
		ss--, tt--;
		
		forn (i, n)
			forn (j, n) {
				z[i][j] = 1e100;
				used[i][j] = 0;
			}
		q.clear();
				
		z[ss][ss] = 0;
		q.insert(mp(0, mp(ss, ss)));
		
		while (!q.empty()) {
			int v = q.begin()->y.x, h = q.begin()->y.y;
			q.erase(q.begin());
			
			ld dv = z[v][h];
			used[v][h] = 1;
			
			if (!used[v][v])
				update(v, v, dv);
			
			li left = e[h] - dist[h][v];
			forn (i, n) {
				if (d[v][i] == -1)
					continue;
					
				if (d[v][i] > left)
					continue;
					
				if (!used[i][h])
					update(i, h, dv + ld(d[v][i]) / ld(s[h]));
			}
		}
		
		ld ans = 1e100;
		forn (i, n)
			ans = min(ans, z[tt][i]);
			
		if (ans > 1e99)
			throw;
		else
			printf (" %.15f", double(ans));
	}
	
	puts("");
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
		cerr << test + 1 << endl;		
	}

#ifdef SU2_PROJ
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}
