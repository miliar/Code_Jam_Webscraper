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
		string s; UI k, result = 0;
		cin >> s >> k;
		queue<bool> q;
		for(auto i: IR(0U, k)) q.push(false);
		bool f = false, st = false;
		for(auto i : IR<UI>(0U, s.size()-k+1)) {
			auto ff = q.front(); q.pop();
			st ^= ff;
			if((s[i] == '-') ^ st) {
				++result;
				st ^= true;
				f = true;
			} else {
				f = false;
			}
			q.push(f);
		}
		bool ok = true;
		for(auto i: IR(s.size()-k+1,s.size())) {
			auto ff = q.front(); q.pop();
			st ^= ff;
			if(st ? s[i] == '+' : s[i] == '-') {
				ok = false; break;
			}
		}
		if(ok) {
			cout << "Case #" << casenum+1 << ": " << result << endl;
		} else {
			cout << "Case #" << casenum+1 << ": " << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
