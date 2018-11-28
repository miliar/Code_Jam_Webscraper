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

const ll INF = (ll) 2e9;
const int MOD = (int) 1e9 + 7;

void solve () {
	ll n;
	cin >> n;
	string s;
	while (n) {
		s += char(n % 10 + '0');
		n /= 10;
	}
	reverse(s.begin(), s.end());
	for (int i = 1; i < s.size(); i++) {
		while (s[i] < s[i - 1]) {
			s[i - 1]--;
			for (int j = i; j < s.size(); j++)
				s[j] = '9';
			i--;
			if (i == 0)
				break;
		}
	}
	ll ans = 0;
	for (int i = 0; i < s.size(); i++) {
		ans = ans * 10 + s[i] - '0';
	}
	cout << ans << enter;
}

int main () {
	ios_base::sync_with_stdio(false);
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
}