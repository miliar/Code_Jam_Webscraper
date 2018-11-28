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

string solve(string S, const int K)
{
    int N = S.size();
    int ret = 0;
    REP(i, N-K+1) {
        if (S[i] == '-') {
            REP(j, K) {
                if (S[i+j] == '-') S[i+j] = '+';
                else S[i+j] = '-';
            }
            ++ret;
        }
    }
    REP(i, N) {
        if (S[i] == '-')
            return "IMPOSSIBLE";
    }
    return toS(ret);
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        string S;
        cin >> S;
        int K;
        cin >> K;
        cout << "Case #" << _t+1 << ": " << solve(S, K) << endl;
    }

    return 0;
}
