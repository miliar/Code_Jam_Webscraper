#include <cstdint>
#include <list>
#include <iostream>
#include <vector>
namespace tidy_numbers
{
std::vector< std::uint64_t > getDigits( std::uint64_t number )
{
	std::list< std::uint64_t > digits;
	while (number)
	{
		digits.push_front(number % 10);
		number /= 10;
	}
	return std::vector< std::uint64_t >(std::begin(digits), std::end( digits ) );
}

auto findNinesBegin(std::vector< std::uint64_t > digits)
{
	std::uint64_t prevDigit = 0;
	std::size_t substructIndex = 0;
	std::size_t current = 0;
	for (;current < digits.size(); ++current)
	{
		auto digit = digits[current];
		if (digit < prevDigit)
		{
			break;
		}
		else 
		{
			if (prevDigit - digit > 1)
			{
				substructIndex = current;
			}
			prevDigit = digit;
		}
	}
	return digits.size() == current ? digits.size() : substructIndex;
}
std::uint64_t previous( std::uint64_t number )
{

	auto digits = getDigits(number);
	auto ninesBegin = findNinesBegin(digits);
	if (ninesBegin >= digits.size())
		return number;
	
	std::uint64_t result = 0; 
	for (std::size_t i = 0; i < digits.size(); ++i)
	{
		auto digit = digits[i];
		std::uint64_t nextDigit = (i > ninesBegin) ? 9 : digit;
		result *= 10;
		result += nextDigit;
		if (i == ninesBegin)
		{
			result -= 1;
		}
		
	}
	
	return result;
}
} // namespace tidy_numbers
int main()
{
	int cases;
	std::cin >> cases;
	for (int i = 0; i < cases; ++i)
	{
		std::string cakes;
		std::uint64_t number = 0;
		std::cin >> number;
		int result = tidy_numbers::previous( number);
		std::cout << "Case #" << i + 1 << ": " << result << std::endl;
	}
}