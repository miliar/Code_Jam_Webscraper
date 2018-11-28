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
const int MAX = 13;
#else
const int MAX = (const int) (1e3 + 11);
#endif

int N, K;
char A[MAX];

static void solve(std::int32_t test) {
    cin >> A >> K;
    N = (int) strlen(A);
    int res = 0;
    for (int i = 0; i <= N - K; ++i) {
        if (A[i] == '+')
            continue;
        for (int j = i; j < i + K; ++j) {
            if (A[j] == '-')
                A[j] = '+';
            else
                A[j] = '-';
        }
        res++;
    }
    bool ok = true;
    for (int i = 0; i < N; ++i) {
        if (A[i] == '-') {
            ok = false;
            break;
        }
    }
    cout << "Case #" << test + 1 << ": ";
    if (ok) {
        cout << res;
    } else {
        cout << "IMPOSSIBLE";
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cout << setprecision(12) << fixed;
#ifdef DK
    tool::run_task(tool::Task::A, solve);
#else
    solve(0);
#endif
    return 0;
}