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

int T;
ll n, k;

int main() {
//#ifndef ONLINE_JUDGE
//    freopen("inp.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//#endif

	int tc = 0;
	cin >> T;
	while (T--) {
		cin >> n >> k;
		ll cur = 1;
		
		ll cur1 = n;
		ll cur2 = -1;
		ll has1 = 1;
		ll has2 = 0;
		ll ans1;
		ll ans2;
		
		while (k > 0) {
//			cout << cur1 << " " << has1 << " " << cur2 << " " << has2 << endl;
			if (k <= has1) {
				ans1 = cur1 / 2;
				ans2 = (cur1 - 1) / 2;		
				break;
			}
			k -= has1;
			if (k <= has2) {
				ans1 = cur2 / 2;
				ans2 = (cur2 - 1) / 2;
				break;
			}
			k -= has2;
			
			ll ncur1 = -1, ncur2 = -1, nhas1 = 0, nhas2 = 0;
			
			if (cur1 % 2 == 0) {
				ncur1 = cur1 / 2;
				ncur2 = (cur1 - 1) / 2;
			}
			else if (cur2 % 2 == 0) {
				ncur1 = cur2 / 2;
				ncur2 = (cur2 - 1) / 2;
			}
			else {
				ncur1 = cur1 / 2;
				ncur2 = -1;
			}
			
			if (cur1 % 2 == 0) {
				nhas1 += has1;
				nhas2 += has1;
			}			
			else {
				nhas1 += has1 * 2;
			}
			
			if (cur2 % 2 == 0) {
				nhas1 += has2;
				nhas2 += has2;
			}
			else if (cur2 != -1) {
				nhas2 += has2 * 2;
			}
			
			cur1 = ncur1;
			cur2 = ncur2;
			has1 = nhas1;
			has2 = nhas2;
		}
		
		cout << "Case #" << ++tc << ": " << max(ans1, ans2) << " " << min(ans1, ans2) << endl;
	}

}

