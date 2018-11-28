#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <bitset>
#include <random>
#include <stack>
#include <list>
#include <unordered_set>
#include <unordered_map>
#include <ctime>

using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define sc second
#define fs first
#define mp make_pair
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()

template<class T> T sqr(T x) { return x*x; }
ld pi = 3.1415926535897932384626433832795;

ll mod = 1e9 + 7;

ll gcd(ll a, ll b) {
	return b ? gcd(b, a % b) : a;
}

ll _gcd(ll a, ll b, ll & x, ll & y) {
	if (a == 0) {
		x = 0; y = 1;
		return b;
	}
	ll _x1, _y1;
	ll d = _gcd(b%a, a, _x1, _y1);
	x = _y1 - (b / a) * _x1;
	y = _x1;
	return d;
}

ld binpow(ld a, ll n) {
	ld res = 1;
	while (n) {
		if (n & 1)
			res *= a;
		a *= a;
		n >>= 1;
		//a %= mod;
		//res %= mod;
	}
	return res;
}

const int N = 3e5 + 10;

ll hd, ad, hk, ak, B, D;

void solve(int test) {
	int ans = 1e9;
	cin >> hd >> ad >> hk >> ak >> B >> D;
	for (int i = 0; i < 111; i++) { //debuf counts
		for (int j = 0; j < 111; j++) { //buff counts
			int DC = i, BC = j;
			int step = 0;
			bool can = 1;
			ll attackD = ad, healthD = hd, healthK = hk, attackK = ak;
			for (;step < 311; step++) {
				if (healthD <= 0) {
					break;
				}
				bool ok = 1;
				if (healthD <= attackK && healthD != hd && healthK > attackD && healthD <= attackK - D*(DC > 0)) {
					healthD = hd;
					ok = 0;
				}
				if (ok && DC) attackK -= D, ok = 0, DC--;
				if (ok && BC) attackD += B, ok = 0, BC--;
				if (ok) {
					healthK -= attackD;
				}
				if (healthK <= 0) {
					ans = min(step+1, ans);
					break;
				}
				healthD -= attackK;
			}

		}
	}
	if (ans == 1e9) {
		printf("Case #%d: IMPOSSIBLE\n", test);
	} else 
	printf("Case #%d: %d\n", test, ans);
}


int main() {
	FILE *f1, *f2;
	freopen_s(&f1, "C-small-attempt2.in", "r", stdin);
	freopen_s(&f1, "C-small-attempt2.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
	return 0;
}