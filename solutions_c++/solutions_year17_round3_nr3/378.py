#include <cmath>
#include <iostream>
#include <vector>

typedef long double ld;
typedef unsigned long long ull;
typedef long long ll;

int main() {
    ull T;
    std::cin >> T;
    std::cout.precision(9);

    for (ull t = 1; t <= T; ++t) {
        ull N, K;
        std::cin >> N >> K;
        ld U;
        std::cin >> U;
        std::vector<ld> P(N);
        for (auto&& Pi : P) {
            std::cin >> Pi;
        }
        while (true) {
            ld min_val = *std::min_element(P.begin(), P.end());
            if (min_val == 1) {
                break;
            }
            ll min_count = std::count(P.begin(), P.end(), min_val);
            ld next = 1;
            for (auto&& Pi : P) {
                if (Pi != min_val) {
                    next = std::min(next, Pi);
                }
            }
            ld required = (next - min_val) * min_count;
            if (required > U) {
                for (auto&& Pi : P) {
                    if (Pi == min_val) {
                        Pi += U / min_count;
                    }
                }
                break;
            } else {
                for (auto&& Pi : P) {
                    if (Pi == min_val) {
                        Pi = next;
                    }
                }
                U -= required;
            }
        }
        ld result = 1;
        for (auto&& Pi : P) {
            result *= Pi;
        }
        std::cout << "Case #" << t << ": " << std::fixed << result << std::endl;
    }
    return 0;
}