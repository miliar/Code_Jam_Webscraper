#include <iostream>
#include <vector>

uint64_t solve (uint64_t n)
{
	// 4
	// 132
	// 1000
	// 7
	// 111111111111111110
	std::vector<int> digits;
	while (n > 10)
	{
		digits.push_back(n % 10);
		n /= 10;
	}
	digits.push_back(n);

	for (int i = 0; i < digits.size() - 1; ++i)
	{
		if (digits[i] < digits[i + 1] || digits[i] == 0)
		{
			for(int k = i; k >= 0; --k)
				digits[k] = 9;
			digits[i + 1]--;
			if (digits[i + 1] < 0)
				digits[i + 1] = 9;
		}	
	}

	n = 0;
	uint64_t mul = 1;
	for (int i = 0; i < digits.size(); ++i)
	{
		n += digits[i] * mul;
		mul *= 10;
	}

	return n;
}


int main ()
{
	int cases_num;
	std::cin >> cases_num;

	for (int current_case = 1; current_case <= cases_num; ++current_case)
	{
		uint64_t n;
		std::cin >> n;

		std::cout << "Case #" << current_case << ": "; 
		n = solve(n);
		std::cout << n;
		if (current_case != cases_num)
			std::cout << std::endl;
	}

	return 0;
}


