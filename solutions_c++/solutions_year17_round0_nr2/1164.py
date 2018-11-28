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

		string n;
		cin >> n;
		int l = n.size();

		// is n increasing?
		bool inc = true;
		int i    = 0;
		for(; i < l - 1; ++i) {
			if(n[i + 1] < n[i]) {
				inc = false;
				break;
			}
		}
		if(inc) {
			cout << n << endl;
			continue;
		}

		// find digit to decrease
		int k;
		for(k = i; k >= 0; --k) {
			if(n[k] > '1') break;
		}
		if(k < 0) {
			// n = 11111110?????
			// -> ans = 99999
			cout << string(l - 1, '9') << endl;
			continue;
		}

		char c = n[k];
		int m;
		for(m = k; m >= 0; --m) {
			if(n[m] == c)
				--n[m];
			else
				break;
		}
		for(int i = m + 2; i < l; ++i) n[i] = '9';

		cout << n << endl;
	}
	return 0;
}
