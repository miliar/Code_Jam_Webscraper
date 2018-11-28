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

int T, tc, R, C, vs[30][30];
string s[30];

int main() {
//#ifndef ONLINE_JUDGE
//    freopen("inp.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//#endif

	cin >> T;
	while (T--) {
		cin >> R >> C;
		for (int i=0; i<R; i++) for (int j=0; j<C; j++) vs[i][j] = 0;
		for (int i=0; i<R; i++) cin >> s[i];
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				if (s[i][j] != '?' && !vs[i][j]) {
					int l = j, r = j, h = i, d = i;
					for (int k=j+1; k<C; k++) {
						if (s[i][k] != '?') {
							break;
						}
						r = k;
					}
					for (int k=j-1; k>=0; k--) {
						if (s[i][k] != '?') {
							break;
						}
						l = k;
					}
					for (int k=i+1; k<R; k++) {
						int ok = 0;
						for (int t=l; t<=r; t++) {
							if (s[k][t] != '?') {
								ok = 1;
								break;								
							}
						}
						if (ok) break;
						h = k;
					}
					for (int k=i-1; k>=0; k--) {
						int ok = 0;
						for (int t=l; t<=r; t++) {
							if (s[k][t] != '?') {
								ok = 1;
								break;								
							}
						}
						if (ok) break;
						d = k;
					}
//					cout << i << " " << j << " " << l << " " << r << endl;
					for (int k=d; k<=h; k++) {
						for (int t=l; t<=r; t++) {
							s[k][t] = s[i][j];
							vs[k][t] = 1;
						}
					}
				}
			}
		}
		
		cout << "Case #" << ++tc << ":" << endl;
		for (int i=0; i<R; i++) cout << s[i] << endl;
	}


}

