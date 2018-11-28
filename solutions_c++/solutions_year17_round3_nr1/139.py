#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

const double pi = 3.141592653589793238;

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int n, k;
		cin >> n >> k;

		vector<double> r(n), h(n);
		vector<int> pos(n);
		for (int i = 0; i < n; ++i) {
			pos[i] = i;
			cin >> r[i] >> h[i];
		}

		sort(pos.begin(), pos.end(), [&r](int lhs, int rhs) {
			return r[lhs] > r[rhs];
		});

		vector<vector<double> > t(n);
		for (int i = 0; i < n; ++i) {
			t[i].resize(k + 1);
			t[i][1] = pi*r[pos[i]]*r[pos[i]] + 2*pi*r[pos[i]]*h[pos[i]];
			if (i == 0) {
				continue;
			}
			if (t[i][1] < t[i - 1][1]) {
				t[i][1] = t[i - 1][1];
			}
			for (int j = 2; j <= k; ++j) {
				t[i][j] = 2*pi*r[pos[i]]*h[pos[i]] + t[i - 1][j - 1];
				if (t[i][j] < t[i - 1][j]) {
					t[i][j] = t[i - 1][j];
				}
			}
		}

		cout.precision(10);
		cout << "Case #" << test << ": " << t[n - 1][k] << endl;
	}
}
