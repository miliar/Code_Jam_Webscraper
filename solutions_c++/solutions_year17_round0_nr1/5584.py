#include <iostream>
#include <fstream>
#include <string>

void flip(char & c) {
	if (c == '+')
		c = '-';
	else if (c == '-')
		c = '+';
}

int getNumberOfFlips(std::string layout, int fSize) {
	int flips = 0;
	
	int index = 0;
	int size = layout.size();

	while (true) {
		if (index > (size - fSize))
			break;

		if (layout[index] == '-') {
			flips++;
			for (int j = 0; j < fSize; ++j)
				flip(layout[index + j]);
		}

		index++;
	}
	
	for (auto it = layout.begin(); it != layout.end(); ++it) {
		if (*it == '-')
			return -1;
	}

	return flips;
}

int main(int argc, char ** args) {
	std::istream & input = std::cin;

	int numberOfTests;
	input >> numberOfTests;

	for (int i = 0; i < numberOfTests; ++i) {
		std::string layout;
		int fSize;

		input >> layout;
		input >> fSize;

		int flips = getNumberOfFlips(layout, fSize);
		
		std::cout << "Case #" << i + 1 << ": ";
		if (flips == -1) 
			std::cout << "IMPOSSIBLE" << std::endl;
		else 
			std::cout << flips << std::endl;
	}
}