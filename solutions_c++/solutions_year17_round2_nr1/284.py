#include <bits/stdc++.h>
using namespace std;

void gettl(bool b) {
	int crt = 1;
	if (!b) {
		for (int i = 0; i < (int) 2e9; i++) {
			crt *= 17;
		}
		gettl(false);
	}
}

#ifndef _DEBUG
#define ass(_Expr) ((void)0)
#define dout(...) ((void)0)
#else
#define dout(...) cout << __VA_ARGS__; cout.flush()
#define ass(_Expr) assert(_Expr);
#endif

typedef long long ll;
typedef double ld;
const int INF = 2e9;
const ll LINF = 2e18;
const ll MOD = 1e9 + 9;
const int PRIME = 29;
const ld EPS = 1e-10;
const ld PI = 3.14159265358979323846;

ll gcd(ll a, ll b, ll & x, ll & y) {
	if (a == 0) {
		x = 0;
		y = 1;
		return b;
	}
	ll x1, y1;
	ll d = gcd(b % a, a, x1, y1);
	x = y1 - (b / a) * x1;
	y = x1;
	return d;
}

vector<bool> fb;

vector<int> mindiv;

vector<ll> primes, divs = { 1 };
vector<int> psize, total;

vector<int> rev;

void solve() {
	int n, d;
	cin >> d >> n;
	ld x = 0;
	for(int i = 0; i < n; i++){
		int ki, si;
		cin >> ki >> si;
		x = max(x, ld(d - ki) / si);
	}
	cout << ld(d) / x << "\n";
}

int main() {
//	ios_base::sync_with_stdio(false);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
//	freopen("keepcounted.in", "r", stdin);
//	freopen("keepcounted.out", "w", stdout);
#endif
	int t;
	cin >> t;
	cout << fixed << setprecision(10);
	for(int tt = 1; tt <= t; tt++){
		cout << "Case #" << tt << ": ";
		solve();
	}
	return 0;
}
