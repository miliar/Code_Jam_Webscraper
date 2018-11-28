
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstdint>

bool IsTidy(uint64_t number)
{
	std::string val = std::to_string(number);
	char prev = val[0];
	for (int i = 1; i < val.length(); i++)
	{
		if (prev > val[i])
		{
			return false;
		}
		prev = val[i];
	}
	return true;
}

void Solve(uint64_t number, size_t index)
{
	uint64_t i = number;
	for (; !IsTidy(i); i--)
	{
	}
	std::cout << "Case #" << index << ": " << i << std::endl;
}

int main()
{
	size_t num = 0;
	std::cin >> num;
	for (size_t i = 0; i < num; i++)
	{
		uint64_t number;
		std::cin >> number;
		Solve(number, i+1);
	}
    return 0;
}

