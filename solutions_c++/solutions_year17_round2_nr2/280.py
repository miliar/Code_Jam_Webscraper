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

int tdist[100][100];

void solve() {
	int n;
	cin >> n;
	int a, ab, b, bc, c, ac;
	// R, O, Y, G, B,  V
	cin >> a >> ab >> b >> bc >> c >> ac;
	if (ab > 0 && (ab > c || (ab == c && ab + c < n))) {
		cout << "IMPOSSIBLE\n";
		return;
	}
	if (ac > 0 && (ac > b || (ac == b && ac + b < n))) {
		cout << "IMPOSSIBLE\n";
		return;
	}
	if (bc > 0 && (bc > a || (bc == a && bc + a < n))) {
		cout << "IMPOSSIBLE\n";
		return;
	}
	if (ab + c == n || ac + b == n || bc + a == n) {
		if (ab != c || ac != b || bc != a) {
			cout << "IMPOSSIBLE\n";
			return;
		}
		string s;
		if (ab + c == n) {
			s = "OB";
		} else if (ac + b == n) {
			s = "VY";
		} else if (bc + a == n) {
			s = "RG";
		}
		for (int i = 0; i < n; i += 2) {
			cout << s;
		}
		cout << "\n";
		return;
	}
	a -= bc;
	b -= ac;
	c -= ab;
	int nn = a + b + c;
	if (max(a, max(b, c)) * 2 > nn) {
		cout << "IMPOSSIBLE\n";
		return;
	}
	vector<pair<int, char>> vv( { { a, 'R' }, { b, 'Y' }, { c, 'B' } });
	sort(vv.begin(), vv.end());
	string res(1, vv[1].second);
	vv[1].first--;
	for (int i = 0; vv[0].first + vv[1].first >= vv[2].first; i++) {
		res.push_back(vv[i % 2].second);
		vv[i % 2].first--;
	}
	res.push_back(vv[2].second);
	vv[2].first--;
	while (vv[2].first > 0) {
		if (vv[0].first > 0) {
			res.push_back(vv[0].second);
			vv[0].first--;
		} else {
			res.push_back(vv[1].second);
			vv[1].first--;
		}
		res.push_back(vv[2].second);
		vv[2].first--;
	}
//	cerr << res << "\n";
	for (int i = 0; i < n; i++) {
		if (res[i] == 'R' && bc > 0) {
			res.insert(res.begin() + i, 'G');
			res.insert(res.begin() + i, 'R');
			bc--;
		}
		if (res[i] == 'Y' && ac > 0) {
			res.insert(res.begin() + i, 'V');
			res.insert(res.begin() + i, 'Y');
			bc--;
		}
		if (res[i] == 'B' && ab > 0) {
			res.insert(res.begin() + i, 'O');
			res.insert(res.begin() + i, 'B');
			bc--;
		}
	}
	cout << res << "\n";
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
	for (int tt = 1; tt <= t; tt++) {
		cout << "Case #" << tt << ": ";
		solve();
	}
	return 0;
}
