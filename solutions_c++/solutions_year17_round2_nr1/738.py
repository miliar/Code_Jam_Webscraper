#include <bits/stdc++.h>

using namespace std;

void runTestCase(int t) {
	int d, n;
	cin >> d >> n;

	vector<int> horses(n);
	vector<int> speeds(n);

	for(int i = 0; i < n; i++) {
		cin >> horses[i];
		cin >> speeds[i];
	}

	double endTime = double(d - horses[0]) / speeds[0];
	for(int i = 1; i < n; i++) {
		endTime = max(double(d - horses[i]) / speeds[i], endTime);
	}

	cout << "Case #" << t << ": ";
	cout << d / endTime << endl;
}

int main() {
	int t;
	cin >> t;

	cout << setprecision(16);
	cout << fixed;

	for(int i = 1; i <= t; i++) {
		runTestCase(i);
	}

	return 0;
}
