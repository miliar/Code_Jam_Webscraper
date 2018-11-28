#include <iostream>
#include <stdlib.h> 

void fillWithNine(std::string& str, std::size_t indexStart)
{
	for(std::size_t i = indexStart; i < str.length(); ++i)
		str[i] = '9';
}

int main() {
	std::size_t n;
	std::cin >> n;
	for(std::size_t numCase = 0; numCase < n; ++numCase)
	{
		long long k;
		std::cin >> k;
		std::string str = std::to_string(k);
		for(std::size_t i = str.length() - 1; i > 0; --i)
		{
			if (str[i] < str[i-1])
			{
				--str[i-1];
				fillWithNine(str, i);
			}
		}
		std::cout << "Case #" << numCase + 1 << ": " <<std::atoll(str.c_str()) << std::endl;
	}
	return 0;
}
