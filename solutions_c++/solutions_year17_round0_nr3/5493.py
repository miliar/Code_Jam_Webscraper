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

void make_gauss_distro(
	const std::vector<bigint_t>& left_s,
	const std::vector<bigint_t>& right_s,
	std::vector<bigint_t>& output_gauss,
	std::size_t& global_maximum_index
)
{
	output_gauss.resize(left_s.size());
	global_maximum_index = 0;
	bigint_t max = 0;

	for(std::size_t i = 0; i < left_s.size(); i++)
	{
		output_gauss[i] = left_s[i] * right_s[i];

		if(output_gauss[i] > max)
		{
			global_maximum_index = i;
			max = output_gauss[i];
		}
	}
}

void get_lsrs(
	const std::vector<bool>& stalls,
	std::vector<bigint_t>& left_s,
	std::vector<bigint_t>& right_s
)
{
	bigint_t count = 0;

	left_s.resize(stalls.size());
	right_s.resize(stalls.size());

	for(std::size_t i = 0; i < stalls.size(); i++)
	{
		if(stalls[i])
		{
			count = 0;
		}

		left_s[i] = count++;
	}

	count = 0;

	for(std::size_t i = 0; i < stalls.size(); i++)
	{
		std::size_t j = stalls.size() - i - 1;

		if(stalls[j])
		{
			count = 0;
		}

		right_s[j] = count++;
	}
}

void solve(
	std::vector<bool>& stalls,
	const bigint_t& k,
	bigint_t& out_ls,
	bigint_t& out_rs
)
{
	std::vector<bigint_t> ls, rs, distro;
	std::size_t gmi = 0;

	//make_gauss_distro
	for(bigint_t i = 0; i < k; i++)
	{
		get_lsrs(stalls, ls, rs);
		make_gauss_distro(ls, rs, distro, gmi);

		//std::cout << "GMI" << gmi << std::endl;

		out_ls = ls[gmi];
		out_rs = rs[gmi];

		stalls[gmi] = true;

		/*
		for(bool b : stalls)
		{
			std::cout << (b? "0" : ".");
		}
		std::cout << std::endl;
		*/
	}
}

int main(int argc, char** argv)
{
	int cases = 0;

	std::cin >> cases;

	for(int t = 1; t <= cases; t++)
	{
		std::vector<bool> stalls;
		std::size_t n = 0;
		bigint_t k = 0, ls = 0, rs = 0;

		std::cin >> n >> k;

		stalls.resize(n + 2);
		stalls[0] = true;
		stalls[stalls.size() - 1] = true;

		solve(stalls, k, ls, rs);

		std::cout << "Case #" << t << ": "
			<< (std::max(ls, rs) - 1)
			<< " "
			<< (std::min(ls, rs) - 1)
			<< std::endl;
	}

	return EXIT_SUCCESS;
}

