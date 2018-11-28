#include <fstream>
#include <string>
#include <vector>

uint64_t solve(uint64_t value)
{
	std::vector<size_t> digits;
	uint64_t res = 0;

	do
	{
		size_t digit = value % 10;
		digits.push_back(digit);
		value /= 10;
	} while (value);

	size_t lastDigit = 0;
	size_t pos = 0;
	for (size_t i = 0; i < digits.size(); ++i)
	{
		if (lastDigit < digits[i] && 0 !=i) 
		{
			pos = i;
			digits[i] -= 1;
		}

		lastDigit = digits[i];
	}

	for (size_t i = digits.size() - 1; ; --i)
	{
		uint64_t power = i != 0 ? 10 : 1;
		if (i < pos)
		{
			res = (res + 9) * power;
		}
		else
		{
			res = (res + digits[i]) * power;
		}

		if (0 == i)
		{
			break;
		}
	}

	return res;
}

void main()
{
	std::ifstream in("d:\\GoogleCodeJam2017\\Qualification\\input.txt");
	std::ofstream out("d:\\GoogleCodeJam2017\\Qualification\\output.txt");

	size_t count = 0;
	in >> count;
	if (0 > count)
	{
		count = 0;
	}

	size_t number;
	for (size_t i = 0; i < count && !in.eof(); ++i)
	{
		uint64_t value;
		in >> value;

		const auto res = solve(value);

		out << "Case #" << i + 1 << ": ";
		out << res;
		out << std::endl;
	}

	in.close();
	out.close();
}