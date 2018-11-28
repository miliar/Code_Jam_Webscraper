#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

int main() {
	std::size_t cases;
	std::cin >> cases;
	for(std::size_t numCase = 0; numCase < cases; ++numCase)
	{
		long double d;
		int n;
		std::cin >> d;
		std::cin >> n;
		std::vector<long double> horses(n);
		for(std::size_t i = 0; i < n; ++i)
		{
			long double a,b;
			std::cin >> a >> b;
			horses[i] = (d - a) / b;
		}
		long double slowest_horse = *std::max_element(horses.begin(), horses.end());
		long double pace = d / slowest_horse;
		std::cout << "Case #" << numCase + 1 << ": " << std::fixed << std::setprecision(6) << pace << std::endl;
	}
	return 0;
}
