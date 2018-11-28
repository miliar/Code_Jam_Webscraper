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

int n, p, a[200], cnt[10], has[10], T, tc;

int main() {
//#ifndef ONLINE_JUDGE
//    freopen("inp.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//#endif

	cin >> T;
	while (T--) {
		cout << "Case #" << ++tc << ": ";
		cin >> n >> p;
		for (int i=0; i<n; i++) cin >> a[i];
		for (int i=0; i<4; i++) cnt[i] = 0;
		for (int i=0; i<n; i++) cnt[a[i] % p]++;
		int ans = cnt[0];
		if (p == 2) {
			ans += cnt[1] / 2 + cnt[1] % 2;
		}
		if (p == 3) {
			for (int i=0; i<3; i++) has[i] = cnt[i];
			int t1 = min(has[1], has[2]);
			ans += t1 + (has[1] - t1) / 3 + (has[2] - t1) / 3;
			has[1] -= t1;
			has[2] -= t1;
//			cout << has[1] << " "<< has[2] << endl;
			ans += (has[1] % 3 || has[2] % 3);
		}
		if (p == 4) {
			for (int i=0; i<4; i++) has[i] = cnt[i];
			int t1 = min(has[1], has[3]);
			int t2 = has[2] / 2;
			has[1] -= t1;
			has[3] -= t1;
			has[2] -= t2 * 2;
			int t3 = min(has[1] / 2, has[2]);
			has[1] -= t3 * 2;
			has[2] -= t3;
//			cout << t1 << " " << t2 << " "<< t3 << endl;
			ans += t1 + t2 + t3 + has[1] / 4 + has[3] / 4;
			ans += (has[1] % 4 || has[3] % 4 || has[2] % 2);
		}
		cout << ans << '\n';
	}


}

