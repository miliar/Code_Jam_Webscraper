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
#include <limits>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>

#include <Eigen/Core>
#include <Eigen/Geometry>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/float128.hpp>

std::vector<std::pair<int, long double>> horses;

long double TimeToReach(std::pair<int, long double>& horse, int to)
{
	return static_cast<long double>(to - horse.first) / horse.second;
}

long double Solve(int to)
{
	int p = 0;
	long double v = 0;
	long double tm = 0;

	for(auto& h : horses)
	{
		if(TimeToReach(h, to) > tm)
		{
			p = h.first;
			v = h.second;
			tm = TimeToReach(h, to);
		}
	}

	return static_cast<long double>(to) / tm;
}

int main(int argc, char** argv)
{
	int cases = 0;

	std::cin >> cases;

	std::cout << std::fixed << std::setprecision(std::numeric_limits<long double>::digits10);

	for(int t = 1; t <= cases; t++)
	{
		int D = 0, N = 0;

		horses.clear();
		horses.resize(0);

		std::cin >> D >> N;

		horses.reserve(N);

		for(int n = 0; n < N; n++)
		{
			int Hp = 0;
			long double Hv = 0;
			std::cin >> Hp >> Hv;

			horses.push_back(std::make_pair<int, long double>(std::move(Hp), std::move(Hv)));
		}

		std::cout << "Case #" << t << ": " << Solve(D) << std::endl;
	}

	return EXIT_SUCCESS;
}

