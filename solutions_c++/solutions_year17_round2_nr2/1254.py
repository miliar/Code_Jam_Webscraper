#include <iostream>
#include <cstdint>
#include <string>
#include <limits>
#include <algorithm>

void legalNexts(int c, bool outLegal[6])
{
	for (int i = 0; i < 6; ++i) { outLegal[i] = true; }
	outLegal[c] = false;
	outLegal[(c + 1) % 6] = false;
	if (c == 0)
		outLegal[5] = false;
	else
		outLegal[c - 1] = false;
}

void pickNext(uint64_t counts[6], bool legals[6], int firstPlaced, int& outColour, std::string& resString)
{
	int index;
	uint64_t maxCount = 0;

	for (int i = 0; i < 6; ++i)
	{
		if (legals[i] && ((counts[i] > maxCount) || (counts[i] == maxCount && i == firstPlaced)))
		{
			index = i;
			maxCount = counts[i];
		}
	}

	counts[index]--;
	outColour = index;

	switch (index)
	{
	case 0:
		resString += "R";
		break;
	case 1:
		resString += "O";
		break;
	case 2:
		resString += "Y";
		break;
	case 3:
		resString += "G";
		break;
	case 4:
		resString += "B";
		break;
	case 5:
		resString += "V";
		break;
	}
}

std::string solve(uint64_t N, uint64_t R, uint64_t O, uint64_t Y, uint64_t G, uint64_t B, uint64_t V)
{
	std::string result;
	result.reserve(1000);
	uint64_t Counts[6] = { R, O, Y, G, B, V };
	bool legalChoice[6] = { true, true, true, true, true, true };
	int firstPlaced = -1;
	int lastPlaced;

	for (int i = 0; i < N; ++i)
	{
		{
			bool anyLegal = false;
			for (int j = 0; j < 6; ++j) { anyLegal |= legalChoice[j] && Counts[j] > 0; }
			if (!anyLegal)
				return "IMPOSSIBLE";
		}

		// Pick horse
		pickNext(Counts, legalChoice, firstPlaced, lastPlaced, result);
		legalNexts(lastPlaced, legalChoice);

		if (i == 0)
			firstPlaced = lastPlaced;

		if (i == N - 2)
		{
			bool firstLegals[6];
			legalNexts(firstPlaced, firstLegals);
			for (int j = 0; j < 6; ++j) { legalChoice[j] = legalChoice[j] && firstLegals[j]; }
		}
	}
	
	return result;
}

int main()
{
	uint64_t t, N, R, O, Y, G, B, V;
	std::cin >> t;
	for (uint64_t i = 1; i <= t; ++i)
	{
		std::cin >> N >> R >> O >> Y >> G >> B >> V;
		std::cout << "Case #" << i << ": " << solve(N,R,O,Y,G,B,V) << std::endl;
	}
    return 0;
}