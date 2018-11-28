#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

class B {
public:
	long tidy(long N) {
		vector<int> digits;
		for (long num = N; num != 0; num /= 10) {
			digits.push_back(num % 10);
		}
		reverse(digits.begin(), digits.end());
		int i;
		bool flag = 0;
		for (i = 0; i < digits.size() - 1; i++) {
			if (digits[i + 1] < digits[i]) {
				flag = 1;
				break;
			}
		}
		if (flag) {
			while ((i > 0) && (--digits[i] < digits[i - 1])) {
				i--;
			}
			if (i == 0) digits[i]--;
			for (i++; i < digits.size(); i++) {
				digits[i] = 9;
			}
		}
		long res = 0;
		for (i = 0; i < digits.size(); i++) {
			res = res * 10 + digits[i];
		}
		return res;
	}
};

int main() {
	int t;
	long N;
	B B1;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> N;
		cout << "Case #" << i << ": " << B1.tidy(N) << endl;
	}
}
