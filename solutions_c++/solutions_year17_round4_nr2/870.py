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
#include <cassert>

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
		int n,c,m;
		cin >> n >> c >> m;
		VI p(m), b(m);
		VVI tickets(c);
		VI npos(n);
		REP(i,m) {
			cin >> p[i] >> b[i];
			p[i]--;
			b[i]--;
			tickets[b[i]].push_back(p[i]);
			npos[p[i]]++;
		}

		REP(i,c) sort(ALL(tickets[i]));

		assert( c==2 );

		int nrides = 0, npromos = 0;

		nrides = max(npos[0],(int)max(tickets[0].size(),tickets[1].size()));

		REP(i,n) npromos = max(npromos,npos[i]-nrides);

		cout << "Case #" << run << ": ";
		cout << nrides << ' ' << npromos << endl;
	}

	return 0;
}
