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
Problem C. Bathroom Stalls
Confused? Read the quick-start guide.
Small input 1
5 points	
You may try multiple times, with penalties for wrong submissions.
Small input 2
10 points	
You must solve small input 1 first.
You may try multiple times, with penalties for wrong submissions.
Large input
15 points	
You must solve all small inputs first.
You have 8 minutes to solve 1 input file. (Judged after contest.)
Problem

A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.

K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.

When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?
Solving this problem

This problem has 2 Small datasets and 1 Large dataset. You must solve the first Small dataset before you can attempt the second Small dataset. You will be able to retry either of the Small datasets (with a time penalty). You will be able to make a single attempt at the Large, as usual, only after solving both Small datasets.
Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with two integers N and K, as described above.
Output

For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is max(LS, RS), and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S.
Limits

1 ≤ T ≤ 100.
1 ≤ K ≤ N.
Small dataset 1

1 ≤ N ≤ 1000.
Small dataset 2

1 ≤ N ≤ 106.
Large dataset

1 ≤ N ≤ 1018.
Sample

Input
  	
Output
 

5
4 2
5 2
6 2
1000 1000
1000 1

	

Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499

In Case #1, the first person occupies the leftmost of the middle two stalls, leaving the following configuration (O stands for an occupied stall and . for an empty one): O.O..O. Then, the second and last person occupies the stall immediately to the right, leaving 1 empty stall on one side and none on the other.

In Case #2, the first person occupies the middle stall, getting to O..O..O. Then, the second and last person occupies the leftmost stall.

In Case #3, the first person occupies the leftmost of the two middle stalls, leaving O..O...O. The second person then occupies the middle of the three consecutive empty stalls.

In Case #4, every stall is occupied at the end, no matter what the stall choices are.

In Case #5, the first and only person chooses the leftmost middle stall.

*/

auto solve_puzzle(std::istream& is)
{
	long long n, k;
	is >> n >> k;

	long long sec=1;
	for ( long long kk = k; kk; kk>>=1, sec<<=1 ); //exp2( (int)ceil(log2( k+1 )) );
	long long empty = n - sec +1;
	long long min = empty / sec;
	long long rem = empty % sec;
	long long max = min;
	if ( (rem - (sec/2)) >= (k-sec/2+1) ) {
		max = min += 1;
	} else if ( rem >= (k-sec/2+1) ) {
		max = min + 1;
	}

#if 0
	int best_min, best_max, best_place;
	std::vector<int> v( n, 0);
	for ( int i = 0; i <k; ++i ){
		best_min = best_max = best_place = -1;
		for ( int j = 0; j < n; ++j ){
			if ( v[j] == 0 ){
				int Ls = 0;
				int Rs = 0;
				for ( int l = j-1; l >= 0 && v[l] == 0; --l ) {
					++Ls;
				}
				for ( int l = j+1; l < n && v[l] == 0; ++l ) {
					++Rs;
				}
				int j_min = std::min(Ls,Rs);
				int j_max = std::max(Ls,Rs);
				if ( best_min < j_min
					|| best_min == j_min && best_max < j_max ) {
					best_place = j;
					best_min = j_min;
					best_max = j_max;
				}
			}
		}
		v[best_place] = 1;
	}

	if ( best_min != min || best_max != max ) {
		std::cout << "Error: " << n << " " << k << " -> " << best_max << " " << best_min << " -> ";
	}
#endif
	return to_string(max) + ' ' + to_string(min);
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
