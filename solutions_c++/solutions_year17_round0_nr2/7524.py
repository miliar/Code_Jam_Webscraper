#include "bits/stdc++.h"

uint64_t solve(uint64_t N) {
    uint64_t d0 = 9, d1 = 9;
    for (uint64_t  i = 1, x = N; x > 0; i *= 10, x /= 10)
    {
        d0 = d1; d1 = x % 10;
        if (d1 > d0) {
            return solve(x * i - 1);
        }
    }
    return N;
}

int main() {
    uint64_t T = 0;
    std::cin >> T;
    for (uint64_t x = 1; x <= T; ++x) {
        uint64_t N = 0;
        std::cin >> N;
        std::cout << "Case #" << x << ": " << solve(N) << std::endl;
    }
    return 0;
}
