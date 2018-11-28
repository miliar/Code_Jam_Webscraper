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

void fill(vector<string> &m, UI sr, UI sc, UI er, UI ec, char ch)
{
	for(auto rr: IR(sr, er+1)) {
		for(auto cc: IR(sc, ec+1)) {
			assert(m[rr][cc] == '?' || m[rr][cc] == ch);
			m[rr][cc] = ch;
		}
	}
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		UI R, C; cin >> R >> C;
		vector<string> m(R);
		for(auto &val : m) cin >> val;
		UI sr = 0U, sc = 0U; char ch = '?';
		for(auto r: IR(0U, R)) {
			bool found = false; sc = 0U;
			for(auto c: IR(0U, C)) {
				if(m[r][c] != '?') {
					ch = m[r][c]; found = true;
					fill(m, sr, sc, r, c, ch); 
					sc = c+1; 
				}
			}
			if(found) {
				if(sc != C) {
					fill(m, sr, sc, r, C-1, ch); 
				}
				sr = r+1;
			}
		}
		if(sr != R) {
			for(auto r: IR(sr, R)) {
				m[r] = m[sr-1];
			}
		}
		cout << "Case #" << casenum+1 << ":" << endl;
		for(auto &val: m) { cout << val << endl; }
	}

	return 0;
}
