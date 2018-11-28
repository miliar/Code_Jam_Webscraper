#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <memory>
#include <unordered_set>
#include <unordered_map>
#include <iterator>
#include <deque>
#include <queue>
#include <cmath>
#include <functional>
#include <numeric>
#include "stdio.h"
#include "time.h"
#include <climits>
#include <stdio.h> 
#include <tuple>
#include <fstream>

#ifdef SAMMAX
#include <ctime>
clock_t beg;
#endif

//#include <boost/lexical_cast.hpp>
//#include <boost/filesystem.hpp>
//#include <boost/utility.hpp>
//#include <boost/aligned_storage.hpp>

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define FORD(i,a,b) for (int i = (a); i > (b); --i)
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()
#define ABS(a) (((a) >= 0) ? (a) : -(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<vector<pair<int, int> > > VVPI;

const double EPS = 1e-8;

void init() {
#ifdef SAMMAX
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	beg = clock();
#else
	//std::ios_base::sync_with_stdio(false);
	//std::cin.tie(nullptr);
#endif  
}

void finish() {
#ifdef SAMMAX
	fprintf(stderr, "*** Total time: %.3lf ***\n", 1.0*(clock() - beg) / CLOCKS_PER_SEC);
#endif
}

int gcd(int a, int b) { return !a ? b : gcd(b % a, a); }
int lcm(int a, int b) { return a / gcd(a, b) * b; }

bool isBetter(pair<int, int> cur, pair<int, int> newOne) {
	//min(LS, RS) is maximal
	if (MIN(cur.first, cur.second) > MIN(newOne.first, newOne.second))
		return false;
	if (MIN(cur.first, cur.second) < MIN(newOne.first, newOne.second))
		return true;

	//max(LS, RS) is maximal
	if (MAX(cur.first, cur.second) > MAX(newOne.first, newOne.second))
		return false;
	if (MAX(cur.first, cur.second) < MAX(newOne.first, newOne.second))
		return true;

	//leftmost stall among those
	return false;
}

int main() {
	init();

	int t;
	cin >> t;
	FOR(caseNum, 1, t + 1) {
		int n, k;
		cin >> n >> k;

		vector<int> bathroom(n + 2, 0);
		bathroom[0] = bathroom[n + 1] = 1;

		int maxAns, minAns;

		FOR(i, 0, k) {
			vector<pair<int, int>> p(n + 2, make_pair(0, 0));

			FOR(j, 0, n + 2) {
				if (bathroom[j])
					continue;
				
				int L = 0;
				while (!bathroom[j - L])
					L++;

				int R = 0;
				while (!bathroom[j + R])
					R++;

				p[j] = make_pair(L, R);
			}

			int best = 0;
			FOR(j, 1, n + 2) {
				if (isBetter(p[best], p[j])) {
					best = j;
				}
			}

			bathroom[best] = 1;

			if (i == k - 1) {
				maxAns = MAX(p[best].first, p[best].second);
				minAns = MIN(p[best].first, p[best].second);
			}
		}

		printf("Case #%d: %d %d\n", caseNum, maxAns - 1, minAns - 1);
	}

	finish();
	return 0;
}