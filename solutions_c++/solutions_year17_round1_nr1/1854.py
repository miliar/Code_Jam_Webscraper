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

std::vector<std::vector<char>> mat;

void print_mat(void)
{
	for(auto& i : mat)
	{
		for(auto& j : i)
		{
			std::cout << j;
		}

		std::cout << std::endl;
	}
}

bool expand_left(int r, int c)
{
	bool have_int = false;

	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
		{
			if(mat[i][j] == '?')
				continue;

			have_int = true;

			for(int ip = i + 1; ip < r; ip++)
			{
				if(mat[ip][j] != '?')
					break;

				mat[ip][j] = mat[i][j];
			}
		}
	}

	return have_int;
}

bool expand_right(int r, int c)
{
	bool have_int = false;

	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
		{
			if(mat[i][j] == '?')
				continue;

			have_int = true;

			for(int ip = i - 1; ip >= 0; ip--)
			{
				if(mat[ip][j] != '?')
					break;

				mat[ip][j] = mat[i][j];
			}
		}
	}

	return have_int;
}

bool expand_up(int r, int c)
{
	bool have_int = false;

	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
		{
			if(mat[i][j] == '?')
				continue;

			have_int = true;

			for(int jp = j + 1; jp < c; jp++)
			{
				if(mat[i][jp] != '?')
					break;

				mat[i][jp] = mat[i][j];
			}
		}
	}

	return have_int;
}

bool expand_down(int r, int c)
{
	bool have_int = false;

	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
		{
			if(mat[i][j] == '?')
				continue;

			have_int = true;

			for(int jp = j - 1; jp >= 0; jp--)
			{
				if(mat[i][jp] != '?')
					break;

				mat[i][jp] = mat[i][j];
			}
		}
	}

	return have_int;
}

void solve_mat(int r, int c)
{
	if(!expand_left(r, c))
		return;
	//std::cout << "---------------------" << std::endl;
	//print_mat();
	if(!expand_right(r, c))
		return;
	//std::cout << "---------------------" << std::endl;
	//print_mat();
	if(!expand_down(r, c))
		return;
	//std::cout << "---------------------" << std::endl;
	//print_mat();
	if(!expand_up(r, c))
		return;
	//std::cout << "---------------------" << std::endl;
	//print_mat();
	//std::cout << "---------------------" << std::endl;
}

int main(int argc, char** argv)
{
	int cases = 0;

	std::cin >> cases;

	for(int t = 1; t <= cases; t++)
	{
		int r = 0, c = 0;

		std::cin >> r >> c;

		mat.clear();
		mat.resize(r, std::vector<char>(c, '?'));

		for(int i = 0; i < r; i++)
		{
			std::string line = "";

			std::cin >> line;

			for(int j = 0; j < c; j++)
			{
				mat[i][j] = line[j];
			}
		}

		std::cout << "Case #" << t << ":" << std::endl;

		solve_mat(r, c);

		print_mat();
	}

	return EXIT_SUCCESS;
}

