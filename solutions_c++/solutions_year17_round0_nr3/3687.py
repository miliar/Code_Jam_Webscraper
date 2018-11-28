#include <iostream>
#include <map>

typedef long long int64_t;
typedef std::map<int64_t, int> int64_map;

inline void print_left_right_stall(int64_t min, int64_t max)
{
	std::cout << max << " " << min << std::endl;
}

inline void put_empty_stall(int64_map& empty_stall, int64_t left, int64_t right)
{
	int64_t max = left >= right ? left : right;
	int64_t min = left >= right ? right : left;
	++empty_stall[max];
	++empty_stall[min];
}

inline void remove_node(int64_map& empty_stall)
{
	auto it = empty_stall.rbegin();
	if (!--it->second)
	{
		empty_stall.erase(it->first);
	}
}

void calculate_last_left_right_stall(int64_t number_of_bathroom, int64_t number_of_people)
{
	if (number_of_bathroom == number_of_people)
	{
		print_left_right_stall(0, 0);
		return;
	}

	int64_map empty_stall;
	empty_stall[number_of_bathroom] = 1;
	int64_t left = 0;
	int64_t right = 0;
	while (number_of_people > 0)
	{
		int64_t empty = empty_stall.rbegin()->first - 1;
		left = empty / 2;
		right = empty - left;
		put_empty_stall(empty_stall, left, right);
		remove_node(empty_stall);
		--number_of_people;
	}

	print_left_right_stall(left >= right ? right : left, left >= right ? left : right);
}

int main(void)
{
	size_t total_test_case;
	std::cin >> total_test_case;
	size_t count = 0;
	while (count < total_test_case)
	{
		uint64_t number_of_bathroom;
		uint64_t number_of_people;
		std::cin >> number_of_bathroom >> number_of_people;
		std::cout << "Case #" << count + 1 << ": ";
		calculate_last_left_right_stall(number_of_bathroom, number_of_people);
		++count;
	}
}