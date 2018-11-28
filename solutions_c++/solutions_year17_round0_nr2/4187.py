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

#define MAXN 1000 + 10
#define MAXM 1000 + 10

set<long long> possible;
void construct(int i, int prev_dig, long long current) {
	if(i == 18) {
		possible.insert(current);
		return;
	}

	for(int d = 0; d <= 9; ++d) {
		if(d >= prev_dig) construct(i+1, d, current*10+d);
	}
}	
	
int main(int argc, char* argv[]) {
	// initialization
 	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	construct(0, 0, 0);

	for(int tc = 1; tc <= T; ++tc) {
		// initialization
		long long N;

		// input
		cin >> N;

		// main program
		long long ans = *(--possible.upper_bound(N));
		
		// output
		cout << "Case #" << tc << ": " << ans <<  endl;
	}
	return 0;
}
