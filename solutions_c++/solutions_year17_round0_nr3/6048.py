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
#include <assert.h>

#ifdef DK

#include "Tool.hh"

#endif

using namespace std;

#ifdef DK
//const int MAX = 11;
const int MAX = (const int) (1e3 + 11);
#else
const int MAX = (const int) (1e3 + 11);
#endif


static pair<int64_t, int64_t> solve1(std::int32_t test, int64_t N, int64_t K) {
    static int A[MAX], L[MAX], R[MAX];
    memset(A, 0x00, sizeof(A));
    memset(L, 0x00, sizeof(L));
    memset(R, 0x00, sizeof(R));

    N += 2;
    A[0] = 1;
    A[N - 1] = 1;
    int res = -1;
    for (int k = 0; k < K; ++k) {
        memset(L, 0x00, sizeof(L));
        memset(R, 0x00, sizeof(R));

        for (int i = 0; i < N; ++i)
            if (A[i] == 1)
                L[i] = -1;
            else
                L[i] = L[i - 1] + 1;
        for (int i = N - 1; i >= 0; --i)
            if (A[i] == 1)
                R[i] = -1;
            else
                R[i] = R[i + 1] + 1;
        int idx1 = -1, mx1 = -N, c1 = 0;
        for (int i = 1; i < N - 1; ++i) {
            if (A[i])
                continue;
            int t1 = min(L[i], R[i]);
            if (mx1 < t1) {
                mx1 = t1;
                c1 = 1;
                idx1 = i;
                continue;
            }
            if (mx1 == t1)
                c1++;
        }
        if (c1 != 1) {
            int mx2 = -N, idx2 = -1;
            for (int i = 1; i < N - 1; ++i) {
                if (A[i])
                    continue;
                int t1 = min(L[i], R[i]);
                int t2 = max(L[i], R[i]);
                if (t1 == mx1 && mx2 < t2) {
                    mx2 = t2;
                    idx2 = i;
                }
            }
            res = idx2;
        } else {
            res = idx1;
        }
        assert(res != -1);
        assert(c1 != 0);
        assert(A[res] == 0);
        A[res] = 1;
    }
    assert(res != -1);
    int mx = max(L[res], R[res]);
    int mn = min(L[res], R[res]);
    return {mx, mn};
}

static pair<int64_t, int64_t> f(int64_t a, int64_t b, int64_t k) {
    if (a > b)
        return {1e18, -1e18};
    int64_t len = b - a + 1;
    if (k == 1) {
        if (len & 1)
            return {len / 2, len / 2};
        return {len / 2, len / 2 - 1};
    }
    int64_t m = (a + b) / 2;
    if ((len & 1) && (k & 1))
        return f(a, m - 1, k / 2);
    if (!(len & 1) && (k & 1))
        return f(a, m - 1, k / 2);
    if ((len & 1) && !(k & 1))
        return f(a, m - 1, k / 2);
    if (!(len & 1) && !(k & 1)) {
        auto t1 = f(m + 1, b, k / 2);
        auto t2 = f(a, m - 1, k / 2);
        if (t1.second < t2.second)
            return t1;
        if (t1.second == t2.second)
            if (t1.first < t2.first)
                return t2;
        return t1;
    }
    assert(false);
    return {};
}

static pair<int64_t, int64_t> solve2(std::int32_t test, int64_t N, int64_t K) {
    return f(0, N - 1, K);
}

static void solve(std::int32_t test) {
    int64_t N, K;
    cin >> N >> K;
//    auto r1 = solve1(test, N, K);
    auto r2 = solve2(test, N, K);
#ifdef DK
//    assert(r1 == r2);
#endif
    cout << "Case #" << test + 1 << ": " << r2.first << " " << r2.second;
}

int main() {
    ios_base::sync_with_stdio(0);
    cout << setprecision(12) << fixed;
#ifdef DK
    tool::run_task(tool::Task::C, solve, false);
#else
    solve(0);
#endif
    return 0;
}