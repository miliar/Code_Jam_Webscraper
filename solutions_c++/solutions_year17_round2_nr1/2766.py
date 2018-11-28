#include <iostream>

using namespace std;

void main() {
	int tn;
	cin >> tn;

	for (int t = 1; t <= tn; ++t) {
		int d, n;
		int k, s;
		double tmax = -1;
		cin >> d >> n;
		for (int i = 0; i < n; ++i) {
			cin >> k >> s;
			double t = double(d - k) / s;
			if (t > tmax) {
				tmax = t;
			}
		}

		//cout << "Case #" << t << ":" << d / tmax << endl;
		printf("Case #%d: %0.6lf\n", t, d / tmax);
	}
}