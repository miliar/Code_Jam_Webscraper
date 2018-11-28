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


int n, q;
VVI d;
VI e, s;

struct pos {
	double t;
	int i,e,h;

	pos(double t_, int i_, int e_, int h_): t(t_), i(i_), e(e_), h(h_) {}

	int operator <(const pos a) const { return t>a.t; }

};


int main()
{
	cout << setprecision(15);

	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {

		cin >> n >> q;

		d = VVI(n,VI(n));
		e = s = VI(n);

		REP(i,n) cin >> e[i] >> s[i];
		REP(i,n) REP(j,n) cin >> d[i][j];

		vector<double> res;

		int a,b;
		REP(k,q) {
			cin >> a >> b;
			a--; b--;

			VVI visited(n,VI(n,0));

			priority_queue<pos> que;
			que.push(pos(0.0,a,0,a));

			while ( !que.empty() ) {
				pos curr = que.top(); que.pop();

				if ( visited[curr.i][curr.h] ) continue;
				visited[curr.i][curr.h] = 1;

				if ( curr.i==b ) {
					res.push_back(curr.t);
					break;
				}

				REP(j,n) if ( d[curr.i][j]>0 ) {
					if ( curr.e>=d[curr.i][j] ) {
						que.push(pos(curr.t+(double)d[curr.i][j]/s[curr.h],
						             j,curr.e-d[curr.i][j],curr.h));
					}
					if ( e[curr.i]>=d[curr.i][j] ) {
						que.push(pos(curr.t+(double)d[curr.i][j]/s[curr.i],
						             j,e[curr.i]-d[curr.i][j],curr.i));
					}
				}
			}

		}

		cout << "Case #" << run << ":";
		REP(i,res.size()) cout << ' ' << res[i];
		cout << endl;
	}

	return 0;
}
