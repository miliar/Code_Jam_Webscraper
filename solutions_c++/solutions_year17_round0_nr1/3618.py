#include <iostream>
#include <string>

static const char happy = '+';
static const char blank = '-';

size_t check_pancake(std::string const& pancake, size_t start, size_t flipper)
{
	for (size_t i = start; i < start + flipper; ++i)
	{
		if (pancake[i] == blank)
		{
			return i;
		}
	}
	return start + flipper;
}

size_t flip_pancake_once(std::string& pancake, size_t start, size_t flipper)
{
	for (size_t i = start; i < start + flipper; ++i)
	{
		pancake[i] = (pancake[i] == blank ? happy : blank);
	}
	return check_pancake(pancake, start, flipper);
}

bool is_remain_all_happy(std::string const& pancake, size_t start)
{
	for (size_t i = 0; i < pancake.length(); ++i)
	{
		if (pancake[i] == blank)
		{
			return false;
		}
	}
	return true;
}

void flip_pancake(std::string& pancake, size_t flipper)
{
	size_t start = 0;
	size_t flip_count = 0;
	while (start <= pancake.length() - flipper)
	{
		if (pancake[start] == blank)
		{
			start = flip_pancake_once(pancake, start, flipper);
			++flip_count;
		}
		else
		{
			++start;
		}
	}

	if (start == pancake.length() || is_remain_all_happy(pancake, start))
	{
		std::cout << flip_count << std::endl;
	}
	else
	{
		std::cout << "IMPOSSIBLE" << std::endl;
	}
}

int main(void)
{
	size_t total_test_case;
	std::cin >> total_test_case;
	size_t count = 0;
	while (count < total_test_case)
	{
		std::string pancake;
		size_t flipper;
		std::cin >> pancake >> flipper;

		std::cout << "Case #" << count + 1 << ": ";
		flip_pancake(pancake, flipper);
		++count;
	}
}