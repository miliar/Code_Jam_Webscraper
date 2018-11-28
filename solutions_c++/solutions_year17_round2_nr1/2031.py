#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>

using namespace std;

double solve() {
	int d, n;
	cin >> d >> n;

	vector<int> kilo(n), speed(n);
	vector<double> secs(n, 0);
	for (int i = 0; i < n; i++) {
		cin >> kilo[i] >> speed[i];
		secs[i] = 1.0 * (d - kilo[i]) / speed[i];
	}

	double maxi = *max_element(secs.begin(), secs.end());
	return 1.0 * d / maxi;
}


int main() {

	int t;

	cin >> t;
	vector<double> ans(t, 0);

	for (int i = 0; i < t; i++) {
		ans[i] = solve();
	}

	for (int i = 0; i < t; i++) {
		printf("Case #%d: %.9f\n", i + 1, ans[i]);
	}
	return 0;
}
