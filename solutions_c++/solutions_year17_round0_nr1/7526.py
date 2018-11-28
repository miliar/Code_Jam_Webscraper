#include "bits/stdc++.h"

void solve(std::string S, const uint64_t &K) {
    uint64_t c = 0;
    for (uint64_t i = 0; i < S.size(); ++i) {
        if (S[i] == '-') {
            if (i > S.size() - K) {
                std::cout << "IMPOSSIBLE"; return;
            }
            for (uint64_t j = i; j < i + K; ++j)
                S[j] = (S[j] == '-') ? '+' : '-';
            ++c;
        }
    }
    std::cout << c; return;
}

int main() {
    uint64_t T = 0;
    std::cin >> T;
    for (uint64_t x = 1; x <= T; ++x) {
        std::string S; uint64_t K = 0;
        std::cin >> S >> K;
        std::cout << "Case #" << x << ": "; solve(S, K); std::cout << std::endl;
    }
    return 0;
}
