#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#define ECHO(x) std::cout << x << std::endl;
#define TRACE(x) std::cout << (#x) << " = " << (x) << std::endl;

void debug(const std::string& state, const std::unordered_map<size_t, std::pair<size_t, size_t>>& map) {
	for (auto& pair : map) {
		ECHO(pair.first << ": {" << pair.second.first << "," << pair.second.second << "}");
	}
	ECHO(state);
}

auto parse(size_t N, size_t K) {
	std::string state = "O" + std::string(N, '.') + "O";
	auto length = N + 2;
	std::unordered_map<size_t, std::pair<size_t, size_t>> map;
	size_t lastChosenStall = 0;
	size_t counter = 0;
	while (counter < K) {
		map.clear();
		for (size_t i = 1; i < length - 1; i++) {
			if (state[i] == '.') {
				size_t left = 0;
				size_t right = 0;
				for (long j = i - 1; j >= 0; j--) {
					if (state[j] == 'O') {
						left = i - j - 1;
						break;
					}
				}

				for (long j = i + 1; j < length; j++) {
					if (state[j] == 'O') {
						right = j - i - 1;
						break;
					}
				}

				map[i] = {std::min(left, right), std::max(left, right)};
			}
		}

		size_t maximal_min = 0;
		std::vector<std::pair<size_t, size_t>> associatedValues;
		for (auto& pair : map) {
			auto actualPair = pair.second;
			if (actualPair.first > maximal_min) {
				maximal_min = actualPair.first;
				associatedValues.clear();
			}

			if (actualPair.first == maximal_min) {
				associatedValues.push_back({actualPair.second, pair.first});
			}
		}

		size_t maximal_max = 0;
		std::vector<size_t> choices;
		for (auto& pair : associatedValues) {
			if (pair.first > maximal_max) {
				maximal_max = pair.first;
				choices.clear();
			}

			if (pair.first == maximal_max) {
				choices.push_back(pair.second);
			}
		}

		std::sort(choices.begin(), choices.end());
		state[choices[0]] = 'O';
		lastChosenStall = choices[0];

		counter++;
	}

	auto lastPair = map[lastChosenStall];
	auto result = std::to_string(lastPair.second);
	result += " ";
	result += std::to_string(lastPair.first);
	return result;
}

int main(int, char**) {
	size_t T, i = 0;
	size_t N, K;

	std::cin >> T;
	for (size_t i = 0; i < T; i++) {
		std::cin >> N >> K;
		auto answer = parse(N, K);
		std::cout << "Case #" << (i+1) << ": " << answer << std::endl;
	}
}
