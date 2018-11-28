#include <stdio.h>
#include <iostream>

#include <vector>

#include <cassert>

size_t solve(std::vector<bool> pancakes, size_t k) {
	//printf("%u %u\n", pancakes.size(), k);
	assert(pancakes.size() >= k);

	size_t countFlips = 0;

	for (size_t i = 0; i < pancakes.size() - (k - 1); ++i) {
		if (!pancakes[i]) {
			for (size_t j = 0; j < k; ++j) {
				pancakes[i + j] = !pancakes[i + j];
			}

			countFlips++;
		}
	}

	// validate
	for (size_t i = 0; i < pancakes.size(); ++i) {
		if (!pancakes[i])
			return -1;
	}

	return countFlips;
}


int main() {
	int testCases;

	std::cin >> testCases;

	for (int i = 0; i < testCases; ++i) {
		std::vector<bool> pancake;

		char c;
		int k;

		bool done = false;
		while (!done) {
			std::cin >> c;

			switch (c) {
				case '+':
					pancake.push_back(true); break;
				case '-':
					pancake.push_back(false); break;
				default:
					std::cin.putback(c);
					done = true;
					break;
			}
		}

		std::cin >> k;

		int flips = solve(pancake, k);

		std::cout << "Case #" << (i + 1) << ": ";

		if (flips < 0) {
			std::cout << "IMPOSSIBLE";
		} else {
			std::cout << flips;
		}
		std::cout << std::endl;

	}

	return 0;
}
