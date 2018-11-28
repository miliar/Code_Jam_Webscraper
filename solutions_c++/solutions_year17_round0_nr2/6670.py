#include <iostream>
#include <cstdint>
#include <vector>

std::vector<uint8_t> fromInt(uint64_t x)
{
	std::vector<uint8_t> result;
	while (x >= 10) 
	{
		result.push_back(x % 10);
		x /= 10; 
	}
	result.push_back(x);
	return result;
}

uint64_t fromVec(std::vector<uint8_t> x)
{
	uint64_t result = 0;
	for (auto it = x.rbegin(); it != x.rend(); it++)
	{
		result *= 10;
		result += *it;
	}
	return result;
}

void tidy(std::vector<uint8_t>& x)
{
	// Single digit numbers are always tidy
	if (x.size() < 2)
		return;

	for (uint32_t i = 0; i < x.size(); ++i)
	{
		// For each digit, we want to compare against each leading place
		for (uint32_t j = i + 1; j < x.size(); ++j)
		{
			if (x[i] < x[j])
			{
				// Sub 1 from position j
				while (j < x.size() && x[j] == 0)
				{
					++j;
				}
				if (j < x.size())
				{
					x[j]--;
				}
				else
				{
					x.pop_back();
				}

				// Replace all up to j with 9s
				for (uint32_t k = 0; k<x.size() && k < j; ++k)
				{
					x[k] = 9;
				}
				// We now know everything up to j is tidy
				i = j - 1;
			}
		}
	}
}

void tidyNumbers()
{
	uint64_t t, n;
	std::cin >> t;
	for (uint64_t i = 1; i <= t; ++i)
	{
		std::cin >> n;
		std::vector<uint8_t> digits = fromInt(n);
		tidy(digits);
		std::cout << "Case #" << i << ": " << fromVec(digits) << std::endl;
	}
}

int main()
{
	tidyNumbers();
    return 0;
}