#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int n, k;
		cin >> n >> k;
		double u;
		cin >> u;
		vector<double> p(n);
		for (int i = 0; i < n; ++i) {
			cin >> p[i];
		}

		sort(p.begin(), p.end());
		int cur = 0;
		while (u >= 1e-12) {
			while (cur < n - 1 && p[cur] >= p[cur + 1] - 1e-12) {
				++cur;
			}
			double next;
			if (cur == n - 1 || (p[cur + 1] - p[cur])*(cur + 1) > u) {
				next = p[cur] + u / (cur + 1);
				u = 0.0;
			} else {
				next = p[cur + 1];
				u -= (p[cur + 1] - p[cur])*(cur + 1);
			}
			for (int i = 0; i <= cur; ++i) {
				p[i] = next;
			}
		}
		
		double ans = 1.0;
		for (int i = 0; i < n; ++i) {
			ans *= p[i];
		}
		
		cout.precision(10);
		cout << "Case #" << test << ": " << ans << endl;
	}
}
