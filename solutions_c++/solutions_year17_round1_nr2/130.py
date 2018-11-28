#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>

using namespace std;
#define pii pair <int, int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define int long long
const int INF = 1e11;

int solve() {
	int n, p;
	cin >> n >> p;
	vector <int> r(n);
	for (auto & i : r)
		cin >> i;
	vector <vector <int> > q(n, vector <int> (p));
	for (auto & i : q)
		for (auto & j : i)
			cin >> j;
	vector <pii> evs;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < p; ++j) {
			int r1, r2;
			r2 = (q[i][j] * 10) / (9 * r[i]);
			r1 = (q[i][j] * 10 + 11 * r[i] - 1) / (11  * r[i]);
			//cout << "i is " << i << " " << r1 << ',' << r2 << endl;
			if (r1 <= r2) {
				evs.pb(mp(r1, -i - 1));
				evs.pb(mp(r2, i + 1));
			}
		}
	}
	sort(evs.begin(), evs.end());
	int ans = 0;
	vector <int> cnt(n, 0);
	vector <int> take(n, 0);
	for (auto i : evs) {
		if (i.ss < 0) {
			cnt[-i.ss - 1]++;
			continue;
		}
		int mn = INF;
		for (auto j : cnt)
			mn = min(mn, j);
		ans += mn;
		for (auto & j : cnt)
			j -= mn;
		for (auto & j : take)
			j += mn;

		if (take[i.ss - 1]) {
			take[i.ss - 1]--;
		} else {
			cnt[i.ss - 1]--;
		}
	}

	int mn = INF;
	for (auto j : cnt)
		mn = min(mn, j);
	ans += mn;
	return ans;
}

int32_t main() {
	freopen("testb.in", "r", stdin);
	freopen("testb.out", "w", stdout);
	int cc;
	cin >> cc;
	for (int i = 1; i <= cc; ++i) {
		cout << "Case #" << i << ": " << solve() << '\n';
	}
}