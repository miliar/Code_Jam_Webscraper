#include <bits/stdc++.h>
#include <ctime>

using namespace std;

#define space ' '
#define enter "\n"
#define fi first
#define se second
#define mp make_pair
#define ALL(x) x.begin(), x.end()

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef set <int> si;
typedef map <int, int> mii;
typedef pair <ll, ll> pll;
typedef vector <int> vi;
typedef vector <pii> vii;
typedef long double ld;

template <class T>
T sqr (T x) {
	return x * x;
}

template <class T>
T gcd (T a, T b) {
	return b ? gcd(b, a % b) : a;
}

template <class T1, class T2>
T1 chmin (T1 & x, const T2 & y) {
	if (T1(y) < x)
		return x = y;
	return x;
}

template <class T1, class T2>
T1 chmax (T1 & x, const T2 & y) {
	if (T1(y) > x)
		return x = y;
	return x;
}

template <class T1, class T2>
ostream & operator << (ostream & os, const pair <T1, T2> & p) {
	return os << '(' << p.fi << ", " << p.se << ')';
}

template <class T>
ostream & operator << (ostream & os, const vector <T> & v) {
	os << '{';
	bool was = false;
	for (const T & x : v) {
		if (was)
			os << ", ";
		was = true;
		os << x;
	}
	os << '}';
	return os;
}

template <class T>
ostream & operator << (ostream & os, const set <T> & v) {
	os << '[';
	bool was = false;
	for (const T & x : v) {
		if (was)
			os << ", ";
		was = true;
		os << x;
	}
	os << ']';
	return os;
}

template <class T>
ostream & operator << (ostream & os, const multiset <T> & v) {
	os << '[';
	bool was = false;
	for (const T & x : v) {
		if (was)
			os << ", ";
		was = true;
		os << x;
	}
	os << ']';
	return os;
}

template <class T1, class T2>
ostream & operator << (ostream & os, const map <T1, T2> & m) {
	os << '<';
	bool was = false;
	for (const auto & x : m) {
		if (was)
			os << ", ";
		was = true;
		os << x;
	}
	os << '>';
	return os;
}

const int INF = (int) 2e9;
const ll LINF = (ll) 2e18;
const int MOD = (int) 1e9 + 7;
const long double Pi = M_PI;
const int MAXN = (int) 55;
const double EPS = 1e-8;

int n, k;
double u, p[MAXN];

void solve () {
	cin >> n >> k >> u;
	for (int i = 1; i <= n; i++) {
		cin >> p[i];
	}
	sort(p + 1, p + n + 1);
	p[n + 1] = 1;
	while (u > EPS) {
		int l = 1;
		int r = n;
		for (int i = 2; i <= n; i++) {
			if (abs(p[i] - p[i - 1]) < EPS)
				continue;
			else {
				r = i - 1;
				break;
			}
		}
		double need = min(p[r + 1] - p[r], u / r);
		u -= need * r;
		for (int i = 1; i <= r; i++) {
			p[i] += need;
		}
		if (r == n)
			break;
	}
	double ans = 1;
	for (int i = 1; i <= n; i++) {
		ans *= (p[i]);
	}
	cout << fixed << setprecision(8) << ans;
}

int main () {
	freopen("d://Documents//CLion//cfr 407//input.txt", "r", stdin);
	freopen("d://Documents//CLion//cfr 407//output.txt", "w", stdout);
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int iter = 1; iter <= T; iter++) {
		cout << "Case #" << iter << ": ";
		solve();
		cout << enter;
	}
}

/*
1
3 4
0 10
1420 1440
90 100
550 600
900 950
100 150
1050 1400
*/