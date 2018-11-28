#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <iomanip>
#include <limits>
using namespace std;
 
#define FORi(m) for( int i = 0; i < (m); ++i )
#define FOR(i, M) for( int i = 0; i < (M); ++i )
#define FOR1(i, M) for( int i = 1; i <= (M); ++i )
#define DEBUGGING 0
#define CERRL() if (DEBUGGING) { std::cerr << '\n'; }
#define EXAM(var) if (DEBUGGING) { std::cerr << #var << ": " << (var) << '\n'; }
#define EXAMARR(var) if (DEBUGGING) { std::cerr << #var << ": "; for (const auto& _var_: var) std::cerr << _var_ << " "; std::cerr << '\n'; }


class Case {
public:
	long double D;
	int N;
	vector<long double> positions;
	vector<long double> speeds;
	Case(long double D, int N): D(D), N(N), positions(N), speeds(N) {}
	Case() {}
} CASE;

long double solve() {
	long double M = 0;
	FOR(i, CASE.N) {
		EXAM(CASE.positions[i]);
		long double rem = CASE.D - CASE.positions[i];
		EXAM(rem);
		M = max(M, rem/CASE.speeds[i]);
		EXAM(M);
	}
	return CASE.D / M;
}

 
int main() {
    int T;
    cin >> T;
    FOR1(t, T) {
        long double D;
		int N;
        cin >> D >> N;
        
		CASE = Case(D, N);
        
        FOR(n, N) {
        	cin >> CASE.positions[n] >> CASE.speeds[n];
		}
        long double maxspeeed = solve();
        cout << "Case #" << t << ": " << fixed << setprecision(6) << maxspeeed << endl;
    }
}
