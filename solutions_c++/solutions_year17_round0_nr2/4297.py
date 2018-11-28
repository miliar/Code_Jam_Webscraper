#include <iostream>
#include <string>

using namespace std;

void solve() {
	string num;
	cin >> num;
	int digits[10] = { 0 };
	digits[num[0] - '0']++;
	bool done = false;
	for (int i = 1; i < num.length() && !done; i++) {
		if (num[i] >= num[i - 1]) {
			digits[num[i] - '0']++;
		}
		else {
			for (int d = 9; d > 0; d--) {
				if (digits[d] != 0) {
					digits[d - 1]++;
					digits[d] = 0;
					//néha több a 9-es
					digits[9] = num.length() - digits[0] - digits[1] - digits[2] - digits[3] - digits[4] - digits[5] - digits[6] - digits[7] - digits[8] - digits[9];
					done = true;
					break;
				}
			}
		}
	}
	for (int d = 1; d < 10; d++) {
		for (int i = 0; i < digits[d]; i++) {
			cout << d;
		}
	}
}


int  main() {
	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
