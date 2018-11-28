#pragma comment(linker, "/STACK:216000000")
#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>
#include <set>
#include <bitset>
#include <sstream>
#include <array>
#include <iomanip>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef long double ld;
const ll MAX = 10000000LL * 10000000LL;
const ll MIN = numeric_limits<ll>::min();
const double PI = 3.14159265358979;
const ll MOD = 1000000007LL;

template<class T>
ostream& operator<<(ostream& out, vector<T>& v) {
	for (int i = 0; i < v.size(); ++i) out << v[i] << " ";
	return out;
}

template<class T>
istream& operator >> (istream& in, vector<T>& v) {
	for (int i = 0; i < v.size(); ++i) in >> v[i];
	return in;
}

template<class T>
T lexical_cast(string& s) {
	stringstream ss(s);
	T t;
	ss >> t;
	return t;
}

ll gcd(ll a, ll b) {
	return b ? gcd(b, a % b) : a;
}

ll cdiv(ll a, ll b) {
	return (a % b) ? (a / b + 1) : (a / b);
}

ll inv(ll n, ll mod) {
	ll pow = mod - 2;
	ll ans = 1;
	ll cur = n;
	while (pow > 0) {
		if (pow & 1) {
			ans *= cur;
			ans %= mod;
		}
		pow /= 2;
		cur *= cur;
		cur %= mod;
	}
	return ans;
}

template<class Cont> void sort(Cont& c) { sort(begin(c), end(c)); }
template<class Cont> void reverse(Cont& c) { reverse(begin(c), end(c)); }

/* ------------------------------------------------
------------------------------------------------- */



int main() {
	ios_base::sync_with_stdio(false);
#ifdef DEBUG
	ifstream cin{ "input.txt" };
	ofstream cout{ "output.txt" };
#endif
	int tsts;
	cin >> tsts;
	for (int tst = 0; tst < tsts; ++tst) {
		cout << "Case #" << tst + 1 << ": ";
		int n, q;
		cin >> n >> q;
		vector<ll> e(n), s(n);
		for (int i = 0; i < n; ++i) {
			cin >> e[i] >> s[i];
		}
		vector<vector<ll>> d(n, vector<ll>(n));
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				cin >> d[i][j];
				if (d[i][j] == -1)
					d[i][j] = MAX;
			}
		}
		int u, v;
		cin >> u >> v;
		u = 0, v = n - 1;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				for (int k = 0; k < n; ++k) {
					d[j][k] = min(d[j][k], d[j][i] + d[i][k]);
				}
			}
		}
		vector<ld> t(n, (ld)MAX);
		t[n - 1] = 0;
		for (int i = n - 2; i >= 0; --i) {
			for (int j = i + 1; j < n; ++j) {
				if (d[i][j] <= e[i])
					t[i] = min(t[i], (ld)1.0 * d[i][j] / s[i] + t[j]);
			}
		}
		cout << setprecision(6) << fixed << t[0] << endl;
	}
}