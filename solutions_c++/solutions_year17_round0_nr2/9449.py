#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using ull = unsigned long long;

bool istidy(ull x)
{
	while (x > 0)
	{
		if (x % 10 < (x /= 10) % 10)
		{
			return 0;
		}
	}
	return 1;
}

int main(int argc, char const *argv[])
{
	if (argc < 3)
	{
		std::cerr << "Syntax: <program> <in> <out>\n";
		return -1;
	}
	std::ifstream ifs(argv[1]);
	std::ofstream ofs(argv[2]);
	std::cout.rdbuf(ofs.rdbuf());
	std::cin.rdbuf(ifs.rdbuf());
	int t;
	std::cin >> t;
	for (int x = 1; x <= t; ++x)
	{
		ull n;
		std::cin >> n;
		std::vector<int> d;
		auto y = n;
		while (y > 0)
		{
			d.push_back(y % 10);
			y /= 10;
		}

		y = n;
		while (!istidy(y))
		{

			for (auto i = d.begin(); i < d.end() - 1; ++i)
			{
				if (*i < *(i + 1))
				{
					--*(i + 1);
					for (auto j = i; j >= d.begin(); --j)
					{
						*j = 9;
					}
				}
			}

			y = 0;
			for (auto i = d.end() - 1; i >= d.begin(); --i)
			{
				y *= 10;
				y += *i;
			}
		}
		std::cout << "Case #" << x << ": " << y << '\n';
	}
	return 0;
}