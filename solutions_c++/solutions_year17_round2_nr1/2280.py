#include <bits/stdc++.h>
using namespace std;

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i, n) for(int i=0;i<(n);i++)
#define FOR(i, a, b) for(int i=(a);i<=(b);i++)
#define FORD(i, a, b) for(int i=(a);i>=(b);i--)

inline bool EQ(double a, double b) { return fabs(a - b) < 1e-9; }

int main() {
    ios::sync_with_stdio(false);
    int T, D, N;
    cin >> T;
    int test = 1;
    double max_t = -1;
    double ki, si;
    cout << fixed << setprecision(6);
    while (test <= T) {
    	cin >> D >> N;
    	max_t = -1;
    	for(int i = 0; i < N; ++i) {
    		cin >> ki >> si;
    		max_t = max(max_t, (D-ki)/si);
    	}	

		cout << "Case #" << test++ << ": ";
		cout << (D / max_t) << endl;
    }
    return 0;
}