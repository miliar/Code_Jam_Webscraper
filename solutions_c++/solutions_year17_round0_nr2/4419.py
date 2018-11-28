#include <iostream>
#include <vector>
#include <string>
#include <istream>


int main() {
	int n;
	std::cin >> n;
	std::vector<char> nums({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'});
	for (int i = 0; i < n; ++i) {
		std::string answer = "";
		long long number;
		std::cin >> number;
		int last_digit = 10;

		int end_nine = 0;
		while(number > 0) {
			int digit = number % 10;
			number /= 10;
			if (last_digit < digit) {
				end_nine = answer.length();
				answer += nums[digit-1];
				last_digit = digit-1;
			} else {
				answer += nums[digit];
				last_digit = digit;
			}
		}

		for (int j = 0; j < end_nine; ++j) {
			answer[j] = '9';
		}

		int begin = answer[answer.length() - 1] == '0' ? answer.length() - 2 : answer.length() - 1;

		std::cout << "Case #" << i+1 << ": ";
		for (int j = begin; j >=0; --j) {
			std::cout << answer[j];
		}
		std::cout << '\n';
	}

	return 0;
}