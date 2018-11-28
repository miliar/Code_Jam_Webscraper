#define TEST

#ifdef TEST 
#define _CRT_SECURE_NO_WARNINGS
#endif


#include <iostream>
#include <string>


int main()
{
#ifdef TEST
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "wb", stdout);
#endif

	int numOfTestcases;
	std::cin >> numOfTestcases;

	for (int i = 0; i < numOfTestcases; ++i)
	{
		std::cout << "Case #" << (i + 1) << ": ";

		std::string s;
		std::cin >> s;

		int pancakeFlipperSize;
		std::cin >> pancakeFlipperSize;

		int counter = 0;
		for (int j = 0; j < s.length() - pancakeFlipperSize + 1; ++j)
		{
			if (s[j] == '-')
			{
				counter++;
				for (int k = 0; k < pancakeFlipperSize; ++k)
				{
					if (s[j + k] == '-') s[j + k] = '+';
					else s[j + k] = '-';
				}
			}
		}

		bool hasSolution = true;
		for (char c : s)
		{
			if (c == '-')
			{
				hasSolution = false;
				break;
			}
		}

		if (hasSolution)
		{
			std::cout << counter << std::endl;
		}
		else
		{
			std::cout << "IMPOSSIBLE" << std::endl;
		}
	}
}