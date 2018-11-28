#define TEST

#ifdef TEST 
#define _CRT_SECURE_NO_WARNINGS
#endif


#include <iostream>
#include <vector>
#include <algorithm>



int main()
{
#ifdef TEST
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "wb", stdout);
#endif

	int numOfTestcases;
	std::cin >> numOfTestcases;

	for (int t = 0; t < numOfTestcases; ++t)
	{
		std::cout << "Case #" << (t + 1) << ": ";

		int numOfGroups, numOfPieces;
		std::cin >> numOfGroups >> numOfPieces;

		std::vector<int> groups;

		for (int k = 0; k < numOfGroups; ++k)
		{
			int s;
			std::cin >> s;
			groups.push_back(s);
		}

		// 2 pieces
		if (numOfPieces == 2)
		{
			int numOfEvenGroups = 0;
			int numOfOddGroups = 0;

			for (auto i : groups)
			{
				if (i % 2 == 0)
				{
					numOfEvenGroups++;
				}
				else
				{
					numOfOddGroups++;
				}
			}

			// all even orders can be filled
			// (odd+1)/2 odd orders can be filled
			std::cout << (numOfEvenGroups + (numOfOddGroups + 1) / 2) << std::endl;
		}
		// 3 pieces
		else if (numOfPieces == 3)
		{
			int numOf3k_0 = 0;
			int numOf3k_1 = 0;
			int numOf3k_2 = 0;

			for (auto i : groups)
			{
				if (i % 3 == 0)
				{
					numOf3k_0++;
				}
				else if (i % 3 == 1)
				{
					numOf3k_1++;
				}
				else
				{
					numOf3k_2++;
				}
			}

			// 3k_0 orders can be filled
			int total = numOf3k_0;

			// 3k_1 and 3k_2 common
			int lower = std::min(numOf3k_1, numOf3k_2);
			total += lower;

			numOf3k_1 -= lower;
			numOf3k_2 -= lower;

			total += (numOf3k_1 + 2) / 3;
			total += (numOf3k_2 + 2) / 3;

			std::cout << total << std::endl;
		}
		else if (numOfPieces == 4)
		{
			int numOf4k_0 = 0;
			int numOf4k_1 = 0;
			int numOf4k_2 = 0;
			int numOf4k_3 = 0;

			for (auto i : groups)
			{
				if (i % 4 == 0)
				{
					numOf4k_0++;
				}
				else if (i % 4 == 1)
				{
					numOf4k_1++;
				}
				else if (i % 4 == 2)
				{
					numOf4k_2++;
				}
				else
				{
					numOf4k_3++;
				}
			}

			// 4k_0 orders can be filled
			int total = numOf4k_0;

			// every 2nd 4k_2 order can be filled
			total += numOf4k_2 / 2;

			// 0 or 1 numof4k_1 remaining
			numOf4k_2 = numOf4k_2 % 2;
			
			// 4k_1 and 4k_3 is the same as for 3k_1 and 3k_2
			int lower = std::min(numOf4k_1, numOf4k_3);
			total += lower;

			numOf4k_1 -= lower;
			numOf4k_3 -= lower;

			if (numOf4k_2 == 1)
			{
				if (numOf4k_1 >= 2)
				{
					total++;
					numOf4k_1 -= 2;
				}
				else if (numOf4k_3 >= 2)
				{
					total++;
					numOf4k_3 -= 2;
				}
				else if (numOf4k_1 == 0 && numOf4k_3 == 0)
				{
					total++;
				}
			}
			
			total += (numOf4k_1 + 3) / 4;
			total += (numOf4k_3 + 3) / 4;
			
			std::cout << total << std::endl;
		}
	}
}