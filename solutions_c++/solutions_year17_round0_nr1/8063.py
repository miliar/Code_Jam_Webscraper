#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

namespace pancake_flipper
{
	int solve(std::vector< bool > pancakes, int flipper_size)
	{
		int result = 0;
		std::size_t current = 0;
		for (; current + flipper_size <= pancakes.size(); ++current)
		{
			if (pancakes[current])
				continue;

			result += 1;
			for (int i = 0; i < flipper_size; ++i)
			{
				pancakes[current + i] = !pancakes[current + i];
			}
		}
		const bool success = std::find(pancakes.begin() + current, pancakes.end(), false) == pancakes.end();
		return success ? result : -1;
	}

	std::vector< bool > fromString(std::string inp)
	{
		std::vector< bool > result;
		std::transform(inp.begin(), inp.end(), std::back_inserter(result), [](char ch) { return ch == '+';  });
		return result;
	}
}
int main()
{
	int cases;
	std::cin >> cases;
	for (int i = 0; i < cases; ++i)
	{
		std::string cakes;
		int flipper_size = 0;
		std::cin >> cakes >> flipper_size;
		int result = pancake_flipper::solve(pancake_flipper::fromString(std::move(cakes)), flipper_size);
		std::cout << "Case #" << i + 1 << ": " << ( result == -1 ? "IMPOSSIBLE" : std::to_string( result ) ) << std::endl;
	}
}