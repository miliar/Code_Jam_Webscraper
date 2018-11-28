#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
#ifdef _DEBUG
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << setprecision(0) << t << ": ";

		double mr = 0;

		int d, n;
		cin >> d >> n;
		for (int i = 0; i < n; i++) {
			double a, b;
			cin >> b >> a;
			double r = (d - b) / a;
			mr = max(mr, r);
		}

		cout << fixed << setprecision(8) << (d / mr) << endl;
	}
	return 0;
}