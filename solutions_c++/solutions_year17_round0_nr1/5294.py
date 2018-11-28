/*
 * Basic Google CodeJam C++ boilerplate.
 *
 * This program uses C++14 (G++ 5.4) and uses the available STDLIB on
 * G++ (GCC) 5.4.0 for C++14, Eigen 3.3.3 and use Boost 1.63.0:
 *
 * http://www.boost.org/ (Boost)
 * http://eigen.tuxfamily.org/index.php?title=Main_Page (Eigen)
*/

#include <iostream>
#include <sstream>
#include <iomanip>
#include <functional>
#include <utility>
#include <algorithm>
#include <string>
#include <vector>
#include <array>
#include <stack>
#include <deque>
#include <map>
#include <memory>
#include <numeric>
#include <type_traits>
#include <exception>
#include <stdexcept>
#include <ratio>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>

#include <Eigen/Core>
#include <Eigen/Geometry>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/float128.hpp>

void flip(int w, std::string& p)
{
	for(int i = 0; i < p.size(); i++)
	{
		if(p[i] == '-')
		{
			int s = i;

			if((i + w) >= p.size())
			{
				s = p.size() - w;
			}

			for(int j = 0; j < w; j++)
			{
				p[j + s] = (p[j + s] == '+')? '-' : '+';
			}

			return;
		}
	}
}

bool finished(const std::string& p)
{
	for(char i : p)
	{
		if(i == '-')
			return false;
	}

	return true;
}

int solve(int w, std::string& p)
{
	int i = 0;
	constexpr int max = 1e6;

	while((!finished(p)) && (i < max))
	{
		flip(w, p);
		i++;
		//std::cout << "=" << p << std::endl;
	}

	return (i >= max)? -1 : i;
}

int main(int argc, char** argv)
{
	int cases = 0;

	std::cin >> cases;

	for(int t = 1; t <= cases; t++)
	{
		std::string p = "";
		int w = 0;
		int s = 0;

		std::cin >> p >> w;

		std::cout << "Case #" << t << ": ";

		s = solve(w, p);

		if(s < 0)
		{
			std::cout << "IMPOSSIBLE";
		}
		else
		{
			std::cout << s;
		}

		std::cout << std::endl;
	}

	return EXIT_SUCCESS;
}

