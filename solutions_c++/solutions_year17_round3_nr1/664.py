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

const double PI = 3.141592653589793238463;

int main() {
	ios_base::sync_with_stdio(false), cin.tie(NULL);

	int T; cin >> T;
	forn(tc, T) {
		cout << "Case #" << tc + 1 << ": ";

		int n, k;
		cin >> n >> k;

		V<Pii> v(n); // <r, h>
		V<pair<double, int>> vh(n); // <area, index>
		forn(i, n)  {
			cin >> v[i].first >> v[i].second; 
			vh[i].first = 2 * PI * v[i].first * v[i].second;  // 2 * PI * r * h	
			vh[i].second = i;
		}

		sort(vh.rbegin(), vh.rend());

		double ans = -1;

		forn(i, n) {
			int r = v[i].first;
			int m = 0;
			double s = Pi * r * r;

			s += 2 * PI * v[i].first * v[i].second;
			++m;

			forn(j, n) {
				if (m == k) break;

				int rj = v[vh[j].second].first;
				if (rj > r || vh[j].second == i) continue;

				s += vh[j].first;
				++m;
			}

			if (m == k) {
				ans = max(ans, s);
			}
		}

		cout.precision(10);
		cout << fixed << ans << endl;
	}

}