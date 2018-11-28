#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <sstream>

int main() {
	std::size_t cases;
	std::cin >> cases;
	for(std::size_t numCase = 0; numCase < cases; ++numCase)
	{
		int n, r, o, y, g, b, v;
		std::cin >> n >> r >> o >> y >> g >> b >> v;
		if (r > b + y || b > r + y || y > b + r)
		{
			std::cout << "Case #" << numCase + 1 << ": " << "IMPOSSIBLE" << std::endl;
		}
		else
		{
			std::stringstream ss;
			bool r_last = false;
			bool b_last = false;
			bool y_last = false;
			
			if (r >= b && r >= y)
			{
					ss << "R";
					r_last = true;
					b_last = false;
					y_last = false;
					--r;
			}
			else if (b >= r && b >= y)
			{
					ss << "B";
					b_last = true;
					r_last = false;
					y_last = false;
					--b;
			}
			else if (y >= b && y >= r)
			{
					ss << "Y";
					y_last = true;
					b_last = false;
					r_last = false;
					--y;
			}
			
			while(r > 0 || b > 0 || y > 0)
			{
				if (!r_last && ((b_last && r >= y) || (y_last && r >= b)))
				{
					ss << "R";
					r_last = true;
					b_last = false;
					y_last = false;
					--r;
					continue;
				}
				if (!b_last && ((r_last && b >= y) || (y_last && b >= r)))
				{
					ss << "B";
					r_last = false;
					b_last = true;
					y_last = false;
					--b;
					continue;
				}
				if (!y_last && ((r_last && y >= b) || (b_last && y >= r)))
				{
					ss << "Y";
					r_last = false;
					b_last = false;
					y_last = true;
					--y;
					continue;
				}

			}
			std::string res =  ss.str();
			if (res.front() == res.back())
			{
				std::swap(res[res.length() - 1], res[res.length() - 2]);
			}
			std::cout << "Case #" << numCase + 1 << ": " << res << std::endl;
		}
	}
	return 0;
}
