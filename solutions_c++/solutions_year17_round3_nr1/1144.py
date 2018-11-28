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
	long long n, k, r, h;
	is >> n >> k;
	std::vector<std::pair<double,double>> v;
	for ( int i = 0; i < n; ++i){
		is >> r >> h;
		v.push_back(std::make_pair(r*r,2*h*r));
	}

	double mrr = 0, s2rh = 0;
	for ( int i = 0; i < k; ++i ) {
	
		auto mit = v.begin();
		for ( auto it = v.begin(); it != v.end(); ++it ) {
			if ( (std::max(it->first-mrr,0.) + it->second)
					>  (std::max(mit->first-mrr,0.) + mit->second) ) {
						mit = it;
			}
		}
		mrr = std::max(mit->first, mrr );
		s2rh += mit->second;
		mit->first = 0;
		mit->second = 0;
	}

	return 3.14159265359 * (s2rh + mrr); 
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
