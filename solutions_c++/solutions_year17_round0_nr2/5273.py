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

using bigint_t = boost::multiprecision::int128_t;

constexpr const char* digits = "9876543210 ";
constexpr const int digits_nbr = 10;

void convert_to_int(std::string a, bigint_t& r)
{
	while((a.size() > 0) && (a.front() == '0'))
		a.replace(0, 1, "");

	if(a.size() == 0)
		a = "0";

	std::istringstream ain(a);

	ain >> r;
}

bool less_than(std::string a, std::string b)
{
	bigint_t ab = 0;
	bigint_t bb = 0;

	convert_to_int(a, ab);
	convert_to_int(b, bb);

	return ab <= bb;
}

bool is_tidy(const std::string& n)
{
	for(std::size_t i = 1; i < n.size(); i++)
	{
		if(n[i - 1] > n[i])
			return false;
	}

	return true;
}

int char_to_int(char c)
{
	return c - '0';
}

bool recsolve(const std::string& n, bigint_t& at, std::string& current, bigint_t& delta)
{
	if(is_tidy(n))
	{
		convert_to_int(n, at);
		current = "";
		delta = 0;
		return false;
	}

	while(!is_tidy(current))
	{
		std::size_t ix = 0;

		for(std::size_t i = 1; i < current.size(); i++)
		{
			if(char_to_int(current[i - 1]) > char_to_int(current[i]))
			{
				ix = i;
				break;
			}
		}

		while(current[ix - 1] == '0')
		{
			ix--;
		}

		//std::cout << ix << "=" << std::string(1, static_cast<char>((char_to_int(n[ix - 1]) - 1) + '0')) << std::endl;

		current.replace(ix - 1, 1, std::string(1, static_cast<char>((char_to_int(n[ix - 1]) - 1) + '0')));
		current.replace(ix, current.size(), std::string(current.size() - ix, '9'));

		//std::cout << "&" << current << std::endl;
	}

	convert_to_int(current, at);

	return true;
}

int main(int argc, char** argv)
{
	int cases = 0;

	std::cin >> cases;

	for(int t = 1; t <= cases; t++)
	{
		std::string n = "", tidy = "";
		bigint_t result = -1, delta = 0;

		std::cin >> n;

		tidy = n;

		recsolve(n, result, tidy, delta);

		if(result == 0)
			result = 1;

		std::cout << "Case #" << t << ": " << result << std::endl;

		//
	}

	return EXIT_SUCCESS;
}

