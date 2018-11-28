#include <iostream>
#include <vector>
using namespace std;
int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int n, q;
		cin >> n >> q;
		vector<double> e(n), s(n);
		for (int i = 0; i < n; ++i) {
			cin >> e[i] >> s[i];
		}
		vector<double> d(n - 1);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				double x;
				cin >> x;
				if (j == i + 1) {
					d[i] = x;
				}
			}
		}
		int u, v;
		cin >> u >> v;

		vector<double> t(n), l(n), tn(n), ln(n);
		for (int i = 0; i < n - 1; ++i) {
			for (int j = 0; j < n; ++j) {
				tn[j] = -1;
			}
			if (e[i] >= d[i] - 1e-9) {
				double mint = 0;
				if (i > 0) {
					bool first = true;
					for (int j = 0; j < n; ++j) {
						if (t[j] > 0 && (first || t[j] < mint)) {
							mint = t[j];
							first = false;
						}
					}
				}
				tn[i] = mint + d[i] / s[i];
				ln[i] = e[i] - d[i];
			}
			for (int j = 0; j < i; ++j) {
				if (t[j] > 0 && l[j] >= d[i] - 1e-9) {
					tn[j] = t[j] + d[i] / s[j];
					ln[j] = l[j] - d[i];
				}
			}
			t.swap(tn);
			l.swap(ln);
		}

		double best = -1;
		for (int i = 0; i < n - 1; ++i) {
			if (t[i] > 0 && (best < 0 || t[i] < best)) {
				best = t[i];
			}
		}
		cout.precision(10);
		cout << "Case #" << test << ": " << best << endl;
	}
}
