#include <string>
#include <iostream>
#include <cmath>

#define size_t unsigned long long

size_t isTidy(size_t& num) {
	std::string numStr = std::to_string(num);
	size_t lastDigit = 0;
	for (int i = 0; i < numStr.size(); i++)	{
		int currentDigit = numStr[i] - '0';
		if (currentDigit < lastDigit) return i;
		lastDigit = currentDigit;
	}
	return -1;
}

int main(int argc, char const *argv[]) {
	size_t numCases;

	std::cin >> numCases;

	for (size_t t = 0; t < numCases; t++) {
		size_t number;

		std::cin >> number;

		size_t untidyness;

		while ((untidyness = isTidy(number)) != -1) {
			std::string numStr = std::to_string(number);
			size_t delta = std::stoll(numStr.substr(untidyness, numStr.size())) + 1;
			number = number - delta;
		}
		
		std::cout << "Case #" << t+1 << ": ";
		std::cout << std::to_string(number) << std::endl;
	}

	return 0;
}
