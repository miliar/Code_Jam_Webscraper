#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include <map>

using namespace std;

void flipSubSeq(std::vector<bool>& seq, int firstIndex, int flipperSize)
{
	for (int i = firstIndex; i < firstIndex + flipperSize; ++i)
	{
		seq[i].flip();
	}
}

std::vector<bool> transform(const std::string& sequence)
{
	std::vector<bool> seq;
	seq.reserve(sequence.size());

	for (const char c : sequence)
	{
		seq.push_back(c == '+');
	}

	return seq;
}

int solvePancakeIssue(const std::string& sequence, int flipperSize)
{
	std::vector<bool> seq = transform(sequence);
	auto flipFunc = [flipperSize, &seq](int firstIndex)
	{
		flipSubSeq(seq, firstIndex, flipperSize);
	};

	auto finished = [&seq]()
	{
		return std::all_of(seq.begin(), seq.end(), [](bool b) { return b; });
	};

	int res = 0;

	if (finished())
	{
		return 0;
	}

	int max = (int)(seq.size() - (flipperSize - 1));
	for (int i = 0; i < max; ++i)
	{
		if (!seq[i])
		{
			flipFunc(i);
			++res;

			if (finished())
			{
				return res;
			}
		}		
	}

	return -1;
}

int main()
{
	ifstream inputFile("A-large.in");
	ofstream outputFile("output_2017.txt");

	int testNumber = 0;

	inputFile >> testNumber;

	for (int i = 1; i <= testNumber; ++i)
	{
		outputFile << "Case #" << i << ": ";
		std::string pancakeSequence;
		int flipperSize = 0;

		inputFile >> pancakeSequence;
		inputFile >> flipperSize;

		int result = solvePancakeIssue(pancakeSequence, flipperSize);
		std::string res = (result == -1 ? "IMPOSSIBLE" : std::to_string(result));

		outputFile << res << endl;
	}

	return 0;
}
