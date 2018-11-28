
#include <bits/stdc++.h>
using namespace std;
#define SQUARE(x)   ((x)*(x))
#define X           first
#define Y           second
#define EPS         (1e-8)
#define INF         (int)INFINITY
#define MOD         (1000000007)
#define PI          (acos(-1.0))
#ifdef DEBUG
#include "debug.cpp"
// #include "testlib.h"
#else
#define deb(...)
#endif
// ----------

typedef pair<long long, long long> intvl;

struct compare {
	bool operator()(const intvl &l, const intvl &r) const {
		if(l.X < r.X) return true;
		else if(l.X == r.X && l.Y > r.Y) return true;
		else return false;
	}
};

#define MAXN 1000000000000000000 + 10

long long N, K;
set<long long> stalls;

int main(int argc, char* argv[]) {
	// initialization
 	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;

	for(int tc = 1; tc <= T; ++tc) {
		// initialization
		stalls.clear();
		
		// input
		cin >> N >> K;
		
		// main program
		stalls.insert(0);
		stalls.insert(N+1);
		long long min_s, max_s, opt_s;
		priority_queue<intvl, vector<intvl>, compare> max_intvl;
		max_intvl.push({N, 0});

		for(long long p = 1; p <= K; ++p) {
			min_s = -1;
			max_s = -1;
			intvl next_s = max_intvl.top();
			max_intvl.pop();
			//for(set<long long>::iterator it = stalls.begin(); it != stalls.end(); ++it) {
			set<long long>::iterator it = stalls.find(next_s.Y);

			// if(it == --stalls.end()) it = stalls.begin();
				
			long long s = ( (*it) + (*(stalls.upper_bound(*it))) ) / 2;
			//if(stalls.find(s) == stalls.end()) {
				long long ls = s-(*(--stalls.lower_bound(s)))-1;
				long long rs = (*(stalls.upper_bound(s)))-s-1;
				if(min(ls, rs) > min_s) {
					min_s = min(ls, rs);
					max_s = max(ls, rs);
					opt_s = s;
				} else if(min(ls, rs) == min_s) {
					if(max(ls, rs) > max_s) {
						min_s = min(ls, rs);
						max_s = max(ls, rs);
						opt_s = s;
					}
				}
			//}
			
			max_intvl.push({ls, next_s.Y});
			max_intvl.push({rs, opt_s});

			//}
			if(min_s == 0 && max_s == 0) break;
			stalls.insert(opt_s);
		}
		
		// output
		cout << "Case #" << tc << ": " << max_s << " " << min_s << endl;
	}

	return 0;
}
