#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

auto parse(size_t N) {
	auto input = std::to_string(N);
	auto length = input.size();
	bool restart = true;
	while (restart) {
		restart = false;
		for (size_t i = 1; i < length; i++) {
			if (input[i - 1] > input[i]) {
				for (size_t j = i; j < length; j++) {
					input[j] = '9';
				}
				input[i - 1]--;
				restart = true;
				break;
			}
		}
	}

	size_t i = 0;
	while (i < length) {
		if (input[i] != '0') {
			return input.substr(i);
		}
		i++;
	}
}

int main(int, char**) {
	size_t T, i = 0;
	size_t N;

	std::cin >> T;
	for (size_t i = 0; i < T; i++) {
		std::cin >> N;
		auto answer = parse(N);
		std::cout << "Case #" << (i+1) << ": " << answer << std::endl;
	}
}
