#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int tst = 1; tst <= t; ++tst) {
		int n, k;
		double u;
		cin >> n >> k >> u;
		vector<double> v;
		for (int i = 0; i < n; ++i) {
			double pom;
			cin >> pom;
			v.push_back(pom);
		}
		v.push_back(1); ++n; ++k;
		sort(v.begin(), v.end());
		if (n == k) {
			double units_left = u;
			for (int i = 1; i < n && units_left > 0 && v[i-1] < 1; ++i) {
				double diff = v[i] - v[i-1];
				if (diff * i > units_left)
					diff = units_left / i;
				units_left -= diff*i;
				for (int j = 0; j < i; ++j)
					v[j] += diff;
			}
			double Prob = 1;
			for (int i = 0; i < n; ++i) Prob = Prob * v[i];

			cout.setf(ios::fixed);
			cout.precision(10);
			cout << "Case #" << tst << ": "<< Prob << "\n";
		}








		/*
		cout.setf(ios::fixed);
		cout.precision(10);
		cout << "Case #" << tst << ": " << "\n";*/
	}
	return 0;
}