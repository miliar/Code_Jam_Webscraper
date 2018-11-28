// Cygwin clang++ 5.4.0 with -std=c++1z

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
		UI N,K; cin >> N >> K;
		long double U; cin >> U;
		vector<long double> P(N); for(auto &v: P) { cin >> v; }
		long double l = 0, r = 1; // ok, bad
		for(auto i: IR(0U, 1000000U)) {
			long double b = (l+r)/2;
			long double need = 0;
			for(const auto &v : P) {
				if(b > v) need += b - v;
			}
			if(need <= U) {
				l = b;
			} else {
				r = b;
			}
		}
		long double result = accumulate(RNG(P), (long double)1, [l](long double acc, long double val) {
			if(l > val) return acc * l;
			return acc * val;
		});
		cout << "Case #" << casenum+1 << ": " << setprecision(20) << result << endl;
	}

	return 0;
}
