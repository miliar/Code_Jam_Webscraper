#include <iostream>
#include <fstream>
#include <string>

std::string reverse(std::string s) {
	std::string output;
	for (auto it = s.rbegin(); it != s.rend(); ++it)
		output.push_back(*it);

	return output;
}

std::string findLastTidy(std::string s) {
	std::string output;
	int digits = 0;

	short digit = 10;
	for (auto it = s.rbegin(); it != s.rend(); ++it) {
		short oldDigit = digit;
		digit = *it - '0';

		if (digit <= oldDigit) {
			output.push_back(*it);
		}
		else {
			output = std::string();

			for (int j = 0; j < digits; ++j) {
				output.push_back('9');
			}

			digit -= 1;

			output.push_back(digit + '0');
		}

		digits++;
	}

	int zeros = 0;
	for (auto it = output.rbegin(); it != output.rend(); ++it) {
		if (*it == '0') {
			zeros++;
		}
		else {
			break;
		}
	}

	for (int i = 0; i < zeros; ++i)
		output.pop_back();

	return reverse(output);
}

int main(int argc, char ** args) {
	int numberOfTests;
	std::cin >> numberOfTests;

	for (int i = 0; i < numberOfTests; ++i) {
		std::string s;
		std::cin >> s;

		auto lastTidy = findLastTidy(s);

		std::cout << "Case #" << i + 1 << ": " << lastTidy << std::endl;
	}

}