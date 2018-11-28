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

pair<int, int> getValidInt(int R, int Q) {
    int Q10 = 10*Q;
    int minR = 9*R;
    int maxR = 11*R;
    int minV = Q10%maxR == 0 ? Q10/maxR : Q10/maxR+1;
    int maxV = Q10/minR;
    //cerr << R << "," << Q << endl;
    //cerr << "minR: " << minR << "," << Q10 << "," << Q10/minR << endl;
    //cerr << "--- " << minV << "," << maxV << endl;
    pair<int, int> vn(minV, maxV);
    if (minV > maxV)
        vn.first = vn.second = -1;
    assert(vn.first <= vn.second);
    return vn;
}

bool haveSame(pair<int, int> &vn0, pair<int, int> &vn1) {
    if (vn0.first == -1 || vn1.first == -1)
        return false;
    return vn1.first <= vn0.second && vn0.first <= vn1.second;
}

int solve2(vector<int> R, vector<vector<int> > Q) {
    int N = R.size();
    int P = Q[0].size();
    if (N == 1) {
        int ret = 0;
        REP(j, P) {
            ret += (getValidInt(R[0], Q[0][j]).first != -1 ? 1 : 0);
        }
        return ret;
    }
    else {
        if (N != 2)
            return -1;

        int ret = 0;
        sort(Q[1].begin(), Q[1].end());
        do {
            int cnt = 0;
            REP(j, P) {
                pair<int, int> vn0 = getValidInt(R[0], Q[0][j]);
                pair<int, int> vn1 = getValidInt(R[1], Q[1][j]);
                if (haveSame(vn0, vn1)) {
                    ++cnt;
                }
            }
            if (cnt > ret)
                ret = cnt;
        } while(next_permutation(Q[1].begin(), Q[1].end()));
        return ret;
    }
}

int solve(vector<int> R, vector<vector<int> > Q) {
    int N = R.size();
    int P = Q[0].size();
    vector<vector<pair<int, int> > > W(N, vector<pair<int, int> >(P));
    REP(i, N) REP(j, P) {
        W[i][j] = getValidInt(R[i], Q[i][j]);
    }
    REP(i, N) {
        sort(W[i].begin(), W[i].end());
    }
    int minV = INT_MAX;
    int maxV = 0;
    REP(i, N) REP(j, P) if (W[i][j].first != -1) {
        minV=min(minV, W[i][j].first);
        maxV=max(maxV, W[i][j].second);
    }
    vector<vector<bool> > used(N, vector<bool>(P));
    REP(i, N) REP(j, P) used[i][j] = W[i][j].first == -1;
    int ret = 0;
    set<int> validV;
    REP(i, N) REP(j, P) if (W[i][j].first != -1) {
        validV.insert(W[i][j].first);
        validV.insert(W[i][j].second);
    }
    for (auto v : validV) {
        bool changed = false;
        do {
        changed = false;
        vector<int> kit;
        REP(i, N) {
            bool found = false;
            REP(j, P) if (!used[i][j] && W[i][j].first <= v && v <= W[i][j].second) {
                kit.push_back(j);
                found = true;
                break;
            }
            if (!found) {
                break;
            }
        }
        if ((int)kit.size() == N) {
            ret++;
            REP(i, N) used[i][kit[i]] = true;
            changed = true;
        }
        }while(changed);
    }
    return ret;
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int N, P;
        cin >> N >> P;
        vector<int> R(N);
        REP(i, N)
            cin >> R[i];
        vector<vector<int> > Q(N, vector<int>(P));
        REP(i, N) REP(j, P)
            cin >> Q[i][j];
        cout << "Case #" << _t+1 << ": " << solve(R, Q) << endl;
    }

    return 0;
}
