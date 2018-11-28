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

struct Seg {
	static const int maxn = 24 * 60 + 5;
	int st[maxn << 1];
	void init() {
		fill_n(st, maxn << 1, INF);
	}
	void upd(int p, int val) {
		for (st[p += maxn] = val; p > 1; ) p >>= 1, st[p] = min(st[p << 1], st[p << 1 | 1]);
	}
	int query(int l, int r) {
		int res = INF;
		for (l += maxn, r += maxn + 1; l < r; l >>= 1, r >>= 1) {
			if (l & 1) chkmin(res, st[l++]);
			if (r & 1) chkmin(res, st[--r]);
		}
		return res;
	}
};

const int maxn = 100 + 5;
int n[2];
int x[2][maxn];
int y[2][maxn];
int nxt[24 * 60 + 5][2];
int dp[24 * 60 + 5][12 * 60 + 5][2];
Seg seg[24 * 60 + 5][2];

void solve() {
	int test; cin >> test;
	FOR(it, 1, test + 1) {
		cout << "Case #" << it << ": ";
		cerr << "Test #" << it << "\n";
		FOR(w, 0, 2) cin >> n[w];
		FOR(w, 0, 2) FOR(i, 0, n[w]) cin >> x[w][i] >> y[w][i];
		FOR(w, 0, 2) {
			FOR(i, 0, 24 * 60 + 1) {
				int found = 0;
				FOR(j, 0, n[w]) {
					if (x[w][j] <= i && y[w][j] > i) {
						found = 1;
						break;
					}
				}
				if (found) {
					nxt[i][w] = -1;
					continue;
				}
				nxt[i][w] = 24 * 60;
				FOR(j, 0, n[w]) {
					if (x[w][j] > i) {
						chkmin(nxt[i][w], x[w][j]);
					}
				}
			}
		}
		int ans = INF;
		FOR(s, 0, 2) {
			FOR(i, 0, 24 * 60 + 1) FOR(w, 0, 2) seg[i][w].init();
			FORd(t, 24 * 60 + 1, 0) FOR(k, 0, min(t, 12 * 60) + 1) FOR(w, 0, 2) {
				int& res = dp[t][k][w];
				res = INF;
				if (t == 24 * 60) {
					if (k == 12 * 60) {
						res = -(w != s);
						seg[k][w].upd(t, res);
					}
					continue;
				}
				int x = t - k;
				if (x >= 0 && x <= 12 * 60 && nxt[t][w] != -1) {
					res = seg[x][!w].query(t + 1, nxt[t][w]) + 1;
				}
				seg[k][w].upd(t, res);
			}
			chkmin(ans, dp[0][0][s]);
		}
		cout << ans << "\n";
	}
}

int main() {
    int JUDGE_ONLINE = 1;
    if (fopen("in.txt", "r")) {
        freopen("in.txt", "r", stdin);
    	freopen("out.txt", "w", stdout);
        JUDGE_ONLINE = 0;
    }
    else {
    	ios_base::sync_with_stdio(0); cin.tie(0);
    }
    solve();
    if (!JUDGE_ONLINE) {
    	//cout << "\nTime elapsed: " << 1000 * clock() / CLOCKS_PER_SEC << "ms\n";
    }
    return 0;
}
