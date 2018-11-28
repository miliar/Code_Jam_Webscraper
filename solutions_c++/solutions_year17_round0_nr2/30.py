#include <string>
#include <iostream>
#include <cassert>
using namespace std;
using i64 = int64_t;


i64 solveBrute(i64 N) {
    i64 answer = 1;
    for (i64 i = 2; i <= N; ++i) {
        i64 x = i;

        bool ok = true;
        int lastD = 10;
        while (x > 0) {
            int d = x % 10;
            x /= 10;
            if (d > lastD) {
                ok = false;
                break;
            }
            lastD = d;
        }

        if (ok) {
            answer = i;
        }
    }
    return answer;
}

i64 solve(i64 N) {
    i64 prefix = 0;
    while (true) {
        i64 bestLeast = -1;
        i64 bestPrefix = -1;
        for (int d = 1; d < 10; ++d) if (double(prefix) * 10 < N * 2 && prefix * 10 + d <= N) {
            i64 least = prefix;
            while (double(least) * 10 < N * 2 && least * 10 + d <= N) {
                least = least * 10 + d;
            }
            if (least > bestLeast) {
                bestLeast = least;
                bestPrefix = prefix * 10 + d;
            }
        }
        if (bestLeast == -1) {
            break;
        }
        prefix = bestPrefix;
    }
    return prefix;
}

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    ios::sync_with_stdio(0);

    int T;
    cin >> T;
    for (int __ = 1; __ <= T; ++__) {
        i64 N;
        cin >> N;
        if (N <= 1000000) {
            assert(solve(N) == solveBrute(N));
        }
        cout << "Case #" << __ << ": " << solve(N) << "\n";
    }

    return 0;
}
