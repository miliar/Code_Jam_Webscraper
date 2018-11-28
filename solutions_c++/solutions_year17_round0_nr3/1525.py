#include <bits/stdc++.h>

using namespace std;

typedef long long dint;

void sovC(dint n, dint c1, dint c2, dint k) {
	if (k <= c1) {
		cout << (n >> 1) << ' ' << ((n - 1)>> 1) << endl;
	} else if (k <= c1 + c2) {
		cout << ((n - 1) >> 1) << ' ' << ((n - 2)>> 1) << endl;
	} else {
		dint nc1, nc2;
		if (n & 1) {
			nc1 = c1 * 2 + c2;
			nc2 = c2;
		} else {
			nc1 = c1;
			nc2 = c1 + c2 * 2;
		}
		sovC((n >> 1), nc1, nc2, k - c1 - c2);
	}
}

int main() {
	freopen(".in", "r", stdin);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++ i) {
		dint n, k;
		cin >> n >> k;
		cout << "Case #" << i << ": ";
		sovC(n, 1, 0, k);
	}
}
