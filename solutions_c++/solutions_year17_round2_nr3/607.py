#include <bits/stdc++.h>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i <= int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define ft first
#define sc second
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

const int N = 105;
ld d[N][N];
int n;
int q;
pt p[N];
ld maxdist[N], v[N];

inline bool read() {
	cin >> n >> q;
	forn (i, n) {
		cin >> maxdist[i] >> v[i];
	}
	forn (i, n) {
		forn (j, n) {
			cin >> d[i][j];
			if (d[i][j] == -1)
				d[i][j] = INF64;
		}
	}
	forn (i, q)
		cin >> p[i].x >> p[i].y;
	return true;
}
   
ld calc(int s, int t) {
	s--, t--;
	ld dp[N];
	forn (i, N)
		dp[i] = INF64;
	dp[s] = 0;
	while(true) {
		bool ok = false;
		forn (i, n) {
			forn (j, n)
				if (d[i][j] <= maxdist[i]) {
					if (dp[j] > dp[i] + d[i][j] / v[i])
						ok = true;
					dp[j] = min(dp[j], dp[i] + d[i][j] / v[i]);
				}
		}
		if (!ok)
			break;
	}
	return dp[t];
}

inline void solve() {   
	forn (k, n)
		forn (i, n)
			forn (j, n)
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
	forn (i, q)
		cout << calc(p[i].x, p[i].y) << ' ';
	cout << endl;
}

int main()
{
#ifdef SU2
	assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif

	cout << setprecision(25) << fixed;
	cerr << setprecision(10) << fixed;

	srand(int(time(NULL)));

	int t;
	cin >> t;
	
	forn (i, t) {
		cout << "Case #" << i + 1 << ": ";
		assert(read());
		solve();
	}

#ifdef SU2
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}