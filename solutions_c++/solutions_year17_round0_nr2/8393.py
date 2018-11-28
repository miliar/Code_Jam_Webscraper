#include <iostream>
#include <stdint.h>

uint64_t get_largest_divisor(uint64_t num) {
	     if (num >= 1000000000000000000) { return 1000000000000000000; }
	else if (num >= 100000000000000000) { return 100000000000000000; }
	else if (num >= 10000000000000000) { return 10000000000000000; }
	else if (num >= 1000000000000000) { return 1000000000000000; }
	else if (num >= 100000000000000) { return 100000000000000; }
	else if (num >= 10000000000000) { return 10000000000000; }
	else if (num >= 1000000000000) { return 1000000000000; }
	else if (num >= 100000000000) { return 100000000000; }
	else if (num >= 10000000000) { return 10000000000; }
	else if (num >= 1000000000) { return 1000000000; }
	else if (num >= 100000000) { return 100000000; }
	else if (num >= 10000000) { return 10000000; }
	else if (num >= 1000000) { return 1000000; }
	else if (num >= 100000) { return 100000; }
	else if (num >= 10000) { return 10000; }
	else if (num >= 1000) { return 1000; }
	else if (num >= 100) { return 100; }
	else if (num >= 10) { return 10; }
	else { return 1; }
}

uint64_t tidyify(uint64_t num) {
	uint64_t original = num;

	uint64_t largest_divisor = get_largest_divisor(num);

	if (largest_divisor == 1) {
		return num;
	}

	int previous_digit = num / largest_divisor;
	uint64_t current_num = (num / largest_divisor) * largest_divisor;

	for (uint64_t divisor = (largest_divisor / 10); divisor >= 1; divisor /= 10) {
		int this_digit = (num / divisor) % 10;

		if (this_digit < previous_digit) {
			current_num -= divisor * 10;

			for (uint64_t i = 1; i <= divisor; i *= 10) {
				current_num += 9 * i;
			}

			goto exitloops;
		} else {
			current_num += this_digit * divisor;
		}

		previous_digit = this_digit;
	}

	exitloops: ;

	if (current_num == original) {
		return current_num;
	} else {
		return tidyify(current_num);
	}
}

int main() {
	int num_nums;
	std::cin >> num_nums;

	uint64_t num;

	for (int case_num = 0; case_num < num_nums; case_num++) {
		std::cin >> num;

		uint64_t tidied = tidyify(num);

		std::cout << "Case #" << (case_num + 1) << ": " << tidied << std::endl;
	}

	return 0;
}
