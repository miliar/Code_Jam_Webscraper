#include <iostream>
#include <cstdint>
#include <vector>
#include <algorithm>

int main() {
    int cases;
    std::cin >> cases;
    std::cerr << cases << " test cases" << std::endl;

    for (int i = 0; i < cases; i++) {
        uint64_t N, K, min, max;
        std::cin >> N >> K;
        std::vector<uint64_t> asdf = {N};
        for (int j = 0; j < K; j++) {
            auto x = std::max_element(asdf.begin(), asdf.end());
            auto n1 = *x / 2;
            auto n2 = *x / 2 - !(*x & 1);
            if (j == K - 1) {
                std::cout << "Case #" << i+1 << ": " << n1 << " " << n2 << std::endl;
                break;
            }
            *x = n1;
            asdf.insert(x, n2);
        }
    }
    return 0;
}
