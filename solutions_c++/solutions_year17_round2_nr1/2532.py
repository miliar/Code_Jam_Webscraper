#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
	ifstream cin("A-large.in");
	ofstream cout("output.txt");

	int T, n, d, p, s, k, i, j;
	cin >> T;

	for (k = 1; k <= T; ++k) {
		cin >> d >> n;

		double ans = 0;

		for (i = 0; i < n; ++i) {
			cin >> p >> s;
			ans = max(ans, (double)(d - p) / s);
		}

		cout << fixed << setprecision(10) << "Case #" << k << ": " << d / ans << endl;
	}

	cin.close();
	cout.close();
	return 0;
}