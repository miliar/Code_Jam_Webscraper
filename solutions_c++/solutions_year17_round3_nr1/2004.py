#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#define _USE_MATH_DEFINES
#include <cmath>


typedef std::pair<__int64 /*r*/, __int64 /*h*/> PC;


__int64 GetSurfaceArea(std::vector<PC> pcs) //Get total surface area of these given pancakes stacked on top of each other, with the first given one being the bottom one.
{
	__int64 runningTotal = pcs.front().first * pcs.front().first;
	for each(PC pc in pcs)
	{
		runningTotal += 2 * pc.first * pc.second;
	}
	return runningTotal;
}


__int64 GetBestCombination(const std::vector<PC>& pcs, std::vector<PC> currentCombination, __int64 offset, __int64 k) {
	if (k == 0)
	{
		std::sort(currentCombination.begin(), currentCombination.end(), [](const PC& a, const PC& b) { return a.first > b.first; });
		return GetSurfaceArea(currentCombination);
	}
	__int64 maxCombVal = -INT_MAX;
	for (__int64 i = offset; i <= pcs.size() - k; ++i)
	{
		currentCombination.push_back(pcs[i]);
		__int64 combVal = GetBestCombination(pcs, currentCombination, i + 1, k - 1);
		maxCombVal = std::max(combVal, maxCombVal);
		currentCombination.pop_back();
	}
	return maxCombVal;
}


int main()
{
	std::ifstream in("input.in");
	std::ofstream out("output.txt");
	if (!in)
		return -1;

	out.precision(15);
	unsigned __int64 numCases = 0;
	in >> numCases;
	for (unsigned __int64 i = 1; i <= numCases; i++)
	{
		out << "Case #" << i << ": ";

		__int64 N, K;
		in >> N >> K;

		std::vector<PC> PCs;

		for (__int64 i = 0; i < N; i++)
		{
			PC p;
			in >> p.first >> p.second;
			PCs.push_back(p);
		}

		__int64 sa = GetBestCombination(PCs, std::vector<PC>(), 0, K);

		out << static_cast<double>(sa) * 3.14159265358979323846 << std::endl;
	}

	return 0;
}


