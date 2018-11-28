#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(void) {

	int test;
	cin >> test;

	for (int Case = 1; Case <= test; ++Case) {

		int n, P;
		cin >> n >> P;

		vector<int> cnt(P, 0);
		for (int i = 0; i < n; ++i) {
			int val;
			cin >> val;
			cnt[val % P]++;
		}

		int ans = 0;
		for (int i = 0; i < P; ++i) {
			if (cnt[i] == 0) continue;
			--cnt[i];
			int best = 0;
			if (P == 2) {
				best = 1 + cnt[0] + cnt[1] / 2;
			} else if (P == 3) {
				int x = min(cnt[1], cnt[2]);
				for (int j = 0; j <= x; ++j) {
					best = max(best, j + (cnt[1]-j) / 3 + (cnt[2]-j) / 3);
				}
				best += 1 + cnt[0];
				// best = 1 + cnt[0] + x + (cnt[1]-x) / 3 + (cnt[2]-x) / 3;
			} else if (P == 4) {
				for (int j = 0; j <= cnt[2] and 2*j <= cnt[1]; ++j) {
					for (int jj = 0; jj <= cnt[2]-j and 2*jj <= cnt[3]; ++jj) {
						int val = min(cnt[1] - 2*j, cnt[3] - 2*jj);
						for (int k = 0; k <= val; ++k) {
							int pos = j + jj + (cnt[2]-j-jj) / 2;
							pos += k + (cnt[1]-2*j-k) / 4 + (cnt[3]-2*jj-k) / 4;
							best = max(best, pos);
						}
					}
				}
				best += 1 + cnt[0];
			}

			ans = max(ans, best);
			++cnt[i];
		}

		cout << "Case #" << Case << ": " << ans << endl;
		cerr << Case << endl;
	}
	return 0;
}