#include <iostream>
#include <cmath>
#include <vector>
#include <limits>
#include <iomanip>

using namespace std;
int main(int argc, char *argv[]) {
	int t;
	cin >> t;
	for (int _ = 0; _ < t; ++_) {
		double d, n;
		vector<double> k, s;
		cin >> d >> n;
		double _k, _s;
		for (int j = 0; j < n; ++j) {
			cin >> _k >> _s;
			k.push_back(_k);
			s.push_back(_s);
		}
		double ans = numeric_limits<double>::infinity();
		for (int i = 0; i < n; ++i) {
			double temp = d * s[i] / (d - k[i]);
			if (temp < ans)
				ans = temp;
		}
		cout << fixed << "Case #" << _ + 1 << ": " << ans << endl;
	}
}