#include "bits/stdc++.h"

double solve(uint64_t D, uint64_t N, std::vector<double> K, std::vector<double> S) {
    double max = 0;
    for (uint64_t i = 0; i < N; ++i) {
        max = std::max(max, (D - K[i]) / S[i]);
    }
    return D / max;
}

int main() {
    uint64_t T = 0;
    std::cin >> T;
    for (uint64_t x = 1; x <= T; ++x) {
        uint64_t D = 0, N = 0;
        std::cin >> D >> N;
        std::vector<double> K(N), S(N);
        for (uint64_t i = 0; i < N; ++i) {
            std::cin >> K[i] >> S[i];
        }
        std::cout << "Case #" << x << ": " << std::fixed << std::setprecision(6) << solve(D, N, K, S) << std::endl;
    }
    return 0;
}
