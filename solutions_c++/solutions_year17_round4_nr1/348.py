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
	int test;
	cin >> test;
	for (int tst = 1; tst <= test; ++tst) {
		cout << "Case #" << tst << ": ";
		int n, p;
		cin >> n >> p;
		vector<int> g(n);
		cin >> g;
		vector<int> cnt(p, 0);
		for (int i = 0; i < n; ++i) {
			cnt[g[i] % p]++;
		}
		if (p == 2) {
			cout << cnt[0] + (cnt[1] + 1) / 2;
		}
		else if (p == 3) {
			int ans = cnt[0];
			cnt[0] = 0;
			int m = min(cnt[1], cnt[2]);
			cnt[1] -= m;
			cnt[2] -= m;
			ans += m;
			ans += cnt[1] / 3;
			cnt[1] = cnt[1] % 3;
			ans += cnt[2] / 3;
			cnt[2] = cnt[2] % 3;
			if (cnt[1] + cnt[2] > 0)
				ans++;
			cout << ans;
		}
		else {
			int ans = cnt[0];
			ans += cnt[2] / 2;
			cnt[2] = cnt[2] % 2;
			int m = min(cnt[1], cnt[3]);
			cnt[1] -= m;
			cnt[3] -= m;
			ans += m;
			m = min(cnt[1] / 2, cnt[2]);
			cnt[1] -= 2 * m;
			cnt[2] -= m;
			ans += m;
			m = min(cnt[3] / 2, cnt[2]);
			cnt[3] -= 2 * m;
			cnt[2] -= m;
			ans += m;
			ans += cnt[1] / 4;
			cnt[1] = cnt[1] % 4;
			ans += cnt[3] / 4;
			cnt[3] = cnt[3] % 4;
			if (cnt[1] + cnt[2] + cnt[3] > 0)
				ans++;
			cout << ans;
		}
		cout << endl;
	}
}