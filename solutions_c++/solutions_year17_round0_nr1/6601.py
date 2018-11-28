#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

//#define _USE_STDIO

#ifdef _USE_STDIO
std::istream& input = std::cin;
std::ostream& output = std::cout;
#else
std::istream& input = std::ifstream("D:\\ainput.txt");
std::ostream& output = std::ofstream("D:\\aoutput.txt");
#endif

int main()
{
	int t;
	input >> t;

	for (int i = 0; i < t; ++i)
	{
		std::string s;
		int k;
		input >> s >> k;

		std::vector<bool> bs;
		int flipped = 0;

		for (auto c : s)
		{
			bs.push_back(c == '+');
		}

		while (!bs.empty())
		{
			if (bs.front())
			{
				bs.erase(bs.begin());
				continue;
			}

			if (bs.size() < k)
			{
				flipped = -1;
				break;
			}

			for (int idx = 0; idx < k; ++idx)
			{
				bs[idx] = !bs[idx];
			}

			flipped++;
		}

		output << "Case #" << i + 1 << ": " << (flipped >= 0 ? std::to_string(flipped) : "IMPOSSIBLE") << std::endl;
	}
}