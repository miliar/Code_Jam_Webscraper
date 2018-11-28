#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

void calc(int nStalls, int kPeople, int& maxLsRs, int& minLsRs)
{
	std::vector<int> ranges;
	ranges.push_back(nStalls);

	for (int i = 0; i < kPeople; ++i)
	{
		std::stable_sort(ranges.begin(), ranges.end());

		int r = ranges.back();
		ranges.pop_back();

		int slot = 0;
		if (r % 2 == 0)
		{
			slot = (r / 2) - 1;
		}
		else
		{
			slot = r / 2;
		}

		int left = slot;
		int right= r - (slot + 1);
		maxLsRs = std::max(left, right);
		minLsRs = std::min(left, right);

		if (left > 0)
			ranges.push_back(left);
		if (right > 0)
			ranges.push_back(right);
	}
}

void main()
{
	std::ifstream in("input.txt");
	std::ofstream out("out.txt");

	std::string line;
	std::getline(in, line);

	int numTestCases = 0;
	std::stringstream ss;
	ss << line;
	ss >> numTestCases;

	for (int i = 0; i < numTestCases; ++i)
	{
		int testCaseNum = i + 1;

		std::getline(in, line);
		ss.clear();

		int numStalls;
		int numPeople;
		ss << line;
		ss >> numStalls >> numPeople;

		//std::cout << numStalls << " " << numPeople << "\n";std::string line;

		int maxLsRs;
		int minLsRs;
		calc(numStalls, numPeople, maxLsRs, minLsRs);

		out << "Case #" << testCaseNum << ": " << maxLsRs << " " << minLsRs << "\n";


	}

	out.close();

	std::cout << "Done!";

	getchar();
}