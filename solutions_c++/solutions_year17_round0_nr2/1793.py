#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int q = 0; q < t; q++) {
		long long n;
		cin >> n;
		vector <int> digits;
		while (n) {
			digits.push_back(n % 10);
			n /= 10;
		}
		for (int i = 0; i < (int)digits.size() - 1; i++) {
			if (digits[i] < digits[i + 1]) {
				digits[i + 1]--;
				for (int j = 0; j <= i; j++)
					digits[j] = 9;
			}
		}
		cout << "Case #" << q + 1 << ": ";
		while (digits.back() == 0)
			digits.pop_back();
		while (!digits.empty()) {
			cout << digits.back();
			digits.pop_back();
		}
		cout << '\n';
	}

	return 0;
}