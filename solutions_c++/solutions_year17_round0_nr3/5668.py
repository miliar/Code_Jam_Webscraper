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
	return a.first > b.first || (a.first == b.first && a.second > b.second);
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

set <int> w;

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	int ts;
	cin >> ts;
	for (int t = 1; t <= ts; t++) {
		int n, k;
		cin >> n >> k;
		w.clear();
		w.insert(1);
		w.insert(n + 2);
		par ans;
		for (int i = 0; i < k; i++) {
			ans = { -1, -1 };
			int pos = -1;
			auto k = w.begin();
			int prev = *k;
			k++;
			for (; k != w.end(); k++) {
				int cur = *k;
				int len = cur - prev - 1;
				par nw;
				if (len % 2 == 0) nw = { len / 2 - 1, len / 2 }; else nw = { len / 2, len / 2 };
				if (nw < ans) {
					ans = nw;
					pos = prev + len / 2 + 1;
				}
				prev = cur;
			}
			w.insert(pos);
		}
		cout << "Case #" << t << ": " << ans.second << " " << ans.first << endl;
	}
	return 0;
}