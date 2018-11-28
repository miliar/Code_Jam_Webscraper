// problemB.cpp : Defines the entry point for the console application.
//

#include <iostream> 
#include <vector>
#include <string>

using namespace std;

void main() {
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		uint64_t n;
		cin >> n;
		vector<int> digits;
		while( n > 0 ) {
			digits.insert(digits.begin(), n % 10 );
			n /= 10;
		}
		int lastDigit = 0;
		for (size_t pos = 0; pos < digits.size();) {
			if (digits[pos] < lastDigit) {
				digits[pos - 1]--;
				for (size_t j = pos; j < digits.size(); j++) {
					digits[j] = 9;
				}
				pos = 0;
				lastDigit = 0;
				continue;
			}
			lastDigit = digits[pos];
			pos++;
		}
		cout << "Case #" << i << ": ";
		for (size_t pos = 0; pos < digits.size(); pos++) {
			if (digits[pos] > 0) {
				cout << digits[pos];
			}
		}
		cout << endl;
	}
}