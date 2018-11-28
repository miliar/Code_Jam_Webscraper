#include <iostream>
#include <cstdio>
#include <algorithm>

// #include <map>
// #include <vector>
// #include <unordered_map>

using namespace std;

struct House {
	long k, s;
};

struct Comp {
	bool operator()(House &a, House &b) {
		return a.k < b.k;
	}
};

int solve() {
	double d, n, k, s;
	double max_time;

	cin >> d >> n;
	for (int i = 0; i < n; ++i) {
		cin >> k >> s;
		double time = (d - k) / s;
		if (time > max_time)
			max_time = time;
	}

	printf("%.10f\n", d / max_time);

	return 0;
}

int t;

int main() {
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}

	return 1;
}