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

int r, c;
int dx[4] = {-1, 0, +1, 0};
int dy[4] = {0, -1, 0, +1};

const int N = 100;
char s[N][N];
vector <int> cs[N][N];

bool read() {
	if (!(cin >> r >> c))
		return false;
	forn(i, r) {
		assert(cin >> s[i]);
	}
	return true;
}

int cn;
int n;
pt nums[N * N];

bool go(int &x, int &y, int &d) {
	x += dx[d];
	y += dy[d];
	if (x == r || y == c || x == -1 || y == -1 || s[x][y] == '#')
		return false;
	if (s[x][y] == '/') {
		d ^= 3;
	}
	if (s[x][y] == '\\') {
		d ^= 1;
	}
	return true;
}

vector <int> g[N * N], gt[N * N];
bool bad[N * N];

vector<bool> used;
vector<int> order, comp;

void dfs1 (int v) {
	used[v] = true;
	for (size_t i=0; i<g[v].size(); ++i) {
		int to = g[v][i];
		if (!used[to])
			dfs1 (to);
	}
	order.push_back (v);
}

void dfs2 (int v, int cl) {
	comp[v] = cl;
	for (size_t i=0; i<gt[v].size(); ++i) {
		int to = gt[v][i];
		if (comp[to] == -1)
			dfs2 (to, cl);
	}
}

void solve(int tc) {
	printf("Case #%d: ", tc + 1);
	forn(i, r)
		forn(j, c)
			cs[i][j].clear();

	forn(i, N * N) {
		g[i].clear();
		gt[i].clear();
		bad[i] = false;
	}

	cn = 0;
	forn(i, r) {
		forn(j, c) {
			if (s[i][j] == '-' || s[i][j] == '|') {
				nums[cn++] = pt(i, j);
				forn(dd, 4) {
					int x = i, y = j;
					int d = dd;
					int cc = d & 1;
					int v = (cn - 1) * 2 + cc;
					vector <pt> path;
					while (go(x, y, d)) {
						if (s[x][y] == '-' || s[x][y] == '|') {
							g[v].pb(v ^ 1);
							bad[v] = true;
						}
						cs[x][y].pb(v);
					}
				}
			}
		}
	}

//	cerr << "here" << endl;

	used.clear();
	order.clear();
	comp.clear();

	forn(i, r)
		forn(j, c)
			if (s[i][j] == '.') {
				vector <int> tmp;
				for (int v: cs[i][j]) {
					if (!bad[v])
						tmp.pb(v);
				}
				cs[i][j] = tmp;
				if (sz(cs[i][j]) == 0) {
					puts("IMPOSSIBLE");
					return;
				}
				if (sz(cs[i][j]) == 1) {
					g[cs[i][j][0] ^ 1].pb(cs[i][j][0]);
					continue;
				}
				if (sz(cs[i][j]) == 2) {
					forn(t, 2)
						g[cs[i][j][t] ^ 1].pb(cs[i][j][t ^ 1]);
					continue;
				}
				throw;
			}

	n = cn * 2;
	forn(i, n)
		for (int to: g[i])
			gt[to].pb(i);

	used.assign (n, false);
	for (int i=0; i<n; ++i)
		if (!used[i])
			dfs1 (i);

	comp.assign (n, -1);
	for (int i=0, j=0; i<n; ++i) {
		int v = order[n-i-1];
		if (comp[v] == -1)
			dfs2 (v, j++);
	}

	for (int i=0; i<n; ++i)
		if (comp[i] == comp[i^1]) {
			puts ("IMPOSSIBLE");
			return;
		}
	puts("POSSIBLE");
	for (int i=0; i<n; ++i) {
		if (comp[i] > comp[i ^ 1]) {
			int id = i / 2;
			s[nums[id].x][nums[id].y] = string("-|")[!(i & 1)];
		}
	}

	forn(i, r)
		puts(s[i]);
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

	forn(test, t) {
		assert(read());
		ld stime = gett();
		solve(test);
		cerr << "Time: " << gett() - stime << endl;
		//break;
	}
	
    return 0;
}
