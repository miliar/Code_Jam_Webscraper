#include <iostream>
#include <string>

std::string pancakes()
{
	std::string pancakes;
	std::cin >> pancakes;
	unsigned k;
	std::cin >> k;
	unsigned flips_made = 0;
	for (auto it = pancakes.begin(); it < pancakes.end() - k + 1; ++it)
	{
		if (*it == '-')
		{
			for (auto flip_it = it; flip_it <= it + k - 1; ++flip_it)
			{
				if (*flip_it == '-') *flip_it = '+';
				else *flip_it = '-';				
			}
			flips_made++;
		}
	}

	for (auto it = pancakes.end() - k; it < pancakes.end(); ++it)
	{
		if (*it == '-') return "IMPOSSIBLE";
	}
	return std::to_string(flips_made);
}

int main()
{
	int testCases = 0;
	std::cin >> testCases;
	for (int i = 0; i < testCases; i++)
	{		
		std::cout << "Case #" << i + 1 << ": ";
		std::cout << pancakes();
		std::cout << std::endl;
	}
}