#include <iostream>
#include <limits>
#include <utility>
#include <algorithm>
#include <queue>

// Forward declaration
std::pair<unsigned long long int, unsigned long long int> calcBathroomStalls(std::priority_queue<unsigned long long int> *curQueue, unsigned long long int numPeople);
std::pair<unsigned long long int, unsigned long long int> split(unsigned long long int i);

void bathroomstalls_problem()
{
	int numProblems = 0;
	std::cin >> numProblems;

	for (int i = 0; i < numProblems; i++) {
		unsigned long long int numStalls;
		std::cin >> numStalls;
		unsigned long long int numPeople;
		std::cin >> numPeople;

		std::priority_queue<unsigned long long int> initQueue;
		initQueue.push(numStalls);

		std::pair<unsigned long long int, unsigned long long int> solution = calcBathroomStalls(&initQueue, numPeople);

		// first - maximum, second - minimum
		std::cout << "Case #" << i + 1 << ": " << solution.first << " " << solution.second << std::endl;
	}
}

std::pair<unsigned long long int, unsigned long long int> calcBathroomStalls(std::priority_queue<unsigned long long int> *curQueue, unsigned long long int numPeople)
{
	unsigned long long int highestVal = std::numeric_limits<unsigned long long int>::min();

	// allocate container *nextList
	std::priority_queue<unsigned long long int> *nextQueue = new std::priority_queue<unsigned long long int>;

	// container to store lastPair returned
	std::pair<unsigned long long int, unsigned long long int> lastPair;

	// for numPeople (loop)
	for (unsigned long long int i = 0; i < numPeople; i++) {
		// get highestVal in curList
		highestVal = curQueue->top();
		curQueue->pop();

		// lastPair = split(highestVal)
		lastPair = split(highestVal);

		// insert in nextList
		nextQueue->push(lastPair.first);
		nextQueue->push(lastPair.second);

		// if curList->isEmpty, curList = nextList. nexList = new list
		if (curQueue->empty()) {
			curQueue = nextQueue;
			nextQueue = new std::priority_queue<unsigned long long int>;
		}

	}

	return std::pair<unsigned long long int, unsigned long long int>(std::max(lastPair.first, lastPair.second), std::min(lastPair.first, lastPair.second));
}

// splits number into left and right
std::pair<unsigned long long int, unsigned long long int> split(unsigned long long int i)
{
	if (i == 1)								// if one
		return std::pair<unsigned long long int, unsigned long long int>(0, 0);
	else if (i % 2 == 0)					// if even
		return std::pair<unsigned long long int, unsigned long long int>(i / 2 - 1, i / 2);
	else {									// if odd
		return std::pair<unsigned long long int, unsigned long long int>(i / 2, i / 2);
	}
}

int main()
{
	bathroomstalls_problem();

	std::cin.get();
	std::cin.get();

	return 0;
}