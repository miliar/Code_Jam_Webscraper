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

int N, K, S[MAXN];

void flip(int index) {
	for(int i = index; i < index+K && i < N; ++i) S[i] = !S[i];
}

int main(int argc, char* argv[]) {
	// initialization
 	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;

	for(int tc = 1; tc <= T; ++tc) {
		// initialization
		string s;

		// input
		cin >> s >> K;
		N = s.length();
		for(int i = 0; i < N; ++i) S[i] = s[i] == '+' ? 0 : 1;
		
		// main program
		bool found = true; // found solution
		int ans = 0;
		for(int i = 0; i < N-K+1; ++i) {
			if(S[i] == 1) { // S[i] is not happy
				flip(i);
				ans++;
				// for(int i = 0; i < N; ++i) cout << S[i];
				// cout << endl;
			}
		}
		for(int i = N-K+1; i < N; ++i) {
			if(S[i] != 0) found = false;
		}
			
		// output
		cout << "Case #" << tc << ": ";
		if(found) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
 	
	return 0;
}
