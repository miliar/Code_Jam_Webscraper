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
const int MAX = 33;
#else
const int MAX = (const int) (1e5 + 11);
#endif

int N;
char A[MAX];

static bool ok() {
    for (int i = 0; i < N - 1; ++i)
        if (A[i] > A[i + 1])
            return false;
    return true;
}

static bool ok(int x) {
    auto S = to_string(x);
    for (int i = 1; i < S.length(); ++i)
        if (S[i - 1] > S[i])
            return false;
    return true;
}

static int brute() {
    auto x = atoi(A);
    for (int i = x; i >= 1; ++i)
        if (ok(i))
            return i;
    return 0;
}

static void solve(std::int32_t test) {
    memset(A, 0, sizeof(A));

    cin >> A;
    N = (int) strlen(A);
    reverse(A, A + N);
    for (int i = 0; i < N - 1; ++i) {
        if (A[i] == '0') {
            int j = i;
            while (j < N && A[j] == '0') {
                A[j] = '9';
                j++;
            }
            if (j < N)
                A[j]--;
            i = j - 1;
            continue;
        }
        if (A[i + 1] == '0') {
            A[i] = '0';
            i--;
            continue;
        }
        if (A[i] < A[i + 1]) {
            for (int j = i; j >= 0; j--)
                A[j] = '9';
            A[i + 1]--;
        }
    }
    if (A[N - 1] == '0') {
        A[N - 1] = 0;
        N--;
    }
    reverse(A, A + N);
#ifdef DK
    assert(ok());
    assert(brute() == atoi(A));
#endif
    cout << "Case #" << test + 1 << ": " << A;
}

int main() {
    ios_base::sync_with_stdio(0);
    cout << setprecision(12) << fixed;
#ifdef DK
    tool::run_task(tool::Task::B, solve, false);
#else
    solve(0);
#endif
    return 0;
}