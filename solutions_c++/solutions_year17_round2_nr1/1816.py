#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

double speed(int d, const vector<int> &k, const vector<int> &s) {
	int n = k.size();
	double t = -1;
	for (int i = 0; i < n; ++i) {
		if (k[i] >= d) continue;
		t = max<double>(t, (d - k[i]) / (double)s[i]);
	}
	if (t < 0)
		return numeric_limits<double>::max();
	return d / t;
}

int main(void) {
	cout.sync_with_stdio(false);
	int nTests;
	cin >> nTests;
	cout << fixed;
	cout.precision(7);
	for (int t = 1; t <= nTests; ++t) {
		int d, n;
		cin >> d >> n;
		vector<int> k(n), s(n);
		for (int i = 0; i < n; ++i) {
			cin >> k[i] >> s[i];
		}
		cout << "Case #" << t << ": " << speed(d, k, s) << endl;
	}
	return 0;
}
