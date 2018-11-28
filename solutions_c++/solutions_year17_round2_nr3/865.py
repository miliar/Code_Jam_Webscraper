// Cygwin g++ 5.4.0 with -std=c++1z

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

long double calc(map<pair<int,int>, long double> &cache, const vector<UI> &E, const vector<UI> &S, const vector<vector<int>>& D, int city, int horse, UI rest)
{
	if(city == E.size()-1) return 0;
	if(cache.count({city,horse})==0) {
		long double temp = 1.0E+20;
		UI dist = D[city][city+1];
		if(dist <= rest) {
			temp = min(temp, (long double)dist/S[horse]+calc(cache,E,S,D,city+1,horse,rest-dist));
		}
		if(city != 0 && E[city]>=dist) {
			temp = min(temp, (long double)dist/S[city]+calc(cache,E,S,D,city+1,city,E[city]-dist));
		}
		cache[{city,horse}]=temp;
	}
	return cache[{city,horse}];
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		UI N, Q; cin >> N >> Q;
		vector<UI> E(N),S(N); for(auto i: IR(0U,N)) { cin >> E[i] >> S[i]; }
		vector<vector<int>> D(N, vector<int>(N));
		for(auto &v: D) { for(auto &val: v) { cin >> val; } }
		UI U,V; cin >> U >> V;
		map<pair<int,int>, long double> cache;
		long double result = calc(cache, E,S,D,0,0,E[0]);
		cout << "Case #" << casenum+1 << ": " << fixed << setprecision(10) << result << endl;
	}

	return 0;
}
