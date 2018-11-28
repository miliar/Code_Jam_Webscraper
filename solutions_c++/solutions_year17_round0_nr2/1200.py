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
const ll MAX = 1000000LL * 1000000LL;
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

bool check(ll n) {
	int last = 9;
	while (n > 0) {
		int cur = n % 10;
		if (cur > last)
			return false;
		last = cur;
		n /= 10;
	}
	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
#ifdef DEBUG
	ifstream cin{ "input.txt" };
	ofstream cout{ "output.txt" };
#endif
	int tst;
	cin >> tst;
	for (int test = 0; test < tst; ++test) {
		cout << "Case #" << test + 1 << ": ";
		ll n;
		cin >> n;
		vector<ll> pows{1};
		for (int i = 0; i < 18; ++i) {
			pows.push_back(pows.back() * 10);
		}
		int pos = 0;
		while (!check(n)) {
			int digit = (n / pows[pos]) % 10;
			n -= (digit + 1) * pows[pos];
			++pos;
		}
		cout << n << endl;
	}
}