// Cygwin clang++ 3.9.1 with -std=c++1z

#include <iostream>
#include <sstream>
#include <iomanip>

#include <iterator>

#include <algorithm>
#include <numeric>
#include <utility>
#include <limits>

#include <string>

#include <vector>
#include <deque>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>

#include <tuple>
#include <initializer_list>

#include <cmath>

// Boost library can be retrieved from http://www.boost.org/
// 1.60 is used

#pragma GCC diagnostic ignored "-Wconversion"
#include <boost/range/irange.hpp>
#include <boost/range/iterator_range.hpp>
#pragma GCC diagnostic warning "-Wconversion"

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned short US;
typedef unsigned char UC;

#define RNG(v) (v).begin(), (v).end()
#define REP(v, e) for(UI v = 0U; v < e; ++v)
#define REP_(v, s, e) for(UI v = s; v < e; ++v)
#define REPV(v, e) for(v = 0; v < e; ++v)
#define REPV_(v, s, e) for(v = s; v < e; ++v)

using namespace std;

template<class Integer>
inline boost::iterator_range< boost::range_detail::integer_iterator<Integer> >
IR(Integer first, Integer  last)
{ return boost::irange(first, last); }

bool check(const string& s)
{
	char c='0';
	for(auto cc: s) {
		if(c > cc) return false;
		c = cc;
	}
	return true;
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		string N; cin >> N; cin.ignore();
		ULL result = 0;
		auto tmp = stoull(N);
		if(check(N) && result < tmp) result = tmp;
		else {
			for(auto i: IR(0UL, N.size())) {
				if(N[i] != '0') {
					string s;
					if(i == 0 && N[i] == '1') {
						s = string(N.size()-1, '9');
					} else {
						s = N.substr(0, i)+char(N[i]-1)+string(N.size()-i-1, '9');
					}
					auto tmp = stoull(s);
					if(check(s) && result < tmp) result = tmp;
				}
			}
		}
		cout << "Case #" << casenum+1 << ": " << result << endl;
	}

	return 0;
}
