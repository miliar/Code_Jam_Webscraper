#include <iostream>
#include <algorithm>
using namespace std;

void togglePlusMinus(std::string& io_str, std::size_t indexStart, std::size_t num)
{
	for(std::size_t i = 0; i < num; ++i)
		io_str[i + indexStart] = (io_str[i + indexStart] == '+') ? '-' : '+';
}

int main() {
	std::size_t n;
	std::cin >> n;
	for(std::size_t numCase = 0; numCase < n; ++numCase)
	{
		std::string str;
		std::cin >> str;
		std::size_t k;
		std::cin >> k;
		std::size_t count = 0;
		for(std::size_t i = 0; i < str.length() - k + 1; ++i)
		{
			if (str[i] == '-')
			{
				togglePlusMinus(str, i, k);
				++count;
			}
		}
		std::cout << "Case #" << numCase + 1 << ": ";
		if (std::find(std::end(str) - k, std::end(str), '-') != std::end(str))
			std::cout << "IMPOSSIBLE" << std::endl;
		else
			std::cout << count << std::endl;
		
	}
	return 0;
}
