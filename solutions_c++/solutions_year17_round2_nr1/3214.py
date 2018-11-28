#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <fstream>
#include <iomanip>
#include <unordered_map>
#include <assert.h>

#ifdef DK

#include "Tool.hh"

#endif

using namespace std;

#ifdef DK
const int MAX = 1000;
#else
const int MAX = (const int) (2e5 + 11);
#endif

int D, N;
int A[MAX], B[MAX];

static bool f(long double v) {
    long double t = D / v;
    for (int i = 0; i < N; ++i) {
        long double ds = D - A[i];
        long double dv = B[i];
        long double dt = ds / dv;
        if (t < dt)
            return false;
    }
    return true;
}

static void solve(std::int32_t test) {
    cin >> D >> N;
    for (int i = 0; i < N; ++i)
        cin >> A[i] >> B[i];

    long double a = 0, b = 1e18, res = -1;
    while (abs(a - b) > 1e-6) {
        long double m = (a + b) / 2.0;
        if (f(m)) {
            a = m;
            res = m;
        } else {
            b = m;
        }
    }
    cout << "Case #" << test + 1 <<  ": " << res;
}

int main() {
    ios_base::sync_with_stdio(0);
    cout << setprecision(12) << fixed;
#ifdef DK
    tool::run_task(tool::Task::A, solve, false);
#else
    solve(0);
#endif
    return 0;
}