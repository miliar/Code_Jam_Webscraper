#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> digits;

void solve() {
	/*for (int i = 0; i < digits.size(); i++)cout << digits[i];
	cout << endl;*/

	for (int i = 0, ant = -1; i < digits.size(); ant = digits[i], i++) {
		if (ant > digits[i]) {
			//cout << "found disparity on digit (" << i << ") --> " << ant << ", " << digits[i] << endl;
			for (int j = i; j < digits.size(); j++) {
				digits[j] = 9;
			}
			if (i)
				digits[i-1]--;

			solve();
		}//111111111111111110
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		long long inp;
		cin >> inp;

		digits.clear();

		while (inp > 0) {
			digits.push_back(inp % 10);
			inp /= 10;
		}

		reverse(digits.begin(), digits.end());

		solve();

		printf("Case #%d: ", t);
		for (int i = 0; i < digits.size(); i++) {
			if (!i and !digits[i])
				continue;
			cout << digits[i];
		}
		cout << endl;
	}
	return 0;
}