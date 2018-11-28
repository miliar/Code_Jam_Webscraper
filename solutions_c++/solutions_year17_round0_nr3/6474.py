#include <iostream>
#include <string>
#include <fstream>
#include <bitset>
#include <unordered_set>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

using Section = pair<uint64_t, uint64_t>;

struct Comparer
{
	bool operator()(const Section& left, const Section& right) {
		auto leftWidth = left.second - left.first;
		auto rightWidth = right.second - right.first;
		return (leftWidth < rightWidth)
			|| (leftWidth == rightWidth && left.first > right.first);
	}
};

void SolveProblemCase(ifstream& input, ofstream& output)
{
	uint64_t N;
	input >> N;
	uint64_t K;
	input >> K;

	priority_queue<Section, vector<Section>, Comparer> emptySections;
	emptySections.emplace(0, N - 1);

	for (uint64_t i = 0; i < K - 1; ++i)
	{
		auto top = emptySections.top();
		emptySections.pop();
		uint64_t iStall = floor((top.second - top.first) / 2) + top.first;

		if (iStall != top.first) {
			emptySections.emplace(top.first, iStall - 1);
		}
		if (iStall != top.second) {
			emptySections.emplace(iStall + 1, top.second);
		}
	}

	auto top = emptySections.top();
	uint64_t iStall = floor((top.second - top.first) / 2) + top.first;
	auto y = max(iStall - top.first, top.second - iStall);
	auto z = min(iStall - top.first, top.second - iStall);

	output << y << " " << z;
}

int main() {
	ifstream inFile("C:\\Users\\drobson\\Downloads\\C-small-1-attempt1.in");

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