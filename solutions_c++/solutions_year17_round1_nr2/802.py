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

#include <boost/graph/edmonds_karp_max_flow.hpp>
#include <boost/graph/adjacency_list.hpp>

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

using namespace boost;

typedef adjacency_list_traits < setS, vecS, directedS > Traits;
typedef adjacency_list < setS, vecS, directedS,
  no_property, property < edge_capacity_t, int,
  property < edge_residual_capacity_t, int,
  property < edge_reverse_t, Traits::edge_descriptor > > > > Graph;

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		UI N, P; cin >> N >> P;
		vector<UI> R(N); for(auto &val: R) { cin >> val; }
		vector<vector<UI>> Q(N, vector<UI>(P));
		for(auto i: IR(0U, N)) {
			for(auto &val: Q[i]) {
				cin >> val;
			}
		}
		Graph g;
		for(auto i: IR(0U, N*P+2)) { add_vertex(g); }
		const UI start = N*P, goal = N*P+1;
		auto capacity = get(edge_capacity, g);
		auto rev = get(edge_reverse, g);
		UI m = 0, k = 1;
		while(m < 1111111) {
			vector<UI> r(N); transform(RNG(R), r.begin(), [k](UI x){ return x*k; });
			vector<vector<UI>> cand(N);
			for(auto i: IR(0U, N)) {
				for(auto j: IR(0U, P)) {
					if(r[i]*9 <= Q[i][j]*10 && Q[i][j]*10 <= r[i]*11) {
						cand[i].push_back(j);
					}
				}
			}
			for(auto p: cand[0]) {
				auto pp = add_edge(start, p, g);
				if(pp.second) {
					auto r = add_edge(p, start, g);
					rev[pp.first] = r.first; rev[r.first] = pp.first; capacity[pp.first] = 1;
				}
			}
			for(auto i: IR(0U, N-1)) {
				for(auto p1: cand[i]) {
					for(auto p2: cand[i+1]) {
						auto i1 = P*i+p1, i2 = P*(i+1)+p2;
						auto p = add_edge(i1, i2, g);
						if(p.second) {
							auto rr = add_edge(i2, i1, g);
							rev[p.first] = rr.first; rev[rr.first] = p.first; capacity[p.first] = 1;
						}
					}
				}
			}
			for(auto p: cand[N-1]) {
				auto pp = add_edge(P*(N-1)+p, goal, g);
				if(pp.second) {
					auto r = add_edge(goal, p, g);
					rev[pp.first] = r.first; rev[r.first] = pp.first; capacity[pp.first] = 1;
				}
			}
			m = *max_element(RNG(r));
			++k;
		}
#if 0
		auto eg = edges(g);
		for(auto i = eg.first; i != eg.second; ++i) {
			cout << source(*i, g) << "->" << target(*i, g) << ':' << capacity[*i] << endl;
		}
#endif
		auto result = edmonds_karp_max_flow(g, start, goal);
		cout << "Case #" << casenum+1 << ": " << result << endl;
	}

	return 0;
}
