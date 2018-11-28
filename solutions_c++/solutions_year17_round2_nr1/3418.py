#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cout << "Case #" << t + 1 << ": ";

		int d, n;
		cin >> d >> n;
		double a = 0;
		for (int i = 0; i < n; i++) {
			int k, s;
			cin >> k >> s;
			a = max(a, 1.0 * (d - k) / s);
		}
		cout << fixed << setprecision(6) << d / a << endl;
	}
	return 0;
}
