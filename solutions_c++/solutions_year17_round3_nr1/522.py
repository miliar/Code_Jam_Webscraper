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

const long double PI = 3.14159265358979323846;

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		UI N,K; cin >> N >> K;
		vector<UI> R(N),H(N);
		for(auto i: IR(0U,N)) { cin >> R[i] >> H[i]; }
		vector<UI> idxR(N); iota(RNG(idxR), 0);
		sort(RNG(idxR), [&R](UI n1, UI n2) { return R[n1] > R[n2]; });
		long double result = 0;
		for(auto i: IR(0U, N)) {
			vector<UI> idxRN;
			copy_if(RNG(idxR), back_inserter(idxRN), [&R,&idxR,i](UI n){ return n != idxR[i] && R[n]<=R[idxR[i]]; });
			if(idxRN.size() < K-1) break;
			sort(RNG(idxRN), [&R,&H](UI n1, UI n2){ return R[n1]*(ULL)H[n1] > R[n2]*(ULL)H[n2]; });
			long double temp = PI * R[idxR[i]] * R[idxR[i]] + 2 * PI * R[idxR[i]]* H[idxR[i]];
			for(auto j: IR(0U, K-1)) {
				temp += 2*PI*R[idxRN[j]]*H[idxRN[j]];
			}
			result = max(result, temp);
		}
		cout << "Case #" << casenum+1 << ": " << setprecision(20) << result << endl;
	}

	return 0;
}
