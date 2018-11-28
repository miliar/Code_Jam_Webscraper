#include <iostream>
#include <string>
#include <unordered_set>
#include <utility>
#include <limits>
#include <algorithm>

// forward declration
int pancake_flipcount(const std::string &, int);
int calculate_flips(const std::vector<std::string> &frontier, int k, int step, std::unordered_set<std::string> &memo_table);
std::string flip(std::string string, int index, int consec);
bool check(std::string string);

void pancake_problem()
{
	int numProblems = 0;			// contains number of problems
	std::cin >> numProblems;

	std::vector<std::pair<std::string, int>> problemList;	// contains problem list
	for (int i = 0; i < numProblems; ++i) {
		std::string text;									// initial string
		int k;												// the problem's k
		std::cin >> text >> k;
		problemList.push_back(std::pair<std::string, int>(text, k));	// vector now contains problem
	}

	for (int i = 0; i < problemList.size(); i++) {
		// solve problem
		int solution = pancake_flipcount(problemList[i].first, problemList[i].second);

		// output solution
		if (solution == -1)
			std::cout << "case #" << i + 1 << ": IMPOSSIBLE\n";
		else
			std::cout << "case #" << i + 1 << ": " << solution << std::endl;
	}
}

int pancake_flipcount(const std::string &init, int k) {
	// create memo table
	std::unordered_set<std::string> visited_strings;

	// create initial frontier
	std::vector<std::string> first;
	first.push_back(init);
	visited_strings.insert(init);

	// create int minFlips to get minimum number of flips
	int minFlips = 0;

	// call BFS algorithm
	minFlips = calculate_flips(first, k, 0, visited_strings);

	// output minFlips
	return minFlips;
}

int calculate_flips(const std::vector<std::string> &frontier, int k, int step, std::unordered_set<std::string> &memo_table) {
	// check if everything is already '+'
	for (int i = 0; i < frontier.size(); i++) {
		if (check(frontier[i]))
			return step;
	}

	// container to store next frontier
	std::vector<std::string> nodesReached;

	// find all strings reachable from each frontier and add all unique strings to nodesReached
	for (int i = 0; i < frontier.size(); i++) {
		for (int j = 0; j < frontier[i].size() - (k - 1); ++j) {
			std::string flipped = flip(frontier[i], j, k);	// flip string starting from index j

			if (memo_table.insert(flipped).second) {	// if string does not exist
				nodesReached.push_back(flipped);		// add in new frontier
			}
		}
	}

	int flips = 0;
	// Explore new frontier if applicable
	if (nodesReached.size() == 0)
		return -1;
	else
		flips = calculate_flips(nodesReached, k, step + 1, memo_table);

	return flips;	// impossible
}

std::string flip(std::string string, int index, int consec) {
	for (int i = index; i < index + consec; ++i) {
		if (string[i] == '-')
			string[i] = '+';
		else
			string[i] = '-';
	}
	return string;
}

bool check(std::string string) {
	for (int i = 0; i < string.size(); i++) {
		if (string[i] != '+')
			return false;
	}

	return true;
}

int main()
{
	pancake_problem();

	std::cin.get();
	std::cin.get();

	return 0;
}