#include <bits/stdc++.h>
using namespace std;

long long solve();

int main() {
	int noCases;
	cin >> noCases;

	for (int i = 1; i <= noCases; ++i) {
		cout << "Case #" << i << ": " << solve() << "\n";
	}

	return 0;
}

bool isTidy (long long n) {
	if (n == 0)
		return true;

	int digit = 9;
	while (n > 0) {
		int d = n % 10;
		n /= 10;
		if (d <= digit) {
			digit = d;
		} else {
			return false;
		}
	}
	return true;
}

long long solve() {
	long long n;
	cin >> n;
	while(!isTidy(n)) {
		--n;
	}
	return n;
}