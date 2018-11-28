#include <string>
#include <iostream>

void flip(int location, int flipperSize, std::string& str) {
	for (int i = location; i < location + flipperSize; i++) {
		str[i] == '-' ? str[i] = '+' : str[i] = '-';
	}
}

int main(int argc, char const *argv[]) {
	int numCases;

	std::cin >> numCases;

	for (int t = 0; t < numCases; t++) {
		std::string response = "IMPOSSIBLE";

		std::string pancakes;
		int flipperSize;

		std::cin >> pancakes;
		std::cin >> flipperSize;

		// std::cout << pancakes << std::endl;

		if (pancakes.find_first_of("-") == std::string::npos) {
			response = "0";
		} else {
			int counter = 0;
			for (int i = 0; i <= pancakes.size() - flipperSize; i++) {
				if (pancakes[i] == '-') {
					flip(i, flipperSize, pancakes);
					// std::cout << pancakes << std::endl;
					counter++;
				}
			}

			if (pancakes.find_first_of("-") == std::string::npos) {
				response = std::to_string(counter);
			}
		}

		std::cout << "Case #" << t+1 << ": ";
		std::cout << response << std::endl;
	}

	return 0;
}
