#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

void main()
{
	int cases;
	std::cin >> cases;
	
	for (int i = 0; i < cases; ++i)
	{
		std::string str;
		int size;
		std::cin >> str;
		std::cin >> size;
		std::vector<int> flipsum(str.size() + 1, 0);

		int j = 0;
		for (j; j + size <= str.size(); ++j)
		{
			if ((str[j] == '+' && ((flipsum[j] - flipsum[std::max(0, j - size + 1)]) % 2 == 0)) ||
				(str[j] == '-' && ((flipsum[j] - flipsum[std::max(0, j - size + 1)]) % 2 == 1)))
			{
				flipsum[j + 1] = flipsum[j];
				continue;
			}
			else
			{
				flipsum[j + 1] = flipsum[j] + 1;
			}
		}

		int result = 1;

		while (j < str.size())
		{
			if ((str[j] == '+' && (flipsum[j] - flipsum[std::max(0, j - size + 1)]) % 2 == 1) ||
				(str[j] == '-' && (flipsum[j] - flipsum[std::max(0, j - size + 1)]) % 2 == 0))
			{
				result = 0;
				break;
			}
			flipsum[j + 1] = flipsum[j];
			++j;
		}

		if (!result)
		{
			std::cout << "Case #" << i + 1 << ": IMPOSSIBLE" << std::endl;
		}
		else {
			std::cout << "Case #" << i + 1 << ": " << flipsum[j] << std::endl;
		}
	}
}