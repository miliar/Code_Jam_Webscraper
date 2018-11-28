#include <iostream>
#include <string>
#include <array>
#include <vector>
#include <algorithm>
#include <cmath>

typedef short int Digit;

long int digitsToLong(std::vector<Digit> digits)
{
	std::reverse(digits.begin(), digits.end());

	long int value = 0;

	for (long int i = 0; i < digits.size(); i++)
		value += (long int)(digits[i] * std::pow(10, i));

	return value;
}

class TidyNumber
{
public:
	explicit TidyNumber(long int number)
	{
		this->number = number;
	}

	explicit TidyNumber(const std::vector<Digit>& digits)
	{
		this->number = digitsToLong(digits);
	}

	const std::vector<Digit> digitVector()
	{
		std::vector<Digit> digits;
		long int current = this->number;
		while (current > 0)
		{
			Digit digit = current % 10;
			digits.push_back(digit);
			current /= 10;
		}

		std::reverse(digits.begin(), digits.end());

//		for (size_t i = 0; i < digits.size(); i++)
//			std::cout << "Digit " << i << ": " << digits[i] << std::endl;

		return digits;
	}

	bool isTidy()
	{
		std::vector<Digit> digits = this->digitVector();

		for (size_t i = 1; i < digits.size(); i++)
			if (digits[i - 1] > digits[i])
				return false;

		return true;
	}

	TidyNumber lastTidy()
	{
		if (this->isTidy())
			return *this;

		std::vector<Digit> digits = this->digitVector();

		for (size_t i = 0; i < digits.size() - 1; )
		{
			if (digits[i] > digits[i + 1])
			{
				digits[i]--;
				for (size_t j = i + 1; j < digits.size(); j++)
					digits[j] = 9;

				i = 0;
			}

			else
				i++;
		}

		return TidyNumber(digits);
	}

	long int getValue() const
	{ return this->number; }

private:
	long int number;
};

int main(int arg, const char* argv[])
{
	long int cases = 0;

	std::cin >> cases;

	for (long int currentCase = 1; currentCase <= cases; currentCase++)
	{
		long int input;
		std::cin >> input;

		TidyNumber number(input);
		std::cout << "Case #" << currentCase << ": " << number.lastTidy().getValue() << std::endl;
	}

	return 0;
}
