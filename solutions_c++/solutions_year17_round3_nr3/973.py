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
*/

auto solve_puzzle(std::istream& is)
{
	long long n, k;
	is >> n >> k;
	double u, p;
	is >> u;
	std::vector<double> v;
	for ( auto i = 0; i < n; ++i ) {
		is >> p;
		v.push_back(p);
	}
	std::sort(v.begin(), v.end());

	for ( int i = 1; i < v.size() && u > 0.; ++i) {
		if ( v[i-1] == v[i] )
			continue;

		double dd = std::min( (v[i] - v[i-1])*i, u );
		u -= dd; 
		double d = dd / i;
		for ( int j = 0; j < i; ++j )
			v[j] += d;
	}
	if ( u > 0. ) {
		double d = u/n;
		for ( int j = 0; j < n; ++j )
			v[j] += d;
	}

	double pp = 1.0;
	for ( auto p : v ) {
		pp *= (p > 1.) ? 1. : p;
	}

	return pp;
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
		os << std::fixed << r << std::endl;
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
