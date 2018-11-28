#define HEADER_H
//#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
using ull          = unsigned long long;
using ll           = long long;
using ld           = long double;
using vi           = vector<ll>;
using vvi          = vector<vi>;
using vb           = vector<bool>;
using ii           = pair<ll, ll>;
constexpr bool LOG = true;
void Log() {
	if(LOG) cerr << "\n";
}
template <class T, class... S>
void Log(T t, S... s) {
	if(LOG) cerr << t << "\t", Log(s...);
} /* ============== END OF HEADER ============== */

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		ll n, k;
		cin >> n >> k;

		// map width to count
		map<ll, ll> m;
		m[n] = 1;

		while(k > 0) {
			auto cur = *--m.end();
			ll width = cur.first;
			ll count = cur.second;
			m.erase(--m.end());
			ll l = (width - 1) / 2;
			ll r = width / 2;
			if(k <= count) {
				cout << r << ' ' << l << endl;
				break;
			}

			k -= count;
			m[l] += count;
			m[r] += count;
		}
	}
	return 0;
}
