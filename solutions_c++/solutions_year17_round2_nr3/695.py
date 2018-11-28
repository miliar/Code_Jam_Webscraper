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
static const long double EPS = 1e-8; 
typedef long long ll; 
typedef mpz_class bint;

template<typename T>
string toS(const T &d) {
    ostringstream oss;
    oss << d;
    return oss.str();
}

vector<long double> solve(int N, int QN, vector<int> E, vector<int> S, vector<vector<int> > D, vector<int> U, vector<int> V)
{
    vector<vector<ll> > CD(N, vector<ll>(N));
    REP(i, N) REP(j, N) {
        if (D[i][j] == -1)
            CD[i][j] = LONG_LONG_MAX;
        else
            CD[i][j] = D[i][j];
    }
    REP(i, N) CD[i][i] = 0;
    REP(k, N) REP(i, N) REP(j, N) if (CD[i][k] != LONG_LONG_MAX && CD[k][j] != LONG_LONG_MAX) {
        CD[i][j] = min(CD[i][j], CD[i][k]+CD[k][j]);
    }

    vector<long double> ans;
    REP(q, QN) {
        int start = U[q];
        int end = V[q];
        vector<long double> mem(N, DBL_MAX);
        mem[start] = 0.0;
        pair<long double, int> st{0, start};
        priority_queue<pair<long double, int> > Q;
        Q.push(st);
        while(!Q.empty()) {
            long double t = -Q.top().first;
            int i = Q.top().second;
            Q.pop();
            if (i == end) {
                ans.push_back(t);
                break;
            }
            if (mem[i]+EPS < t)
                continue;
            REP(j, N) {
                long double minT = DBL_MAX;
                REP(h, N) if (mem[h] != DBL_MAX && CD[h][j] <= E[h]) {
                    long double lastT = mem[h];
                    long double nextT = lastT+(long double)CD[h][j]/(long double)S[h];
                    minT = min(minT, nextT);
                }
                if (minT < mem[j]) {
                    mem[j] = minT;
                    pair<long double, int> nst{-minT, j};
                    Q.push(nst);
                }
            }
        }
        assert((int)ans.size() == q+1);
    }
    return ans;
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int N, Q;
        cin >> N >> Q;
        vector<int> E(N), S(N);
        REP(i, N) cin >> E[i] >> S[i];
        vector<vector<int> > D(N, vector<int>(N));
        REP(i, N) REP(j, N) cin >> D[i][j];
        vector<int> U(Q), V(Q);
        REP(i, Q) {
            cin >> U[i] >> V[i];
            --U[i];
            --V[i];
        }
        vector<long double> ans = solve(N, Q, E, S, D, U, V);
        assert((int)ans.size() == Q);
        printf("Case #%d:", _t+1);
        REP(i, Q)
            printf(" %.9Lf",  ans[i]);
        printf("\n");
        //cout << "Case #" << _t+1 << ": " << solve(N, Q, E, S, D, U, V) << endl;
    }

    return 0;
}
