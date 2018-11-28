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

int solveB(int N, int P, vector<int> G)
{
    assert(N <= 8);
    sort(G.begin(), G.end());
    int ans = 0;
    do {
        int cur = 0;
        int cnt = 0;
        REP(i, N) {
            if (cur == 0)
                ++cnt;
            cur = (cur + G[i]) % P;
        }
        ans = max(ans, cnt);
    } while(next_permutation(G.begin(), G.end()));
    return ans;
}

int solveR(int N, int P, vector<int> G)
{
    vector<int> C(P, 0);
    REP(i, N)
        ++C[G[i]%P];
    if (P == 2) {
        return C[0] + (C[1]+1)/2;
    }
    else if (P == 3) {
        int minC = min(C[1], C[2]);
        int maxC = max(C[1], C[2]);
        int left = maxC - minC;
        return C[0] + minC + (left+2)/3;
    }
    else {
        assert(P == 4);
        int c0 = C[0];
        int c2 = C[2]/2;
        int c2_left = C[2]%2;
        int c13 = min(C[1], C[3]);
        int c13_left = max(C[1], C[3])-c13;
        int ans = c0 + c2 + c13;
        //cerr << "c0: " << c0 << endl;
        //cerr << "c2: " << c2 << endl;
        //cerr << "c13: " << c13 << endl;
        if (c2_left == 1) {
            if (c13_left >= 2) {
                c2_left = 0;
                c13_left -= 2;
                ans++;
            }
        }
        ans += (c13_left+3)/4;
        if (c13_left == 0 && c2_left == 1)
            ans++;
        return ans;
    }
}

int solve(int N, int P, vector<int> G)
{
    int ans = solveR(N, P, G);
    if (N <= 8) {
        int ref = solveB(N, P, G);
        //cerr << ans << "," << ref << endl;
        if (ans != ref) {
            vector<int> C(P, 0);
            REP(i, N)
                ++C[G[i]%P];
            REP(i, P)
                cerr << C[i] << endl;
        }
        assert(ans == ref);
    }
    return ans;
}

int main(void)
{
    #if 0
    {
        int N = 8;
        int P = 4;
        while(true) {
            vector<int> G(N);
            REP(i, N)
                G[i] = rand()%100;
            solve(N, P, G);
            cerr << "OK" << endl;
        }
    }
    #endif
    int T;
    cin >> T;
    REP(_t, T) {
        int N, P;
        cin >> N >> P;
        vector<int> G(N);
        REP(i, N)
            cin >> G[i];
        cout << "Case #" << _t+1 << ": " << solve(N, P, G) << endl;
    }

    return 0;
}
