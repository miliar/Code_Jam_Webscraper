#include <bits/stdc++.h>

using namespace std;

void main2() {
	int d, n;
	cin >> d >> n;
	double max_t = 0.0;
	for (int i = 0; i < n; i++) {
		int k, s;
		cin >> k >> s;
		max_t = max(max_t, ((double)d-k)/s);
	}
	cout << fixed << setprecision(9) << d/max_t << endl;
}

int main() {
	int t; cin >> t;
	for (int o = 1; o <= t; o++) {
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
