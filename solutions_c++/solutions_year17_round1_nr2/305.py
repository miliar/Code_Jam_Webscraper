#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

typedef pair<int, int> PII;

PII servings(int q, int r) {
	int x_1 = (q * 10 + r * 11 - 1) / (r * 11); // round up
	int x_2 = (q * 10) / (r * 9); // round down
	return make_pair(x_1, x_2);
}

int main() {
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		int n, p; cin >> n >> p;
		vector<int> r(n);
		for (int i = 0; i < n; ++i) cin >> r[i];
		vector<vector<int> > q(n);
		for (int i = 0; i < n; ++i) {
			q[i].resize(p);
			for (int j = 0; j < p; ++j) {
				cin >> q[i][j];
			}
			sort(q[i].begin(), q[i].end());
		}

		int ans = 0;

		vector<int> pointers(n, 0);
		bool okay = true;
		while (okay) {
			vector<PII> pp(n);
			for (int i = 0; i < n; ++i) {
				if (pointers[i] == p) {
					okay = false; break;
				}
				pp[i] = servings(q[i][pointers[i]], r[i]);
				if (pp[i].first > pp[i].second) { // unusable package
					pointers[i]++;
					i--; // redo
				}
			}
			if (!okay) break;

			PII smallest = pp[0];
			int smallest_idx = 0;
			for (int i = 1; i < n; ++i) {
				if (pp[i] < smallest) {
					smallest = pp[i];
					smallest_idx = i;
				}
			}

			bool good_package = true;
			for (int i = 0; i < n; ++i) {
				// if ranges overlap
				if (!(pp[i].first <= smallest.second && smallest.second <= pp[i].second)) {
					good_package = false; break;
				}
			}
			if (good_package) {
				ans++;
				for (int i = 0; i < n; ++i) pointers[i]++; // sure, package them together. greedy is best.
			} else {
				pointers[smallest_idx]++; // this is unusable, then
			}

			for (int i = 0; i < n; ++i) {
				if (pointers[i] >= p) {
					okay = false; break;
				}
			}
		}

		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}