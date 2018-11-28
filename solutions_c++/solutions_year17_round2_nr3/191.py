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

int n, q, T, tc;
double d[200][200], e[200], s[200], tot[200], dp[200][200], fdp[200], c[200][200], nfdp[200], ans[200];

int main() {
//#ifndef ONLINE_JUDGE
//    freopen("inp.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//#endif

	cin >> T;
	while (T--) {
		cin >> n >> q;
		for (int i=0; i<n; i++) cin >> e[i] >> s[i];
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) cin >> d[i][j];
		}
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				c[i][j] = d[i][j];
				if (c[i][j] == -1) c[i][j] = foo;
			}
		}
		
		for (int k=0; k<n; k++) {
			for (int i=0; i<n; i++) {
				for (int j=0; j<n; j++) {
					if (c[i][k] + c[k][j] < c[i][j]) {
						c[i][j] = c[i][k] + c[k][j];
					}
				}
			}
		}
//		for (int i=0; i<n; i++) {
//			for (int j=0; j<n; j++) {
//				cout << c[i][j] << " ";
//			}
//			cout << endl;
//		}
		for (int tt=0; tt<q; tt++) {
			int x, y;
			cin >> x >> y;
			x--; y--;
			for (int i=0; i<n; i++) fdp[i] = foo;
			fdp[x] = 0;
			for (int k=0; k<2*n; k++) {
				for (int i=0; i<n; i++) nfdp[i] = fdp[i];
				for (int i=0; i<n; i++) {
					for (int j=0; j<n; j++) {
						if (c[j][i] <= e[j]) {
							nfdp[i] = min(nfdp[i], fdp[j] + c[j][i] / s[j]);
						}
					}
				}
				for (int i=0; i<n; i++) fdp[i] = nfdp[i];
			}
			ans[tt] = fdp[y];
		}
		cout << "Case #" << ++tc << ": ";
		for (int i=0; i<q; i++) {
			if (i) printf(" ");
			assert(ans[i] != foo);
			printf("%.12lf", ans[i]);
		}
		cout << endl;
	}


}

