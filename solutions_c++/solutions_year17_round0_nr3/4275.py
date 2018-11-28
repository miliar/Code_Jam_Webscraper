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


int main() {
	ios_base::sync_with_stdio(false), cin.tie(NULL);

	int T; cin >> T;
	forn(tc, T) {
		cout << "Case #" << tc + 1 << ": ";
		set<tuple<int, int, int>> q; // -sz, left, right

		int n, k;
		cin >> n >> k;

		q.insert(make_tuple(-n, 0, n - 1));
		int x, y;

		forn(i, k) {
			auto it = q.begin();
			int l, r, sz;
			tie(sz, l, r) = *it;
			sz = -sz;

			q.erase(it);

			int d = (l + r) / 2;
			if (d != l) {
				q.insert(make_tuple(l - d, l, d - 1));
			}
			if (d != r) {
				q.insert(make_tuple(d - r, d + 1, r));
			}

			x = max(d - l, r - d);
			y = min(d - l, r - d);
		}

		cout << x << ' ' << y << endl;
	}
	


}