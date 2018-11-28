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

pair<int, char> b[10];
pair<int, pair<int, char> > a[10];
int T, tc, n;

int main() {
//#ifndef ONLINE_JUDGE
//    freopen("inp.txt", "r", stdin);
//    freopen("out1.txt", "w", stdout);
//#endif

	cin >> T;
	while (T--) {
		cout << "Case #" << ++tc << ": ";
		cin >> n;
		for (int i=0; i<3; i++) {
			cin >> a[i].FI;
//			cout << a[i].FI << endl;
			cin >> b[i].FI;
		}
		a[0].SE.SE = 'R';
		b[0].SE = 'O';
		a[1].SE.SE = 'Y';
		b[1].SE = 'G';
		a[2].SE.SE = 'B';
		b[2].SE = 'V';
		
		a[0].SE.FI = 1;
		a[1].SE.FI = 2;
		a[2].SE.FI = 0;
		a[0].FI -= b[1].FI;
		a[1].FI -= b[2].FI;
		a[2].FI -= b[0].FI;
		
		int ok = 0;
		for (int i=0; i<3; i++) {
			if (a[i].FI < 0) {
				ok = 1;
				break;
			}
		}
		
		if (ok) {
			cout << "IMPOSSIBLE" << endl;
				continue;
		}
		
		sort(a, a + 3);
		if (a[2].FI > a[1].FI + a[0].FI) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		string ans = "";
		int rem = a[2].FI - a[1].FI;
		int rem1 = a[0].FI - rem;
		int p0 = 0, p1 = 0, p2 = 0;
		
		for (int i=0; i<rem1; i++) {
			ans.pb(a[1].SE.SE);
			if (!p1) {
				p1 = 1;
				for (int i=0; i<b[a[1].SE.FI].FI; i++) {
					ans.pb(b[a[1].SE.FI].SE);
					ans.pb(a[1].SE.SE);
				}
			}
			ans.pb(a[2].SE.SE);
			if (!p2) {
				p2 = 1;
				for (int i=0; i<b[a[2].SE.FI].FI; i++) {
					ans.pb(b[a[2].SE.FI].SE);
					ans.pb(a[2].SE.SE);
				}
			}
			ans.pb(a[0].SE.SE);
			if (!p0) {
				p0 = 1;
				for (int i=0; i<b[a[0].SE.FI].FI; i++) {
					ans.pb(b[a[0].SE.FI].SE);
					ans.pb(a[0].SE.SE);
				}
			}
		}
		
		for (int i=rem1; i<a[1].FI; i++) {
			ans.pb(a[1].SE.SE);
			if (!p1) {
				p1 = 1;
				for (int i=0; i<b[a[1].SE.FI].FI; i++) {
					ans.pb(b[a[1].SE.FI].SE);
					ans.pb(a[1].SE.SE);
				}
			}
			ans.pb(a[2].SE.SE);
			if (!p2) {
				p2 = 1;
				for (int i=0; i<b[a[2].SE.FI].FI; i++) {
					ans.pb(b[a[2].SE.FI].SE);
					ans.pb(a[2].SE.SE);
				}
			}
		}
		for (int i=0; i<rem; i++) {
			ans.pb(a[0].SE.SE);
			if (!p0) {
				p0 = 1;
				for (int i=0; i<b[a[0].SE.FI].FI; i++) {
					ans.pb(b[a[0].SE.FI].SE);
					ans.pb(a[0].SE.SE);
				}
			}
			ans.pb(a[2].SE.SE);
			if (!p2) {
				p2 = 1;
				for (int i=0; i<b[a[2].SE.FI].FI; i++) {
					ans.pb(b[a[2].SE.FI].SE);
					ans.pb(a[2].SE.SE);
				}
			}
		}
		if (!p0) {
			if (sz(ans) != 0 && b[a[0].SE.FI].FI > 0) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			p0 = 1;
			for (int i=0; i<b[a[0].SE.FI].FI; i++) {
				ans.pb(b[a[0].SE.FI].SE);
				ans.pb(a[0].SE.SE);
			}
		}
		if (!p1) {
			if (sz(ans) != 0 && b[a[1].SE.FI].FI > 0) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			p1 = 1;
			for (int i=0; i<b[a[1].SE.FI].FI; i++) {
				ans.pb(b[a[1].SE.FI].SE);
				ans.pb(a[1].SE.SE);
			}
		}
		if (!p2) {
			if (sz(ans) != 0 && b[a[2].SE.FI].FI > 0) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			p2 = 1;
			for (int i=0; i<b[a[2].SE.FI].FI; i++) {
				ans.pb(b[a[2].SE.FI].SE);
				ans.pb(a[2].SE.SE);
			}
		}
		cout << ans << endl;
	}
	

}

