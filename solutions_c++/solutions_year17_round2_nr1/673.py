//#define _GLIBCXX_DEBUG
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <climits> 
#include <cfloat> 
#include <map> 
#include <utility> 
#include <set> 
#include <iostream>
#include <iomanip>
#include <memory> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <sstream> 
#include <complex> 
#include <stack> 
#include <queue> 
#include <numeric>
#include <cassert>
#include <gmpxx.h>

#define FOR(i, min, max) for (int i = (min); i < (max); ++i) 
#define FORE(i, min, max) for (int i = (min); i <= (max); ++i) 
#define REP(i, n) for (int i = 0; i < (n); ++i) 
#define REPV(vec, i) for (int i = 0; i < (int)(vec.size()); ++i) 
#define FOR_EACH(vec, it) for (typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); ++it)

using namespace std; 
static const double EPS = 1e-12; 
typedef long long ll; 
typedef mpz_class bint;

template<typename T>
string toS(const T &d) {
    ostringstream oss;
    oss << d;
    return oss.str();
}

long double solve(int D, int N, vector<int> K, vector<int> S)
{
    long double maxTime = -1.0;
    REP(i, N) {
        long double t = (long double)(D-K[i])/(long double)S[i];
        if (t > maxTime) {
            maxTime = t;
        }
    }
    return D/maxTime;
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int D, N;
        cin >> D >> N;
        vector<int> K(N);
        vector<int> S(N);
        REP(i, N)
            cin >> K[i] >> S[i];
        long double ans = solve(D, N, K, S);
        printf("Case #%d: %.10Lf\n", _t+1, ans);
        //cout << "Case #" << _t+1 << ": " << setprecision(10) << solve(D, N, K, S) << endl;
    }

    return 0;
}
