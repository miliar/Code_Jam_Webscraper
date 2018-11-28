#include <bits/stdc++.h>
using namespace std;

#define ms(s, n) memset(s, n, sizeof(s))
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FORd(i, a, b) for (int i = (a) - 1; i >= (b); i--)
#define FORall(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define sz(a) int((a).size())
#define present(t, x) (t.find(x) != t.end())
#define all(a) (a).begin(), (a).end()
#define uni(a) (a).erase(unique(all(a)), (a).end())
#define pb push_back
#define pf push_front
#define mp make_pair
#define fi first
#define se second
#define prec(n) fixed<<setprecision(n)
#define bit(n, i) (((n) >> (i)) & 1)
#define bitcount(n) __builtin_popcountll(n)
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<pi> vii;
const int MOD = (int) 1e9 + 7;
const int INF = (int) 1e9;
const ll LINF = (ll) 1e18;
const ld PI = acos((ld) -1);
const ld EPS = 1e-9;
inline ll gcd(ll a, ll b) {ll r; while (b) {r = a % b; a = b; b = r;} return a;}
inline ll lcm(ll a, ll b) {return a / gcd(a, b) * b;}
inline ll fpow(ll n, ll k, int p = MOD) {ll r = 1; for (; k; k >>= 1) {if (k & 1) r = r * n % p; n = n * n % p;} return r;}
template<class T> inline int chkmin(T& a, const T& val) {return val < a ? a = val, 1 : 0;}
template<class T> inline int chkmax(T& a, const T& val) {return a < val ? a = val, 1 : 0;}
inline ll isqrt(ll k) {ll r = sqrt(k) + 1; while (r * r > k) r--; return r;}
inline ll icbrt(ll k) {ll r = cbrt(k) + 1; while (r * r * r > k) r--; return r;}
inline void addmod(int& a, int val, int p = MOD) {if ((a = (a + val)) >= p) a -= p;}
inline void submod(int& a, int val, int p = MOD) {if ((a = (a - val)) < 0) a += p;}
inline int mult(int a, int b, int p = MOD) {return (ll) a * b % p;}
inline int inv(int a, int p = MOD) {return fpow(a, p - 2, p);}
inline int sign(ld x) {return x < -EPS ? -1 : x > +EPS;}
inline int sign(ld x, ld y) {return sign(x - y);}
#define db(x) cerr << #x << " = " << (x) << ", ";
#define endln cerr << "\n";
#define chkpt cerr << "-----\n";

struct HopcroftKarp {
	static const int MAXV = 1000 + 5;
	static const int MAXE = 1000000 + 5;
	int nx, ny, E, adj[MAXE], nxt[MAXE], lst[MAXV], cur[MAXV], lev[MAXV], que[MAXV], matx[MAXV], maty[MAXV];
	void init(int nx, int ny) {
		this->nx = nx, this->ny = ny;
		E = 0, fill_n(lst, nx + 1, -1);
		fill_n(matx, nx + 1, -1), fill_n(maty, ny + 1, -1);
	}
	void add(int x, int y) {
		adj[E] = y, nxt[E] = lst[x], lst[x] = E++;
	}
	int bfs() {
		int qsize = 0;
		for (int x = 1; x <= nx; x++) if (matx[x] != -1) lev[x] = -1;
		else {
			lev[x] = 0;
			que[qsize++] = x;
		}
		int found = 0;
		for (int i = 0; i < qsize; i++) {
			for (int x = que[i], e = lst[x]; e != -1; e = nxt[e]) {
				int y = adj[e];
				if (maty[y] == -1) found = 1;
				else if (lev[maty[y]] == -1) {
					lev[maty[y]] = lev[x] + 1;
					que[qsize++] = maty[y];
				}
			}
		}
		return found;
	}
	int dfs(int x) {
		for (int &e = cur[x]; e != -1; e = nxt[e]) {
			int y = adj[e];
			if (maty[y] == -1 || (lev[maty[y]] == lev[x] + 1 && dfs(maty[y]))) {
				matx[x] = y;
				maty[y] = x;
				return 1;
			}
		}
		return 0;
	}
	int maxmat() {
		int res = 0;
		while (bfs()) {
			for (int x = 1; x <= nx; x++) cur[x] = lst[x];
			for (int x = 1; x <= nx; x++) if (matx[x] == -1) res += dfs(x);
		}
		return res;
	}
} hopkarp;

