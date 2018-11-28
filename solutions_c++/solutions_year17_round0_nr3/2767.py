#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	int T;
	long long int n, m, t, q, r;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> n >> m;
		t = 1;
		while (true) {
			if (t <= m && m <= 2 * t - 1) break;
			t *= 2;
		}
		q = (n - 2 * t + 1) / t;
		r = (n - 2 * t + 1) % t;
		if (m - t - r + 1 <= 0) {
			cout << "Case #" << i + 1 << ": ";
			cout << (q + 1) / 2 + (q + 1) % 2 << " " << (q + 1) / 2 << endl;
		}
		else {
			cout << "Case #" << i + 1 << ": ";
			cout << q / 2 + q % 2 << " " << q / 2 << endl;
		}
	}
}