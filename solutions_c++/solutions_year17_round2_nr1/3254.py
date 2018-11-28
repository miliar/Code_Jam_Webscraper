#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;

	for (int c = 1; c <= t; ++c) {
		// scan input
		double d;
		int n;
		cin >> d;
		cin >> n;

		vector<int> k (n + 1);
		vector<int> s (n + 1);
		vector<double> time(n+1);
		double max_t = -1;
		for (int i = 1; i <= n; ++i) {
			cin >> k[i];
			cin >> s[i];
			time[i] = (d - k[i]) / s[i];
			if (max_t < time[i]) {
                max_t = time[i];
			}
		}

		double answer = d / max_t;

		// output
		// cout << "Case #" << c << ": " << answer << endl;
		printf("Case #%d: %f\n", c, answer);
	}

	return 0;
}
