#include <iostream>
#include <bitset>
#include <string>

int OversizedPancakeFlipper(unsigned int &minFlips, std::bitset<1000> &pancakes) {
	unsigned int numFixes=0;
	if (pancakes.all()) {
		return 0;
	}
	else {
		for (unsigned int cnt = 0; cnt < 1000; ++cnt) {
			if (pancakes[cnt] == 0) {
				if (cnt + minFlips >= 1000) {
					return -1;
				}
				++numFixes;
				for (unsigned int i = 0; i < minFlips; ++i) {
					pancakes[cnt + i].flip();
				}
			}
		}
		return numFixes;
	}
}

void mapInput(std::string &input, std::bitset<1000> &pancakes) {
	unsigned int length = input.length();
	for (unsigned int cnt = 0; cnt < length; ++cnt) {
		switch (input[cnt]) {
		case '+':
			pancakes[cnt] = 1;
			break;
		case '-':
			pancakes[cnt] = 0;
			break;
		default:
			throw 1;
		}
	}
	//Set the remaining pancakes to their correct face.
	for (unsigned int cnt = length; cnt < 1000; ++cnt) {
		pancakes[cnt] = 1;
	}
}

int main(int argc, char* argv[]) {
	unsigned int numTestCases;
	std::string input;
	unsigned int minFlips;
	std::bitset<1000> pancakes;

	std::cin >> numTestCases;

	for (unsigned int testCase = 1; testCase <= numTestCases; ++testCase) {
		std::cin >> input;
		mapInput(input, pancakes);

		std::cin >> minFlips;

		std::cout << "Case #" << testCase << ": ";
		int moves = OversizedPancakeFlipper(minFlips, pancakes);
		if (moves >= 0) {
			std::cout << moves << std::endl;
		}
		else {
			std::cout << "IMPOSSIBLE" << std::endl;
		}
	}

	return 0;
}