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

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		UI N, R, O, Y, G, B, V; cin >> N >> R >> O >> Y >> G >> B >> V;
		string result = "IMPOSSIBLE";
		if(R >= (G?G+1:0) && B >= (O?O+1:0) && Y >= (V?V+1:V)) {
			UI r = R-G, b = B-O, y = Y-V;
			UI m = max({r,b,y});
			char c1,c2,c3,cc1,cc2,cc3;UI n1,n2,n3,nn1,nn2,nn3;
			if(m*2 <= r+b+y) {
				if(m == r) { c1='R'; c2='B'; c3='Y'; cc1='G';cc2='O';cc3='V'; n1=r;n2=b;n3=y;nn1=G;nn2=O;nn3=V;}
				if(m == b) { c1='B'; c2='R'; c3='Y'; cc1='O';cc2='G';cc3='V'; n1=b;n2=r;n3=y;nn1=O;nn2=G;nn3=V;}
				if(m == y) { c1='Y'; c2='B'; c3='R'; cc1='V';cc2='O';cc3='G'; n1=y;n2=b;n3=r;nn1=V;nn2=O;nn3=G;}
				result = "";
				for(auto i: IR(0U,m)) {
					result+=c1; while(nn1>0) { result += cc1; result += c1; --nn1; }
					if(i<n2) {
						result+=c2; while(nn2>0) { result += cc2; result += c2; --nn2; }
					}
					if(i+n3>=m) {
						result+=c3; while(nn3>0) { result += cc3; result += c3; --nn3; }
					}
				}
			}
		} else if(R == G && B == 0 && O == 0 && Y == 0 && V == 0) {
			result = ""; for(auto i: IR(0U, R)) { result += "RG"; }
		} else if(B == O && R == 0 && G == 0 && Y == 0 && V == 0) {
			result = ""; for(auto i: IR(0U, B)) { result += "BO"; }
		} else if(Y == V && B == 0 && O == 0 && R == 0 && G == 0) {
			result = ""; for(auto i: IR(0U, Y)) { result += "YV"; }
		}
		cout << "Case #" << casenum+1 << ": " << result << endl;
	}

	return 0;
}
