#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++) {
		double d, n;
		cin >> d >> n;

		double min_time = 0;
		for(int i = 0; i < n; i++) {
			double k, s;
			cin >> k >> s;
			min_time = max((d-k)/s, min_time);
		}

		cout << "Case #" << t << ": " <<  fixed << setprecision(6) << d/min_time << endl;
	}
}