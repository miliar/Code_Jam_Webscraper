/*
VIM: let g:lcppflags="-std=c++11 -O2 -pthread"
VIM: let g:wcppflags="/O2 /EHsc /DWIN32"
*/

#include <assert.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <exception>
#include <stdexcept>
#include <map>
#include <set>
#include <list>
#include <vector>
#include <string>
#include <memory>
#include <functional>
#include <algorithm>
#include <utility>
#include <limits> 
#include <math.h>

typedef long long ll;
typedef std::vector<ll> vec;
void check(bool b) { if (!b) std::cerr << "error" << std::endl; }

template <typename T>
std::string to_string( T t ){
	std::stringstream ss;
	ss << t;
	return ss.str();
}

/*
Problem B. Tidy Numbers
Confused? Read the quick-start guide.
Small input
5 points	
You may try multiple times, with penalties for wrong submissions.
Large input
15 points	
You must solve the small input first.
You have 8 minutes to solve 1 input file. (Judged after contest.)
Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?
Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.
Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ N ≤ 1000.
Large dataset

1 ≤ N ≤ 1018.
Sample

Input
  	
Output
 

4
132
1000
7
111111111111111110

	

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

Note that the last sample case would not appear in the Small dataset.

*/

auto solve_puzzle(std::istream& is)
{
	std::string n;
	is >> n;

	for ( int i = 0; i < n.length()-1;  ){
		if ( n[i] <= n[i+1] ) {
			++i;
		} else {
			while ( i >= 0 && --n[i] < '0' ) {
				--i;
			}
			if ( i < 0 ) {
				return std::string("something is wrong.");
			}
			if ( i == 0 && n[i] == '0' ) {
				n = std::string( n.length()-1, '9');
				break;
			} else {
				for ( int j = i+1; j < n.length(); ++j ) {
					n[j] = '9';
				}
				--i;
			}
		}
	}

	return n;
}

void read_input_and_solve( std::istream& is, std::ostream& os ) 
{
	srand((unsigned)time(NULL));
	int puzzle_count;

	is >> puzzle_count;
	is.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for (int i = 1; i <= puzzle_count; i++)
	{
		os << "Case #" << i << ": ";
		auto r = solve_puzzle(is);
		os << r << std::endl;
	}
}

int main(int argc, char * argv[])
{
	try{
		if ( *++argv ) {
			std::ifstream ifs(*argv);
			read_input_and_solve( ifs, std::cout );
		} else {
			read_input_and_solve( std::cin, std::cout );
		}

		return 0;
	}
	catch (const std::exception& e)
	{
		std::cerr << std::endl
			<< "std::exception(\"" << e.what() << "\")." << std::endl;
		return 2;
	}
	catch (...)
	{
		std::cerr << std::endl
			<< "unknown exception." << std::endl;
		return 1;
	}
}
