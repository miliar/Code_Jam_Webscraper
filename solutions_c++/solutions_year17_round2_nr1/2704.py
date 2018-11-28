#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int q = 1; q <= t; q++) {
		long long d, n;
		cin >> d >> n;
		double slowest_horse = DBL_MIN;
		for (int i = 0; i < n; i++) {
			long long k, s;
			cin >> k >> s;
			slowest_horse = max((d - k) / (double)s, slowest_horse);
		}
		cout << fixed << setprecision(6) << "Case #" << q << ": " << d / slowest_horse << endl;
	}
	return 0;
}
