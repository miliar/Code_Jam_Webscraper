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

int main()
{
	cout << setprecision(15);

	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {
		int n, p, g;
		cin >> n >> p;
		VI nmod(4);
		REP(i,n) { cin >> g; nmod[g%p]++; }

		int res = -1;
		int x,y;
		switch ( p ) {
		case 2:
			res = nmod[0] + (nmod[1]+1)/2;
			break;

		case 3:
			x = min(nmod[1],nmod[2]);
			y = max(nmod[1],nmod[2]) - x;
			res = nmod[0] + x + (y+2)/3;
			break;

		case 4:
			x = nmod[2]/2;
			nmod[2] -= 2*x;
			y = min(nmod[1],nmod[3]);
			nmod[1] -= y;
			nmod[3] -= y;
			res = nmod[0] + x + y;
			if ( nmod[2]!=0 && max(nmod[1],nmod[3])>=2 ) {
				res++;
				if ( nmod[1]>0 ) nmod[1] -= 2;
				if ( nmod[3]>0 ) nmod[3] -= 2;
			}
			x = max(nmod[1],nmod[3]);
			res += x/4; x = x%4;
			if ( nmod[2]>0 || x>0 ) res++;
			break;

		default: return 1;
		}

		cout << "Case #" << run << ": ";
		cout << res << endl;
	}

	return 0;
}
