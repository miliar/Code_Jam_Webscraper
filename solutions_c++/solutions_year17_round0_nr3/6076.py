#include <algorithm>
#include <fstream>
#include <iostream>
#include <queue>
#include <tuple>

bool using_stdio = false;

std::pair<long long, long long> split(long long n)
{
	return std::make_pair(n / 2, n / 2 + (n % 2));
}

void do_solve(std::istream& input, std::ostream& output)
{
	int t;
	input >> t;

	for (int i = 0; i < t; ++i)
	{
		long long n, k;
		input >> n >> k;

		long long ls, rs;

		std::priority_queue<long long> spaces;
		spaces.push(n);

		for (long long j = 0; j < k; ++j)
		{
			long long max_space = spaces.top();
			std::tie(ls, rs) = split(max_space - 1);
			spaces.pop();
			spaces.push(ls);
			spaces.push(rs);
		}

		output << "Case #" << i + 1 << ": " << std::max(ls, rs) << " " << std::min(ls, rs) << std::endl;
	}
}

int main()
{
	if (using_stdio)
	{
		do_solve(std::cin, std::cout);
	}
	else
	{
		do_solve(std::ifstream("D:\\cinput.txt"), std::ofstream("D:\\coutput.txt"));
	}
}