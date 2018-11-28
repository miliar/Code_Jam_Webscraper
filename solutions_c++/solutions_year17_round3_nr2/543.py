#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <array>
#include <list>
#include <stack>
#include <valarray>
#include <fstream>

using namespace std;

typedef unsigned uint;
typedef long long Int;
typedef unsigned long long UInt;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }
double fin() { double x; scanf("%lf", &x); return x; }
Int lin() { Int x; scanf("%lld", &x); return x; }

struct Interval {
    int S, E;
};

bool compare(Interval a, Interval b) {
    return a.S < b.S;
}

int NC, NJ;
int NA, A[10000];
Interval C[101];
Interval J[101];
int D[1441][730][2];

void solve() {
    NC = in();
    NJ = in();
    for (int i = 0; i < NC; i++) {
        C[i].S = in();
        C[i].E = in();
    }
    for (int i = 0; i < NJ; i++) {
        J[i].S = in();
        J[i].E = in();
    }
    for (int i = 0; i <= 1440; i++) {
        for (int j = 0; j <= 720; j++)
            D[i][j][0] = D[i][j][1] = INF;
    }
    D[0][0][0] = 0;
    for (int i = 1; i <= 1440; i++) {
        for (int j = 0; j <= i && j <= 720; j++) {
            int k;
            if (j > 0) {
                for (k = 0; k < NC; k++) {
                    if (C[k].S < i && C[k].E >= i)
                        break;
                }
                if (k == NC) {
                    D[i][j][0] = min(D[i - 1][j - 1][0], D[i - 1][j - 1][1] + 1);
                }
            }
            for (k = 0; k < NJ; k++) {
                if (J[k].S < i && J[k].E >= i)
                    break;
            }

            if (k == NJ) {
                D[i][j][1] = min(D[i - 1][j][0] + 1, D[i - 1][j][1]);
            }
        }
    }
    int sol = min(D[1440][720][0], D[1440][720][1] + 1);
    for (int i = 0; i <= 1440; i++) {
        for (int j = 0; j <= 720; j++)
            D[i][j][0] = D[i][j][1] = INF;
    }
    D[0][0][1] = 0;
    for (int i = 1; i <= 1440; i++) {
        for (int j = 0; j <= i && j <= 720; j++) {
            int k;
            if (j > 0) {
                for (k = 0; k < NC; k++) {
                    if (C[k].S < i && C[k].E >= i)
                        break;
                }
                if (k == NC) {
                    D[i][j][0] = min(D[i - 1][j - 1][0], D[i - 1][j - 1][1] + 1);
                }
            }
            for (k = 0; k < NJ; k++) {
                if (J[k].S < i && J[k].E >= i)
                    break;
            }

            if (k == NJ) {
                D[i][j][1] = min(D[i - 1][j][0] + 1, D[i - 1][j][1]);
            }
        }
    }
    chmin(sol, min(D[1440][720][0] + 1, D[1440][720][1]));
    cout << ' ' << sol << endl;
//    sort(C, C + NC, compare);
//    sort(J, J + NJ, compare);
//    int sumC = 0;
//    for (int i = 0; i < NJ; i++) {
//        sumC += J[i].E - J[i].S;
//    }
//    int canCombine;
//    for (int i = 0; i < NJ - 1; i++) {
//        canCombine = 1;
//        for (int j = 0; j < NC; j++) {
//            if (J[i].E < C[j].S && C[j].S < J[i + 1].S) {
//                canCombine = 0;
//                break;
//            }
//        }
//        if (canCombine) {
//            A[NA++] = J[i + 1].S - J[i].E;
//        }
//    }
//    if (NJ > 1) {
//        canCombine = 1;
//        for (int j = 0; j < NC; j++) {
//            if (J[NJ - 1].E < C[j].S || J[0].S > C[j].S) {
//                canCombine = 0;
//                break;
//            }
//        }
//        if (canCombine) {
//            A[NA++] = 1440 - J[NJ - 1].E + J[0].S;
//        }
//    }
//    sort(A, A + NA);
//
//    int i;
//    for (i = 0; i < NA && sumC + A[i] <= 720; i++) {
//        sumC += A[i];
//    }
//    cout << ' ' << (NJ - i) * 2  << endl;
}

int main() {

#ifdef LOCAL_ENV
    freopen("sol.in", "r", stdin);
    freopen("sol.out", "w", stdout);
#endif

    int nc = in();
    for (int tc = 1; tc <= nc; tc++) {
        cout << "Case #" << tc << ":";
        solve();
    }
    return 0;
}
