#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdint>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

using int64 = int64_t;

constexpr int64 MOD = 1000000007;

typedef pair<int, int> P;

typedef pair<double, int> Q;

struct pancake {
    int r, h;
    pancake() {}
    ~pancake() {}
    pancake(int a, int b): r(a), h(b) {}

    bool operator < (const pancake& o) const { return r == o.r ? h < o.h : r < o.r; }
};

double area(double r) {
    return M_PI * r * r;
}

double circ(double r) {
    return 2 * M_PI * r;
}

int N, K;

pancake pc[1000];

double solve() {
    sort(pc, pc+N);
    double opt[1000][1000];
    fill(opt[0], opt[0]+K+1, 0);
    opt[0][1] = circ(pc[0].r) * pc[0].h;

    double ret = opt[0][1] + area(pc[0].r);
    for (int j = 1; j < N; ++j) {
        for (int k = 0; k <= K; ++k) {
            opt[j][k] = opt[j-1][k];
            if (k > 0) {
                double cand = opt[j-1][k-1] + circ(pc[j].r) * pc[j].h;
                if (cand > opt[j][k]) {
                    opt[j][k] = cand;
                }
                ret = max(ret, cand + area(pc[j].r));
            }
        }
    }

    return ret;
}

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> K;
        for (int j = 0; j < N; ++j) {
            cin >> pc[j].r >> pc[j].h;
        }
        printf("Case #%d: %.12f\n", t, solve());
    }

    return 0;
}
