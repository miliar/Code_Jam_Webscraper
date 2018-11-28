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

int N, K;
Int PI[1000];
Int UI;
double U;
double P[51];

void solve() {
    N = in();
    K = in();
    U = fin();
    UI = (long long)(U * 10000);
    Int sumI = 0;
    double sum = 0;
    for (int i = 0; i < N; i++) {
        P[i] = fin();
        PI[i] = (long long)(P[i] * 10000);
        sumI += PI[i];
        sum += P[i];
    }
    sort(P, P + N);
    sort(PI, PI + N);
    Int exI = 0;
    double ex = 0;
    double exP = 1;
    for (int i = N - 1; i >= 0; i--) {
        if ((sumI - exI + UI) >= PI[i] * (i + 1)) {
            printf(" %.7lf\n", pow((sum - ex + U) / (i + 1), i + 1) * exP);
            break;
        } else {
            ex += P[i];
            exI += PI[i];
            exP *= P[i];
        }
    }
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
