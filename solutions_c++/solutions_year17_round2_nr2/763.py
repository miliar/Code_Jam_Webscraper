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

string solve(int n, vector<int> c) {
	string mp = "RYBOVG";
	string ans;
	string imp = "IMPOSSIBLE";
	for (int i = 0; i < 3; ++i) {
		if (c[i] + c[5 - i] == n) {
			if (c[i] == c[5 - i]) {
				for (int j = 0; j < n / 2; ++j) {
					ans.push_back(mp[i]);
					ans.push_back(mp[5 - i]);
				}
				return ans;
			}
			else {
				return imp;
			}
		}
	}
	for (int i = 0; i < 3; ++i) {
		if (c[5 - i] > 0 && c[i] <= c[5 - i]) {
			return imp;
		}
	}
	string block[3];
	for (int i = 0; i < 3; ++i) {
		int cnt = c[5 - i];
		if (cnt > 0) {
			block[i].push_back(mp[i]);
			for (int j = 0; j < c[5 - i]; ++j) {
				block[i].push_back(mp[5 - i]);
				block[i].push_back(mp[i]);
			}
			c[5 - i] = 0;
			c[i] -= cnt + 1;
		}
	}
	for (int i = 0; i < 3; ++i) {
		if (block[i].size() > 0)
			c[i]++;
	}
	int nn = c[0] + c[1] + c[2];
	if (2 * c[0] > nn || 2 * c[1] > nn || 2 * c[2] > nn) {
		return imp;
	}
	vector<int> ord = { 0, 1, 2 };
	sort(ord.begin(), ord.end(), [&](int a, int b) {return c[a] > c[b]; });
	int cnt = c[ord[1]] + c[ord[2]] - c[ord[0]];
	for (int i = 0; i < cnt; ++i) {
		ans.push_back(mp[ord[0]]);
		ans.push_back(mp[ord[1]]);
		ans.push_back(mp[ord[2]]);
	}
	c[ord[0]] -= cnt;
	c[ord[1]] -= cnt;
	c[ord[2]] -= cnt;
	for (int i = 0; i < c[ord[1]]; ++i) {
		ans.push_back(mp[ord[0]]);
		ans.push_back(mp[ord[1]]);
	}
	for (int i = 0; i < c[ord[2]]; ++i) {
		ans.push_back(mp[ord[0]]);
		ans.push_back(mp[ord[2]]);
	}
	for (int i = 0; i < 3; ++i) {
		if (block[i].size() > 0) {
			int pos = ans.find(mp[i]);
			ans.replace(pos, 1, block[i]);
		}
	}
	return ans;
}


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
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		vector<int> c = { r, y, b, o, v, g };
		cout << solve(n, c) << endl;
	}
}