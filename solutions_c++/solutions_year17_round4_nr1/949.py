#include <cassert>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <numeric>
#include <sstream>
#include <utility>
#include <cmath>

#include <algorithm>
#include <bitset>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#include <memory.h>
using namespace std;

#define Pi 3.141592653589793
#define all(c) (c).begin(), (c).end()
typedef long long ll;

template <typename T>
int numbits(T n) {
    return n ? 1 + numbits(n & (n - 1)) : 0;
}

class timer {
public:
    timer() : t_(clock()) {}
    void restart() { t_ = clock(); }
    float elapsed() { return float(clock() - t_) / CLOCKS_PER_SEC; }
private:
    clock_t t_;
};

void run();

int main() {
    // freopen("in.txt", "r", stdin);

#ifdef LOCAL_HOST
    freopen("out.txt", "w", stdout);
    timer t;
#endif
    run();
#ifdef LOCAL_HOST
    // printf("\nElapsed time: %.9f\n", t.elapsed());
#endif
    return 0;
}

int dp[4][101][101][101];
int cnts[4];

int calc(int left, int one, int two, int thr, int p) {
    if (one + two + thr == 0) {
        return 0;
    }
    int& res = dp[left][one][two][thr];
    if (res != -1) {
        return res;
    }
    int subres = 0;
    res = (left == 0) ? 1 : 0;
    if (one) {
        if (left >= 1) {
            subres = max(subres, calc(left - 1, one - 1, two, thr, p));
        } else {
            subres = max(subres, calc(left + p - 1, one - 1, two, thr, p));
        }
    }
    if (two) {
        if (left >= 2) {
            subres = max(subres, calc(left - 2, one, two - 1, thr, p));
        } else {
            subres = max(subres, calc(left + p - 2, one, two - 1, thr, p));
        }
    }
    if (thr) {
        if (left >= 3) {
            subres = max(subres, calc(left - 3, one, two, thr - 1, p));
        } else {
            subres = max(subres, calc(left + p - 3, one, two, thr - 1, p));
        }
    }
    res += subres;
    return res;
}

void run() {
    int T; cin >> T;
    for (int cs = 0; cs < T; ++cs) {
        int n, p; cin >> n >> p;
        vector<int> vi(n);
        memset(dp, -1, sizeof(dp));
        memset(cnts, 0, sizeof(cnts));
        for (int i = 0; i < n; ++i) {
            cin >> vi[i];
            cnts[vi[i] % p]++;
        }
        int res = cnts[0] + calc(0, cnts[1], cnts[2], cnts[3], p);
        cout << "Case #" << cs + 1 << ": " << res << endl;
    }
}

