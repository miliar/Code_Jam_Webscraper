#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int t;
	cin >> t;
	cout << std::setprecision(20);
	for (int testCase = 1; testCase <= t; testCase++) {
		int d, n;
		cin >> d >> n;
		double maxTime = 0.0;
		while (n--) {
			int k, s;
			cin >> k >> s;
			double time = double(d - k) / s;
			if (time > maxTime)
				maxTime = time;
		}
		cout << "Case #" << testCase << ": ";
		cout << (d / maxTime) << '\n';
	}
	return 0;
}
