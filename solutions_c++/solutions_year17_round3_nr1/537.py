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

struct Cake {
    int R, H;
};

bool compare(Cake a, Cake b) {
    return a.R < b.R;
}

int N, K;
int cnt;
double m[1002];
Cake C[1001];

void add(double a) {
    int i = ++cnt;
    while (i > 0 && m[i - 1] < a) {
        m[i] = m[i - 1];
        i--;
    }
    m[i] = a;
    if (cnt >= K - 1) cnt = K - 2;
}

void solve() {
    N = in();
    K = in();
    cnt = -1;
    for (int i = 0; i < N; i++) {
        C[i].R = in();
        C[i].H = in();
    }
    sort(C, C + N, compare);

    for (int i = 0; i < K - 1; i++) {
        add(2 * M_PI * C[i].R * C[i].H);
    }
    double maxA = 0;
    for (int i = K - 1; i < N; i++) {
        double area = M_PI * C[i].R * C[i].R + 2 * M_PI * C[i].R * C[i].H;
        for (int j = 0; j < K - 1; j++) {
            area += m[j];
        }
        chmax(maxA, area);
        add(2 * M_PI * C[i].R * C[i].H);
    }
    printf(" %.7lf\n", maxA);
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
