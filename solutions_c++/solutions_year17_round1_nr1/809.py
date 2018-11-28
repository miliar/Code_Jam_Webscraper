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

void solve(vector<string> &vs)
{
    int R = vs.size();
    int C = vs[0].size();
    REP(i, R) {
        bool found = false;
        int lastPos = -1;
        REP(j, C) if (vs[i][j] != '?') {
            FOR(k, lastPos+1, j) if (vs[i][k] == '?') {
                vs[i][k] = vs[i][j];
            }
            lastPos = j;
        }
        if (lastPos != -1) {
            FOR(k, lastPos+1, C)
                vs[i][k] = vs[i][lastPos];
        }
        if (lastPos == -1 && i > 0) {
            REP(j, C) {
                assert(vs[i][j] == '?');
                vs[i][j] = vs[i-1][j];
            }
        }
    }

    for (int i=R-1; i>=0; i--) {
        if (vs[i][0] == '?') {
            assert(i+1 < R);
            REP(j, C) {
                assert(vs[i][j] == '?');
                vs[i][j] = vs[i+1][j];
            }
        }
    }
    REP(i, R) REP(j, C) assert(vs[i][j] != '?');
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int R, C;
        cin >> R >> C;
        vector<string> vs(R);
        REP(i, R) {
            cin >> vs[i];
            assert((int)vs[i].size() == C);
        }
        solve(vs);
        cout << "Case #" << _t+1 << ":" << endl;
        REP(i, R)
            cout << vs[i] << endl;
    }

    return 0;
}
