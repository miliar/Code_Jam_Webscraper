#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define nfor(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

template<typename A, typename B> inline ostream& operator<< (ostream& out, const pair<A, B>& p) { return out << "(" << p.x << ", " << p.y << ")"; }
template<typename T> inline ostream& operator<< (ostream& out, const vector<T>& a) { out << "["; forn(i, sz(a)) { if (i) out << ','; out << ' ' << a[i]; } return out << " ]"; } 
template<typename T> inline ostream& operator<< (ostream& out, const set<T>& a) { return out << vector<T>(all(a)); }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const map<X, Y>& a) { return out << vector<pair<X, Y>>(all(a)); }
template<typename T> inline ostream& operator<< (ostream& out, pair<T*, int> a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

#ifdef SU1
#define LOG
#endif

int n, q;
const int N = 105;
int e[N], s[N];
li d[N][N];
ld d2[N][N];

bool read() {
	if (!(cin >> n >> q))
		return false;
	forn(i, n) {
		assert(scanf("%d%d", &e[i], &s[i]) == 2);
	}
	forn(i, n) {
		forn(j, n) {
			assert(scanf("%Ld", &d[i][j]) == 1);
		}
	}
	return true;
}

void solve(int tc) {
	printf("Case #%d: ", tc + 1);
	forn(i, n)
		d[i][i] = 0;
	forn(k, n)
		forn(i, n)
			forn(j, n)
				if (d[i][k] != -1 && d[k][j] != -1) {
					if (d[i][j] == -1)
						d[i][j] = d[i][k] + d[k][j];
					else
						d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
				}

/*	forn(i, n) {
		forn(j, n) {
			cerr << d[i][j] << " ";
		}
		cerr << endl;
	}*/

	forn(i, n) {
		forn(j, n) {
			d2[i][j] = ld(1e100);
			if (d[i][j] == -1)
				continue;
			if (d[i][j] <= e[i])
				d2[i][j] = ld(d[i][j]) / s[i];
		}
		d2[i][i] = 0;
	}

	forn(k, n)
		forn(i, n)
			forn(j, n)
				d2[i][j] = min(d2[i][j], d2[i][k] + d2[k][j]);

	forn(i, q) {
		int u, v;
		assert(scanf("%d %d", &u, &v) == 2);
		--u, --v;
		if (i)
			putchar(' ');
		printf("%0.9f", double(d2[u][v]));
	}
	puts("");
}

int main() {
#ifdef SU1
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;

	int t;
	assert(cin >> t);
	int tc = 0;

    while (read()) {
		ld stime = gett();
		solve(tc++);
		cerr << "Time: " << gett() - stime << endl;
		//break;
	}
	
    return 0;
}
