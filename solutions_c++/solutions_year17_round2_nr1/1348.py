#include <iostream>
#include <cstdint>
#include <string>
#include <limits>
#include <algorithm>


double calcSpeed(uint64_t D, uint64_t K, uint64_t S)
{
	return (static_cast<double>(D) - static_cast<double>(K)) / static_cast<double>(S);
}

int main()
{
	uint64_t t, N, D, K, S;
	std::cin >> t;
	for (uint64_t i = 1; i <= t; ++i)
	{
		double worstT = 0;
		std::cin >> D >> N;
		for (uint64_t j = 1; j <= N; ++j)
		{
			std::cin >> K >> S;
			worstT = std::max(worstT, calcSpeed(D, K, S));
		}
		std::cout.precision(std::numeric_limits<double>::digits10);
		std::cout << "Case #" << i << ": " << std::fixed << static_cast<double>(D) / worstT << std::endl;
	}
    return 0;
}