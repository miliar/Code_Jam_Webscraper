#include <math.h>
#include <iostream>
#include <vector>

void insertNumber(std::vector<int> &vect, int num)
{
	if (num > 0)
	{
		insertNumber(vect, num / 10);
		vect.push_back(num % 10);
	}
}

void main()
{
	int cases;
	std::cin >> cases;

	for (int i = 0; i < cases; ++i)
	{
		long long input;
		std::cin >> input;

		if (input < 10)
		{
			std::cout << "Case #" << i + 1 << ": " << input << std::endl;
			continue;
		}

		long long t = input;

		std::vector<int> numberVector;
		insertNumber(numberVector, input);

		for (int j = 1; j < numberVector.size(); ++j)
		{
			if (numberVector[j] < numberVector[j - 1])
			{
				int k = j;
				while (k < numberVector.size())
				{
					numberVector[k] = 9;
					++k;
				}
				numberVector[j - 1] -= 1;
				int l = j - 1;
				while (l > 0 && numberVector[l] < numberVector[l - 1])
				{
					numberVector[l] = 9;
					numberVector[l - 1] -= 1;
					--l;
				}
			}
		}

		long long output = 0;
		for (int z = 0; z < numberVector.size(); ++z)
		{
			output = output * 10 + numberVector[z];
		}
		std::cout << "Case #" << i + 1 << ": " << output << std::endl;
	}
}