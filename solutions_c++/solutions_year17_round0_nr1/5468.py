#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <initializer_list>
#include <unordered_set>
#include <unordered_map>
#include <cassert>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair <int, int> par;
typedef pair <ll, ll> parll;
int const INF = 1e9 + 7;
ll const LLINF = 1e18 + 7;
ld const eps = 1e-8;
ld const PI = acos(-1);
ll const p_hash = 257;
ll const mod = 1e9 + 9;
bool operator == (par a, par b) {
	return (a.first == b.first && a.second == b.second);
}
par operator + (par a, par b) {
	return{ a.first + b.first, a.second + b.second };
}
par operator - (par a, par b) {
	return{ a.first - b.first, a.second - b.second };
}
bool operator < (par const& a, par const& b) {
	return a.first < b.first || (a.first == b.first && a.second < b.second);
}
istream& operator >> (istream& in, par & a) {
	return (in >> a.first >> a.second);
}
ostream& operator << (ostream& ou, par a) {
	return (ou << a.first << " " << a.second << endl);
}
namespace std {
	template <>
	struct hash <par> {
		std::size_t operator ()(const par& a) const {
			using std::size_t;
			using std::hash;
			return (1LL * hash<int>()(a.first) * p_hash + 1LL * hash<int>()(a.second)) % mod;
		}
	};
}
bool eq(ld const& a, ld const& b) {
	return (a - b < eps && a - b > -eps);
}
bool less(ld const& a, ld const& b) {
	return (a - b < -eps);
}

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans = 0;
		bool un = false;
		for (int j = 0; j < s.size(); j++) {
			if (s[j] == '-') {
				if (j + k > s.size()) {
					un = true;
					break;
				} else {
					ans++;
					for (int f = j; f < j + k; f++) {
						if (s[f] == '-') s[f] = '+'; else s[f] = '-';
					}
				}
			}
		}
		cout << "Case #" << i + 1 << ": ";
		(un) ? cout << "IMPOSSIBLE" : cout << ans;
		cout << endl;
	}
	return 0;
}