#include <iostream>

int solve(std::string cakes, int spat) {
    int turns = 0;
    for (int i = 0; i <= cakes.length() - spat; ++i) {
        if (cakes[i] == '-') {
            ++turns;
            for (int k = 0; k < spat; ++k) {
                cakes[i+k] = cakes[i+k] == '+' ? '-' : '+';
            }
        }
    }
    for (int i = cakes.length() - spat + 1; i < cakes.length(); ++i) {
        if (cakes[i] != '+') return -1;
    }
    return turns;
}

int main() {
    int testcases;
    std::cin >> testcases;
    for (int i = 0; i < testcases; ++i) {
        std::string cakes;
        std::cin >> cakes;
        int spat;
        std::cin >> spat;
        // std::cout << "test case " << (i + 1) << " '" << cakes << "' " << spat << std::endl;
        int solution = solve(cakes, spat);
        std::cout << "Case #" << (i + 1) << ": ";
        if (solution < 0) {
            std::cout << "IMPOSSIBLE";
        } else {
            std::cout << solution;
        }
        std::cout << std::endl;
    }
}
