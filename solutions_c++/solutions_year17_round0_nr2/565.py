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

ll toLL(string s) {
    istringstream iss(s);
    ll ret;
    iss >> ret;
    return ret;
}

bool isTidy(string S) {
    int size = S.size();
    REP(i, size-1)
        if (S[i] > S[i+1])
            return false;
    return true;
}

string solve(ll N)
{
    string S = toS(N);
    int size = S.size();
    REP(i, size-1) {
        if (S[i] > S[i+1]) {
            string prefix = toS(toLL(S.substr(0, i+1))-1);
            if (!isTidy(prefix)) {
                prefix = solve(toLL(prefix));
            }
            if (prefix == "0")
                prefix = "";
            return prefix + string(size-(i+1), '9');
        }
    }
    return S;
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        ll N;
        cin >> N;
        string ans = solve(N);
        assert(isTidy(ans));
        assert(toLL(ans) <= N);
        cout << "Case #" << _t+1 << ": " << ans << endl;
    }

    return 0;
}
