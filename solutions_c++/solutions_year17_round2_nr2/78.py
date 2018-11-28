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

		int n;
		int r, y, b;
		int o, g, v;
		cin >> n >> r >> o >> y >> g >> b >> v;

		// modifications for large
		if(o > b || g > r || v > y) {
			cout << "IMPOSSIBLE\n";
			continue;
		}

		b -= o;
		r -= g;
		y -= v;

		int m = b + r + y;

		// solve small
		if(r + r > m || y + y > m || b + b > m) {
			cout << "IMPOSSIBLE\n";
			continue;
		}

		// extra condition
		if(o > 0 && b == 0) {
			cerr << "extra case " << endl;
			if(n == 2 * o) {
				string ans;
				while(o--) ans.push_back('O'), ans.push_back('B');
				cout << ans << "\n";
			} else
				cout << "IMPOSSIBLE\n";
			continue;
		}
		if(g > 0 && r == 0) {
			cerr << "extra case " << endl;
			if(n == 2 * g) {
				string ans;
				while(g--) ans.push_back('G'), ans.push_back('R');
				cout << ans << "\n";
			} else
				cout << "IMPOSSIBLE\n";
			continue;
		}
		if(v > 0 && y == 0) {
			cerr << "extra case " << endl;
			if(n == 2 * v) {
				string ans;
				while(v--) ans.push_back('V'), ans.push_back('Y');
				cout << ans << "\n";
			} else
				cout << "IMPOSSIBLE\n";
			continue;
		}

		// red and yellow interleaved
		string ans;
		if(r <= y) {
			for(int i = 0; i < r; ++i) ans.push_back('Y'), ans.push_back('R');
			for(int i = r; i < y; ++i) ans.push_back('Y');
		} else {
			for(int i = 0; i < y; ++i) ans.push_back('R'), ans.push_back('Y');
			for(int i = y; i < r; ++i) ans.push_back('R');
		}

		// now interleave blue
		int pos = ans.size();
		for(int i = 0; i < b; ++i) {
			ans.insert(pos, 1, 'B');
			--pos;
		}

		// insert two coloured horses
		for(int pos = ans.size() - 1; pos >= 0; --pos) {
			while(ans[pos] == 'B' && o > 0) {
				ans.insert(pos, "BO");
				--o;
			}
			while(ans[pos] == 'R' && g > 0) {
				ans.insert(pos, "RG");
				--g;
			}
			while(ans[pos] == 'Y' && v > 0) {
				ans.insert(pos, "YV");
				--v;
			}
		}

		assert(o == 0 && g == 0 && v == 0);

		cout << ans << endl;

		assert(ans.size() == n);

		// check duplicates
		for(int i = 0; i < ans.size() - 1; ++i) assert(ans[i] != ans[i + 1]);
		assert(ans[0] != ans[n - 1]);
	}
	return 0;
}
