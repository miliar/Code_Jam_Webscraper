#include <iostream>
#include <vector>
using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		double d;
		int n;
		cin >> d >> n;

		double maxs;
		for (int i = 0; i < n; ++i) {
			double k, s;
			cin >> k >> s;
			double tt = (d - k) / s;
			double ss = d / tt;
			if (i == 0 || ss < maxs) {
				maxs = ss;
			}
		}

		cout.precision(10);
		cout << "Case #" << test << ": " << maxs << endl;
	}
}
