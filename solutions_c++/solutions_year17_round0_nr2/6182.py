#define TEST

#ifdef TEST 
#define _CRT_SECURE_NO_WARNINGS
#endif


#include <iostream>
#include <string>


int main()
{
#ifdef TEST
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "wb", stdout);
#endif

	int numOfTestcases;
	std::cin >> numOfTestcases;

	for (int i = 0; i < numOfTestcases; ++i)
	{
		std::cout << "Case #" << (i + 1) << ": ";

		std::string number;
		std::cin >> number;

		// search for first decrease
		// populate it back until there is a different number
		// fill the number up with 9s from that point on
		size_t position = -1;
		for (size_t i = 1; i < number.size(); ++i)
		{
			if (number[i - 1] > number[i])
			{
				position = i - 1;
				break;
			}
		}

		// number is not good
		if (position != -1)
		{
			// decrease previous digits if needed
			number[position]--;
			while (position > 0 && number[position] == number[position - 1] - 1)
			{
				number[position - 1]--;
				position--;
			}

			// if first digit is 0, remove it and let all other digits be 9
			if (number[0] == '0') position = 0;
			for (size_t i = position + 1; i < number.size(); ++i)
			{
				number[i] = '9';
			}
		}

		bool found = false;
		for (char c : number)
		{
			if (c != '0') found = true;
			if (found) std::cout << c;
		}
		std::cout << std::endl;
	}
}