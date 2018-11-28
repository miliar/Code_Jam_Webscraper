#include <iostream> // std::cout; std::cin
#include <fstream> // std::fstream::open; std::fstream::close; 
#include <cstdlib> // rand
#include <cassert> // assert
#include <cctype> // isalnum; isalpha; isdigit; islower; isupper; isspace; tolower; toupper
#include <cmath> // pow; sqrt; round; fabs; abs; log
#include <climits> // INT_MIN; INT_MAX; LLONG_MIN; LLONG_MAX; ULLONG_MAX
#include <cfloat> // DBL_EPSILON; LDBL_EPSILON
#include <cstring> // std::memset
#include <algorithm> // std::swap; std::max; std::min; std::min_element; std::max_element; std::minmax_element; std::next_permutation; std::prev_permutation; std::nth_element; std::sort; std::lower_bound; std::upper_bound; std::reverse
#include <limits> // std::numeric_limits<int>::min; std::numeric_limits<int>::max; std::numeric_limits<double>::epsilon; std::numeric_limits<long double>::epsilon;
#include <numeric> // std::accumulate; std::iota
#include <string> // std::to_string; std::string::npos; std::stoul; std::stoull; std::stoi; std::stol; std::stoll; std::stof; std::stod; std::stold; 
#include <list> // std::list::merge; std::list::splice; std::list::merge; std::list::unique; std::list::sort
#include <bitset>
#include <vector>
#include <deque>
#include <stack> // std::stack::top; std::stack::pop; std::stack::push
#include <queue> // std::queue::front; std::queue::back; std::queue::pop; std::queue::push
#include <set> // std::set::count; std::set::find; std::set::equal_range; std::set::lower_bound; std::set::upper_bound
#include <map> // std::map::count; std::map::find; std::map::equal_range; std::map::lower_bound; std::map::upper_bound
#include <unordered_set>
#include <unordered_map>
#include <utility> // std::pair; std::make_pair
#include <iterator>
#include <functional> // std::less<int>; std::greater<int>
using namespace std;

class Solution {
public:
	int oversizedPancakeFlipper(string& s, const int idx, const int k) {
		if (s == string(s.size(), '+')) {
			return 0;
		}
		for (int i = idx, n = s.size(); i + k <= n; i++) {
			if (s.at(i) == '-') {
				for (int j = 0; j < k; j++) {
					s.at(i + j) = s.at(i + j) == '-' ? '+' : '-';
				}
				int result = oversizedPancakeFlipper(s, i + 1, k);
				if (result >= 0) {
					return result + 1;
				}
				for (int j = 0; j < k; j++) {
					s.at(i + j) = s.at(i + j) == '-' ? '+' : '-';
				}
			}
		}
		return -1;
	}
};

int main(void) {
	Solution solution;
	int T, val, k;
	string s;

	fstream x, y;
	x.open("A-small-attempt2.in", fstream::in);
	y.open("A-small-attempt2.out", fstream::out);
	x >> T;
	for (int i = 1; i <= T; i++) {
		s.clear();
		x >> s >> k;
		val = solution.oversizedPancakeFlipper(s, 0, k);
		if (val < 0) {
			y << "Case #" << i << ": IMPOSSIBLE\n";
		}
		else {
			y << "Case #" << i << ": " << val << '\n';
		}
	}
	y.close();
	x.close();

	// string s;
	// int k = 0, result = 0, answer = 0;
	// s = "---+-++-";
	// k = 3;
	// answer = 3;
	// result = solution.oversizedPancakeFlipper(s, k);
	// assert(answer == result);

	// s = "+++++";
	// k = 4;
	// answer = 0;
	// result = solution.oversizedPancakeFlipper(s, k);
	// assert(answer == result);

	// s = "-+-+-";
	// k = 4;
	// answer = -1;
	// result = solution.oversizedPancakeFlipper(s, k);
	// assert(answer == result);

	// cout << "\nPassed All\n";
	return 0;
}