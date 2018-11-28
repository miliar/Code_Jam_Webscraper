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
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	for(int tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": ";

		int n;
		cin >> n;
		int p;
		cin >> p;
		array<int, 4> count;
		count.fill(0);
		while(n--) {
			int x;
			cin >> x;
			++count[x % p];
		}

		int ans = count[0];
		if(p == 2) {
			ans += (count[1] + 1) / 2;
		} else if(p == 3) {
			int j = min(count[1], count[2]);
			count[1] -= j;
			count[2] -= j;
			ans += j;
			ans += (count[1] + 2) / 3;
			ans += (count[2] + 2) / 3;
		} else {
			assert(p == 4);
			int j = min(count[1], count[3]);
			ans += j;
			count[1] -= j;
			count[3] -= j;

			int b2 = count[2] / 2;
			ans += b2;
			count[2] -= 2 * b2;

			// left with a00, a10, 00c, or 01c
			int x = max(count[1], count[3]);
			if(count[2] == 0) {
				ans += (x + 3) / 4;
			} else {
				assert(count[2] == 1);
				++ans;
				x -= 2;
				if(x >= 0) {
					ans += (x + 3) / 4;
				}
			}
		}

		cout << ans << endl;
	}

	return 0;
}
