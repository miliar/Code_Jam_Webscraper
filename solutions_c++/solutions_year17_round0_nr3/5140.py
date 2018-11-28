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

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		ULL N, K; cin >> N >> K;
		map<ULL, ULL> m = { { N, 1 } };
		ULL l, r;
		while(K-->0) {
			auto back = *--(m.end());
			r = back.first / 2;
			l = back.first - r - 1;
			if(m.count(l)==0) m[l] = 0;
			if(m.count(r)==0) m[r] = 0;
			++m[l]; ++m[r];
			if(back.second == 1) {
				m.erase(back.first);
			} else {
				--m[back.first];
			}
		}
		cout << "Case #" << casenum+1 << ": " << max(l,r) << ' ' << min(l,r) << endl;
	}

	return 0;
}
