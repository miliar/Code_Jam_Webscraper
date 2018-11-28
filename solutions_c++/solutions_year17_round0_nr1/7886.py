#include <algorithm>
#include <bitset>
#include <iostream>
#include <stdexcept>
#include <string>

#define NLEN 1000
#define ONE '+'
#define ZERO '-'

template <typename T>
void switch_place(T& chain, size_t index) {
    if (chain[index] == ONE) {
        chain[index] = ZERO;
    } else {
        chain[index] = ONE;
    }
}

size_t work(std::string chain, size_t k) {
    auto pluses = std::count(chain.cbegin(), chain.cend(), '+');

    if ((unsigned)pluses == chain.length()) {
        return 0;
    }

    if (chain.length() < k) {
        throw std::runtime_error("IMPOSSIBLE");
    }
    size_t changes = 0;

    for (size_t pos = 0; pos < chain.length() - k + 1; ++pos) {
        if (chain[pos] == ZERO) {
            ++changes;
            for (size_t pos2 = 0; pos2 < k; ++pos2) {
                switch_place(chain, pos + pos2);
            }
            //std::cout << chain << std::endl;
        }
    }

    pluses = std::count(chain.cbegin(), chain.cend(), '+');
    if ((unsigned)pluses != chain.length()) {
        throw std::runtime_error("IMPOSSIBLE");
    }
    return changes;
}

int main() {
    size_t cases = 0;
    std::cin >> cases;

    for (size_t i = 1; i < cases + 1; ++i) {
        std::string chain;
        size_t      k;
        std::cin >> chain >> k;

        std::cout << "Case #" << i << ": ";

        try {
            auto ans = work(chain, k);
            std::cout << ans << '\n';
        } catch (std::runtime_error& err) {
            std::cout << "IMPOSSIBLE" << '\n';
        }
    }
}

