#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

bool use_stdio = false;

void do_solve(std::istream& input, std::ostream& output)
{
	int t;
	input >> t;

	for (int i = 0; i < t; ++i)
	{
		std::string n;
		input >> n;

		std::vector<int> digits;

		for (auto c : n)
		{
			digits.push_back(c - '0');
		}

		auto itr = digits.begin();

		while (itr != digits.end())
		{
			int prev_digit = itr == digits.begin() ? 0 : *(itr - 1);
			int next_digit = itr + 1 == digits.end() ? 9 : *(itr + 1);

			if (std::min(9, *itr) > next_digit)
			{
				*itr = *itr - 1;
				*(itr + 1) = *(itr + 1) + 10;
			}

			if (std::max(*itr, 0) < prev_digit)
			{
				itr--;
				continue;
			}

			*itr = std::min(*itr, 9);
			itr++;
		}
		
		long long result = 0;
		for (auto n : digits)
		{
			result = result * 10 + n;
		}

		output << "Case #" << (i + 1) << ": " << result << std::endl;
	}
}

int main()
{
	if (use_stdio)
	{
		do_solve(std::cin, std::cout);
	}
	else
	{
		do_solve(std::ifstream("D:\\binput.txt"), std::ofstream("D:\\boutput.txt"));
	}
}