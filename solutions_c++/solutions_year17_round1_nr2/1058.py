//This is getting accepted!
// I HATE BUG
// God Of The Bugs
// 12/11/2016
#include<bits/stdc++.h>

using namespace std;

#define ms(s, n) memset(s, n, sizeof(s))
#define FI first
#define SE second
#define pb push_back
#define mp make_pair
#define ll long long
#define sz(a) ((int)(a).size())
#define __builtin_popcount __builtin_popcounll
#define ld long double

typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<int, pii> ppi;

const double PI = acos(0) * 2;
const double EPS = 1e-8;
const ll MOD = 1e9 + 7;
const int MAXN = 1e5 + 5;
const int oo = 1e9;
const double foo = 1e30;

template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return __builtin_popcounll(s);}
template<class T> T sqr(T x) { return x * x; }

inline void addmod(int& a, int val, int p = MOD) {if ((a = (a + val)) >= p) a -= p;}
inline void submod(int& a, int val, int p = MOD) {if ((a = (a - val)) < 0) a += p;}
inline int mult(int a, int b, int p = MOD) {return (ll) a * b % p;}

int T, tc, vs[60][60], ans, n, p, a[60], c[60][60];
map<int, int> mm;
vector<int> v[60][60];

int cal(int u, int v) {
	int l = 0, r = 10000000 / v;
	while (l <= r) {
		int mid = (l + r) >> 1;
		double gg = mid * v;
		double lo = gg / 100. * 90.;
		double hi = gg / 100. * 110.;
		if (u >= lo && u <= hi) return mid;
		if (u < lo) r = mid - 1;
		else l = mid + 1;
	}
	return -1;
}

int main() {
//#ifndef ONLINE_JUDGE
//    freopen("inp.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//#endif

	cin >> T;
	while (T--) {
		cin >> n >> p;
		for (int i=0; i<n; i++) for (int j=0; j<p; j++) {
			vs[i][j] = 0;
			v[i][j].clear();
		}
		for (int i=0; i<n; i++) {
			cin >> a[i];
		}
		
		mm.clear();
		ans = 0;
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<p; j++) {
				cin >> c[i][j];
				v[i][j].pb(cal(c[i][j], a[i]));
				if (~v[i][j][0]) {
					mm[v[i][j][0]];
					for (int k=v[i][j][0]; k<10000000; k++) {
						double gg = k * a[i];
						double lo = gg / 100. * 90.;
						double hi = gg / 100. * 110.;
						if (c[i][j] >= lo && c[i][j] <= hi) {
							v[i][j].pb(k);
							mm[k];
						}
						else break;
					}
					for (int k=v[i][j][0]; k>0; k--) {
						double gg = k * a[i];
						double lo = gg / 100. * 90.;
						double hi = gg / 100. * 110.;
						if (c[i][j] >= lo && c[i][j] <= hi) {
							v[i][j].pb(k);
							mm[k];
						}
						else break;
					}
				}
			}
		}
		
		for (map<int, int>::iterator it=mm.begin(); it!=mm.end(); it++) {
			int cur = it->FI, find = 1;
			while (find) {
				find = 0;
				int ok = 0, cnt = 0;
				for (int i=0; i<n; i++) {
					ok = 0;
					for (int j=0; j<p; j++) if (!vs[i][j]) {
						for (int k=0; k<sz(v[i][j]); k++) {
							if (v[i][j][k] == cur) {
								cnt++;
								ok = 1;
								break;
							}
						}
						if (ok) break;
					}
					if (!ok) break;
				}
				if (ok && cnt == n) {
					ans++;
					find = 1;
					for (int i=0; i<n; i++) {
						for (int j=0; j<p; j++) if (!vs[i][j]) {
							int ok = 0;
							for (int k=0; k<sz(v[i][j]); k++) {
								if (v[i][j][k] == cur) {
									cnt++;
									ok = 1;
									vs[i][j] = 1;
									break;
								}
							}
							if (ok) break;
						}
					}
				}
			}
		}
		
		cout << "Case #" << ++tc << ": " << ans << endl;
	}


}

