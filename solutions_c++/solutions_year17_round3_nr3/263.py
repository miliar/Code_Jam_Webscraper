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

	double u;
	cin >> u;

	vector<double> p(n);
	for (int i = 0; i < n; i++) {
		cin >> p[i];
	}
	p.push_back(1.0);

	sort(p.begin(), p.end());
	for (int i = 1; i <= n; i++) {
		double diff = (p[i] - p[i - 1]) * i;
		if (diff <= u) {
			u -= diff;
		}
		else {
			double prod = 1.0;
			for (int j = 0; j < i; j++) {
				prod *= p[i - 1] + u / i;
			}
			for (int j = i; j < n; j++) {
				prod *= p[j];
			}
			printf("%0.8lf", prod);
			return;
		}
	}

	printf("1.0");
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
