#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cassert>
#include <cstdlib>
#include <climits>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

template <typename T> using V = vector<T>;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> Pii;

const double Pi = acos(-1.0);

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))

void solve()  {
	string s; 
	int k;
	cin >> s >> k;

	vector<char> vc(s.length() + 5);
	bool inv = false;
	int ans = 0;
	//cout << s << ' ' << k << endl;

	forn(i, s.length()) {
		if (vc[i]) {
			inv = !inv;
		}

		char ch = s[i];
		if (inv) ch = ch == '+' ? '-' : '+';

		if (ch == '-') {
			if (i + k <= s.length()) {
				++ans;
				inv = !inv;
				vc[i] = 0;
				vc[i + k] = 1;
			}
			else {
				cout << "IMPOSSIBLE" << endl;
				return;
			}
		}
	
	}
	cout << ans << endl;
}

int main() {
	ios_base::sync_with_stdio(false), cin.tie(NULL);

	int T; cin >> T;
	forn(tc, T) {
		cout << "Case #" << tc + 1 << ": ";
		solve();
	}

}