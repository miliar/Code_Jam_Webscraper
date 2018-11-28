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

bool check(deque<pair<UI,UI>>&spec, UI s, UI e)
{
	if(s > e) {
		return check(spec, 0, e) && check(spec, s, 1440);
	}
	for(const auto &v: spec) {
		if(v.second <= s || e <= v.first) {
		} else return false;
	}
	return true;
}

UI period(UI s, UI e)
{
	if(s > e) return e+1440-s;
	return e-s;
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		UI Ac,Aj; cin >> Ac >> Aj;
		if(Ac == 0) swap(Ac,Aj);
		deque<pair<UI,UI>> C(Ac),J(Aj);
		for(auto i: IR(0U, Ac)) { cin >> C[i].first >> C[i].second; }
		for(auto i: IR(0U, Aj)) { cin >> J[i].first >> J[i].second; }
		sort(RNG(C)); sort(RNG(J));
		UI Tj = accumulate(RNG(C), 0, [](UI acc, pair<UI,UI>&v) { return acc+(v.second-v.first); });
		UI Tc = accumulate(RNG(J), 0, [](UI acc, pair<UI,UI>&v) { return acc+(v.second-v.first); });
		while(true) {
			if(C.size() != 0) {
				UI can = 720 - Tj; auto canit = C.end();
				auto it = C.begin();
				auto next = it; ++next;
				while(next != C.end()) {
					if(check(J, it->second, next->first) && can >= (next->first-it->second)) {
						can = next->first - it->second; canit = it;
					}
					it = next;
					++next;
				}
				auto p = period(C.back().second, C.front().first);
				if(p > 0 && check(J, C.back().second, C.front().first) && can >= p) {
					Tj += p;
					C.front().first = 0;
					C.back().second = 1440;
					continue;
				} else if(canit != C.end()) {
					auto f = canit->first;
					auto s = canit->second;
					auto next = C.erase(canit);
					Tj += next->first - s;
					next->first = f;
					continue;
				}
			}
			if(J.size() != 0) {
				UI can = 720 - Tc; auto canit = J.end();
				auto it = J.begin();
				auto next = it; ++next;
				while(next != J.end()) {
					if(check(C, it->second, next->first) && can >= (next->first-it->second)) {
						can = next->first - it->second; canit = it;
					}
					it = next;
					++next;
				}
				auto p = period(J.back().second, J.front().first);
				if(p > 0 && check(C, J.back().second, J.front().first) && can >= p) {
					Tc += p;
					J.front().first = 0;
					J.back().second = 1440;
					continue;
				} else if(canit != J.end()) {
					auto f = canit->first;
					auto s = canit->second;
					auto next = J.erase(canit);
					Tc += next->first - s;
					next->first = f;
					continue;
				}
			}
			break;
		}
#if 0
cout << "-C-" << endl;
for(const auto &v : C) { cout << v.first << '-' << v.second << endl; }
cout << "-J-" << endl;
for(const auto &v : J) { cout << v.first << '-' << v.second << endl; }
cout << "---" << endl;
#endif
		UI result = 0; bool isC = false, isJ = false;
		auto itC = C.begin(), itJ = J.begin();
		while(itC != C.end() || itJ != J.end()) {
			if(itC != C.end() && (itJ == J.end() || itC->first < itJ->first)) {
				if(isC) ++result;
				++result;
				++itC; isC = true; isJ = false; continue;
			}
			if(itJ != J.end() && (itC == C.end() || itC->first > itJ->first)) {
				if(isJ) ++result;
				++result;
				++itJ; isJ = true; isC = false; continue;
			}
		}
		if(C.size()&&(C.front().first==0&&C.back().second==1440)||J.size()&&(J.front().first==0&&J.back().second==1440)) --result;
		if(result%2) ++result;
		cout << "Case #" << casenum+1 << ": " << result << endl;
	}

	return 0;
}
