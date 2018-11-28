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

void solve() {
	string s;
	cin >> s;
	bool b = true;
	while (b) {
		b = false;

		fore(i, 1, s.length()) {
			if (s[i] < s[i - 1]) {
				--s[i - 1];
				fill(s.begin() + i, s.end(), '9');

				b = true;
			}
		}
	}

	s.erase(0, min(s.find_first_not_of('0'), s.size() - 1));
	cout << s << endl;
}

int main() {
	ios_base::sync_with_stdio(false), cin.tie(NULL);

	int T; cin >> T;
	forn(tc, T) {
		cout << "Case #" << tc + 1 << ": ";
		solve();
	}

}