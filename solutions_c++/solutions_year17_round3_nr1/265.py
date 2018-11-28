#include <bits/stdc++.h>
using namespace std;

#ifdef HELTHAZAR
	#define DEBUG true
#else
	#define DEBUG false
#endif

#define dout if (DEBUG) cout

void solve() {
	int n, k;
	cin >> n >> k;

	vector<long long> r(n), h(n);
	vector<pair<long long, int> > rh;
	for (int i = 0; i < n; i++) {
		cin >> r[i] >> h[i];
		rh.push_back(make_pair(2 * r[i] * h[i], i));
	}

	sort(rh.begin(), rh.end());
	reverse(rh.begin(), rh.end());

	long long maxcover = 0;
	for (int i = 0; i < n; i++) {
		int cnt = 1;
		long long cover = r[i] * r[i] + 2 * r[i] * h[i];
		for (int j = 0; j < n && cnt < k; j++) {
			int index = rh[j].second;
			if (index == i) {
				continue;
			}
			if (r[index] <= r[i]) {
				cnt++;
				cover += rh[j].first;
			}
		}
		maxcover = max(maxcover, cover);
	}

	printf("%0.9lf", ((double) acos(-1.0) * maxcover));
}

int main() {
	int test;
	cin >> test;

	for (int t = 1; t <= test; t++) {
		printf("Case #%d: ", t);
		// cout << "Case #" << t << ": ";

		solve();

		// cout << endl;
		printf("\n");
	}
}
