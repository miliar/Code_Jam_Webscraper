#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

void main() {
	int tn;
	cin >> tn;

	std::cout << setprecision(6) << fixed;

	for (int t = 1; t <= tn; ++t) {
		int n, k;
		cin >> n >> k;
		double u;
		cin >> u;
		vector<double> p = vector<double>(n);
		//vector<double> px = vector<double>(n);
		double z = u;
		for (int i = 0; i < n; i++) {
			cin >> p[i];
			z += p[i];
		}
		z /= n;

		//sort(p.begin(), p.end());

		// Small
		// Bin search
		double l = 0, r = 1.0;
		double um = 0.0;
		while (fabs(um - u) > 1e-7) {
			double m = (l + r) / 2.0;
			um = 0;
			for (int i = 0; i < n; i++) {
				um += p[i] > m ? 0 : m - p[i];
			}
			if (um > u) {
				r = m;
			}
			else {
				l = m;
			}
		}

		double m = l; // (l + r) / 2.0;
		double prod = 1.0;
		for (int i = 0; i < n; i++) {
			prod *= p[i] > m ? p[i] : m;
		}

		cout << "Case #" << t << ": " << prod << endl;
		//printf(" %0.6lf", dist[v]);
	}
}