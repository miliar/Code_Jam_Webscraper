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
const int MAXN = (int) 1e3 + 10;
const long double Pi = M_PI;

int n, k;
pair <int, int> a[MAXN];
double dp[MAXN][MAXN];

void solve () {
	long double ans = 0;
	for (int i = 1; i <= n + 1; i++) {
		for (int j = 0; j <= k + 1; j++) {
			dp[i][j] = 0;
		}
	}
	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		cin >> a[i].fi >> a[i].se;
	}
	sort(a + 1, a + n + 1);
	reverse(a + 1, a + n + 1);
//	for (int i = 1; i <= n; i++) {
//		cout << a[i].fi << ' ' << a[i].se << enter;
//	}
	for (int i = 1; i <= n; i++) {
		chmax(dp[i + 1][1], dp[i][0] + Pi * a[i].fi * a[i].fi + 2 * Pi * a[i].fi * a[i].se);
		for (int j = 1; j <= k; j++) {
			chmax(dp[i + 1][j + 1], dp[i][j] + 2 * Pi * a[i].fi * a[i].se);
			chmax(dp[i + 1][j], dp[i][j]);
		}
	}
	for (int i = 1; i <= n; i++) {
		chmax(ans, dp[i + 1][k]);
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