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

char a[33][33], b[33][33];

void solve(int test) {
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> a[i][j], b[i][j] = a[i][j];
		}
	}
	bool emptyrow = 0;
	for (int i = 0; i < n; i++) {
		bool yes = 1;
		for (int j = 0; j < m; j++) {
			yes &= a[i][j] == '?';
		}
		emptyrow |= yes;
	}
	if (emptyrow) {
		for (int i = 0; i < m; i++) {
			char c = '?';
			for (int j = 0; j < n; j++) {
				if (a[j][i] != '?') c = a[j][i];
				else if (c != '?') b[j][i] = c;
			}
			c = '?';
			for (int j = n - 1; j >= 0; j--) {
				if (a[j][i] != '?') c = a[j][i];
				else if (c != '?') b[j][i] = c;
			}
		}
	}
	else {
		for (int i = 0; i < n; i++) {
			char c = '?';
			for (int j = 0; j < m; j++) {
				if (a[i][j] != '?') c = a[i][j];
				else if (c != '?') b[i][j] = c;
			}
			c = '?';
			for (int j = m - 1; j >= 0; j--) {
				if (a[i][j] != '?') c = a[i][j];
				else if (c != '?') b[i][j] = c;
			}
		}
	}
	emptyrow = 0;
	for (int i = 0; i < n; i++) {
		bool yes = 1;
		for (int j = 0; j < m; j++) {
			yes &= b[i][j] == '?';
		}
		emptyrow |= yes;
	}
	if (emptyrow) {
		for (int i = 0; i < m; i++) {
			char c = '?';
			for (int j = 0; j < n; j++) {
				if (b[j][i] != '?') c = b[j][i];
				else if (c != '?') b[j][i] = c;
			}
			c = '?';
			for (int j = n - 1; j >= 0; j--) {
				if (b[j][i] != '?') c = b[j][i];
				else if (c != '?') b[j][i] = c;
			}
		}
	}
	bool emptycol = 0;
	for (int i = 0; i < m; i++) {
		bool yes = 1;
		for (int j = 0; j < n; j++) {
			yes &= b[j][i] == '?';
		}
		emptycol |= yes;
	}
	if (emptycol) {
		for (int i = 0; i < n; i++) {
			char c = '?';
			for (int j = 0; j < m; j++) {
				if (b[i][j] != '?') c = b[i][j];
				else if (c != '?') b[i][j] = c;
			}
			c = '?';
			for (int j = m - 1; j >= 0; j--) {
				if (b[i][j] != '?') c = b[i][j];
				else if (c != '?') b[i][j] = c;
			}
		}
	}
	printf("Case #%d:\n", test);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << b[i][j];
		}
		cout << '\n';
	}
}


int main() {
	FILE *f1, *f2;
	freopen_s(&f1, "A-large.in", "r", stdin);
	freopen_s(&f1, "A-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		if (i == 8)
			int ad = 12;
		solve(i);
	}
	return 0;
}