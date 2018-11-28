#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <functional>
#include <numeric>
#include <cmath>
#include <string>
#include <cctype>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

#define ALL(x) ((x).begin()),((x).end())
#if __cplusplus >= 201103L
#define FOR(i,c) for(auto i=c.begin(); i!=c.end(); ++i)
#define REP(i,n) for(decltype(n) i=0; i<(n); ++i)
#else
#define FOR(i,c) for(typeof(c.begin()) i=c.begin(); i!=c.end(); ++i)
#define REP(i,n) for(typeof(n) i=0; i<(n); ++i)
#endif

const int infty = 999999999;

const int dx[8] = {  1, 0,-1, 0, 1,-1,-1, 1 };
const int dy[8] = {  0, 1, 0,-1, 1, 1,-1,-1 };

template<class T> void minimize(T &a, T b) { a = min(a,b); }
template<class T> void maximize(T &a, T b) { a = max(a,b); }

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) fprintf(stderr,__VA_ARGS__)
#else
#define debug(...)
#endif

const string let("RYB"), opp("GVO");
int main()
{
	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {

		int n;
		vector<int> col(3), mix(3);
		cin >> n >> col[0] >> mix[2] >> col[1] >> mix[0] >> col[2] >> mix[1];

		int ncol = col[0] + col[1] + col[2];

		string res;
		REP(i,3) {
			if ( 2*col[i]>ncol || col[i]<mix[i] ) {
				res = "IMPOSSIBLE";
				break;
			}
		}

		if ( res.empty() ) {
			int last = -1;
			REP(i,3) if ( col[i]>0 ) {
				res += let[i]; col[i]--;
				while ( mix[i]>0 ) {
					res += opp[i]; mix[i]--;
					res += let[i]; col[i]--;
				}
				last = i;
				break;
			}
			debug("init last = %d, col = %d,%d,%d, res = %s\n",
			       last,col[0],col[1],col[2],res.c_str());
			while ( col[0]>0 || col[1]>0 || col[2]>0 ) {
				REP(i,3) if ( i!=last && col[i]>=col[3-i-last] ) {
					res += let[i]; col[i]--;
					while ( mix[i]>0 ) {
						res += opp[i]; mix[i]--;
						res += let[i]; col[i]--;
					}
					last = i;
					debug("last = %d, col = %d,%d,%d, res = %s\n",
					       last,col[0],col[1],col[2],res.c_str());
					break;
				}
			}
		}

		cout << "Case #" << run << ": ";
		cout << res << endl;
	}

	return 0;
}
