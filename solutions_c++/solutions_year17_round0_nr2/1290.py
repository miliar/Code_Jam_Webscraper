#include <iostream>
#include <vector>
#include <algorithm>

typedef unsigned long long number;

std::vector<int> numberToArray(number N) {
	std::vector<int> ret;
	while (N > 0) {
		ret.push_back(N % 10);
		N /= 10;
	}
	reverse(ret.begin(), ret.end());
	return ret;
}

number arrayToNumber(const std::vector<int>& digits) {
	number N = 0;
	for (const auto& d : digits) {
		N += d;
		N *= 10;
	}
	return N/10;
}

int main() {

	int t;
	std::cin >> t;

	for (auto c = 1; c <= t; c++) {
		number n;
		std::cin >> n;

		auto digits = numberToArray(n);

		bool setNines = false;

		int reverseIndex = -1;

		for (auto i = 0; i < digits.size() - 1; i++) { 
			if (setNines) {
				digits[i + 1] = 9;
			}
			else {
				if (digits[i] > digits[i + 1]) {
					digits[i]--;
					reverseIndex = i;
					setNines = true;
					digits[i + 1] = 9;
				}
			}
		}

		for (auto i = reverseIndex; i > 0; i--) {
			if (digits[i - 1] > digits[i]) {
				digits[i] = 9;
				digits[i - 1]--;
			}
			else {
				break;
			}
		}

		auto N = arrayToNumber(digits);
		std::cout << "Case #" << c << ": " << N << "\n";

	}

	getchar();

	return 0;
}