const int maxn = 1e2 + 5;
int n, m;
int a[maxn][maxn];
int b[maxn][maxn];
int row[maxn];
int col[maxn];
int majordig[maxn + maxn];
int minordig[maxn + maxn];

void solve() {
	int test; cin >> test;
	FOR(it, 1, test + 1) {
		cout << "Case #" << it << ": ";
		cin >> n >> m;
		FOR(i, 0, n) fill_n(a[i], n, 0), fill_n(b[i], n, 0);
		fill_n(row, n, 0), fill_n(col, n, 0);
		fill_n(majordig, n + n, 0), fill_n(minordig, n + n, 0);
		int ans = 0; vii change;
		FOR(i, 0, m) {
			string s; int r, c; cin >> s >> r >> c; r--, c--;
			a[r][c] = s[0];
			int u = r + c;
			int v = r - c + n - 1;
			if (a[r][c] == '+') {
				b[r][c] = 1;
				ans++;
			}
			else if (a[r][c] == 'x') {
				b[r][c] = 2;
				ans++;
			}
			else if (a[r][c] == 'o') {
				b[r][c] = 3;
				ans++, ans++;
			}
			if (a[r][c] != '+') {
				row[r] = col[c] = 1;
			}
			if (a[r][c] != 'x') {
				majordig[u] = minordig[v] = 1;
			}
		}
		hopkarp.init(n, n);
		FOR(i, 0, n) FOR(j, 0, n) {
			if (a[i][j] != 'x' && a[i][j] != 'o' && !row[i] && !col[j]) {
				hopkarp.add(i + 1, j + 1);
			}
		}
		ans += hopkarp.maxmat();
		FOR(i, 0, n) {
			if (~hopkarp.matx[i + 1]) {
				int j = hopkarp.matx[i + 1] - 1;
				b[i][j] |= 2;
				change.pb(mp(i, j));
			}
		}
		hopkarp.init(n + n - 1, n + n - 1);
		FOR(i, 0, n + n - 1) FOR(j, 0, n + n - 1) if (!majordig[i] && !minordig[j] && !(i + j + n - 1 & 1)) {
			int u = (i + (j - (n - 1))) / 2;
			int v = (i - (j - (n - 1))) / 2;
			if (u >= 0 && u < n && v >= 0 && v < n && a[u][v] != '+' && a[u][v] != 'o') {
				hopkarp.add(i + 1, j + 1); 
			}
		}
		ans += hopkarp.maxmat();
		FOR(i, 0, n + n - 1) {
			if (~hopkarp.matx[i + 1]) {
				int j = hopkarp.matx[i + 1] - 1;
				int u = (i + (j - (n - 1))) / 2;
				int v = (i - (j - (n - 1))) / 2;
				change.pb(mp(u, v));
				b[u][v] |= 1;
			}
		}
		sort(all(change)), uni(change);
		cout << ans << " " << sz(change) << "\n";
		FOR(i, 0, sz(change)) {
			int u = change[i].fi;
			int v = change[i].se;
			if (b[u][v] == 1) {
				cout << "+ " << u + 1 << " " << v + 1 << "\n";
			}
			else if (b[u][v] == 2) {
				cout << "x " << u + 1 << " " << v + 1 << "\n";
			}
			else if (b[u][v] == 3) {
				cout << "o " << u + 1 << " " << v + 1 << "\n";
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
#ifdef _LOCAL_
	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
#endif
	solve();
#ifdef _LOCAL_
	//printf("\nTime elapsed: %dms", 1000 * clock() / CLOCKS_PER_SEC);
#endif
	return 0;
}
