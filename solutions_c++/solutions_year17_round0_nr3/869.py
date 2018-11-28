//============================================================================
// Name        : stalls.cpp
// Author      : Dick Carter
//============================================================================

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

using size_type = vector<int>::size_type;

struct Gap {
	size_type numGaps;
	size_type gapSize;
};
void addToGaps(queue<Gap> &gaps, size_type numGaps, size_type gapSize);

int main() {
	int numTests;
	cin >> numTests;
	for (int testId = 1; testId <= numTests; ++testId) {
		cout << "Case #" << testId << ": ";
		size_type numPeople, numStalls;
		cin >> numStalls >> numPeople;
		queue<Gap> gaps;
		gaps.push({1, numStalls});
		auto numPeopleLeft = numPeople;
		while (numPeopleLeft > 0) {
			auto numBestGap = gaps.front().numGaps;
			auto wholeGap = gaps.front().gapSize;
			auto maxHalfGap = wholeGap / 2;
			auto minHalfGap = wholeGap - 1 - maxHalfGap;
			if (numPeopleLeft <= numBestGap) {
				cout << maxHalfGap << " " << minHalfGap << endl;
				break;
			}
			addToGaps(gaps, numBestGap, maxHalfGap);
			addToGaps(gaps, numBestGap, minHalfGap);
			numPeopleLeft -= numBestGap;
			gaps.pop();
		}
	}
	return 0;
}

void addToGaps(queue<Gap> &gaps, size_type numGaps, size_type gapSize) {
	if (gapSize == gaps.back().gapSize)
		gaps.back().numGaps += numGaps;
	else {
		gaps.push({numGaps, gapSize});
	}
}
