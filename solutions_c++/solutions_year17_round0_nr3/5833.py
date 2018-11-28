#include <string>
#include <iostream>
#include <cmath>
#include <vector>
// #include "../debug.hpp"

std::pair<size_t, size_t> lastMinDistance;

std::pair<size_t, size_t> getOutputDistances(const std::vector<bool>& stalls) {
	size_t minDistance = -1;
	size_t maxDistance = 0;
	size_t lastPos = 0;

	while (lastPos < stalls.size()-1) {
		// std::cout << "lp: " << lastPos << std::endl;
		size_t distance = 0;

		for (int i = lastPos; i < stalls.size(); i++) {
			if (stalls[i]) {
				lastPos = i+1;
				break;
			}
			distance++;
			lastPos = i+1;
		}

		maxDistance = std::max(maxDistance, distance);
		minDistance = std::min(minDistance, distance);
	}

	return {maxDistance, minDistance};
}

std::pair<size_t, size_t> minDistance(const std::vector<bool>& stalls, const size_t pos) {
	size_t distance1 = 0;
	size_t distance2 = 0;

	for (int i = pos+1; i < stalls.size(); i++) {
		if (stalls[i]) break;
		distance1++;
	}

	for (int i = pos-1; i >= 0; i--) {
		if (stalls[i]) break;
		distance2++;
	}

	return {std::min(distance1, distance2), std::max(distance1, distance2)};
}

size_t bestPosition(const std::vector<bool>& stalls) {
	size_t bestPosition = 0;
	size_t bestMaxDistance = 0;
	size_t bestMinDistance = 0;

	for (int i = 0; i < stalls.size(); i++) {
		if (stalls[i]) continue;
		auto distance = minDistance(stalls, i);
		// TRACE(distance);
		if (distance.first > bestMinDistance) {
			bestMinDistance = distance.first;
			bestMaxDistance = distance.second;
			bestPosition = i;
		} else if (distance.first == bestMinDistance) {
			if (distance.second > bestMaxDistance) {
				bestMinDistance = distance.first;
				bestMaxDistance = distance.second;
				bestPosition = i;
			}
		}
	}

	lastMinDistance = {bestMinDistance, bestMaxDistance};

	return bestPosition;
}

int main(int argc, char const *argv[]) {
	size_t numCases;

	std::cin >> numCases;

	for (size_t t = 0; t < numCases; t++) {
		size_t n, k;
		size_t max = 0;
		size_t min = 0;

		std::cin >> n;
		std::cin >> k;

		std::vector<bool> stalls(n, false);

		while (k > 0) {
			k--;
			// for (auto a : stalls) {
			// 	TRACE(a);
			// }
			auto bestPos = bestPosition(stalls);
			// TRACE(bestPos);
			stalls[bestPos] = true;
		}

		// for (auto a : stalls) {
		// 	TRACE(a);
		// }

		// auto distances = getOutputDistances(stalls);
		
		std::cout << "Case #" << t+1 << ": ";
		std::cout << lastMinDistance.second << " " << lastMinDistance.first << std::endl;
	}

	return 0;
}
