#include <iostream>
#include <string>
#include <fstream>
#include <bitset>
#include <unordered_set>
#include <vector>
#include <queue>

using namespace std;

inline bool AllTrue(const vector<bool>& bits)
{
	return find(bits.cbegin(), bits.cend(), false) == bits.cend();
}

struct FlipState
{
	FlipState(vector<bool>&& state, uint64_t numFlips)
	{
		State = state;
		NumFlips = numFlips;
	}
	vector<bool> State;
	uint64_t NumFlips;
};

void SolveProblemCase(ifstream& input, ofstream& output)
{
	unordered_set<vector<bool>> alreadySeen;
	string pancakes;
	input >> pancakes;
	vector<bool> orig(pancakes.size());
	for (auto i = 0; i < pancakes.size(); ++i) {
		orig[i] = pancakes[i] == '+';
	}

	int flipperSize;
	input >> flipperSize;

	int numFlippablePositions = 1 + orig.size() - flipperSize;
	queue<FlipState> searchQueue;
	alreadySeen.emplace(orig);
	searchQueue.push(FlipState(std::move(orig), 0));

	while (!searchQueue.empty())
	{
		auto cur = searchQueue.front();
		searchQueue.pop();
		if (AllTrue(cur.State)) {
			output << cur.NumFlips;
			return;
		}

		for (int flipperPos = 0; flipperPos < numFlippablePositions; ++flipperPos)
		{
			auto nextState = cur.State;
			for (int pancake = flipperPos; pancake < flipperPos + flipperSize; ++pancake) {
				nextState[pancake].flip();
			}

			if (alreadySeen.find(nextState) == alreadySeen.end()) {
				alreadySeen.emplace(nextState);
				searchQueue.push(FlipState(std::move(nextState), cur.NumFlips + 1));
			}
		}
	}

	output << "IMPOSSIBLE";
}

int main() {
	ifstream inFile("C:\\Users\\drobson\\Downloads\\A-small-attempt0.in");

	ofstream outFile("C:\\Users\\drobson\\Documents\\CodeJam\\output.txt");

	size_t numTestCases;
	inFile >> numTestCases;

	for (auto i = 1; i <= numTestCases; ++i)
	{
		outFile << "Case #" << i << ": ";
		SolveProblemCase(inFile, outFile);
		outFile << endl;
	}

	outFile.close();

	return 0;
}