#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int c = 1; c <= t; ++c) {
		double m = 0.0;
		int n;
		double d;
		cin >> d >> n;
		while(n--) {
			double k, s;
			cin >> k >> s;
			double ti = (d - k) / s;
			if (m < ti) m = ti;
		}

		printf("Case #%d: %f\n", c, d / m);
	}

	return 0;
}
