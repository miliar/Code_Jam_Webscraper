#include <algorithm>
#include <iostream>
#include <deque>
#include <string>

bool bxor(const bool a, const bool b) {
    return a ? !b : b;
}

bool should_flip(const bool is_happy, const bool is_flipped) {
    return bxor(is_happy, is_flipped);
}

std::string solve(std::string pancakes, const unsigned int K) {
    auto is_prev_flipped = std::deque<bool>();
    for (auto i = 0u; i < K - 1; ++i) {
        is_prev_flipped.push_back(false);
    }

    auto is_flipped = false;

    auto flips = 0u;
    for (const auto& pancake: pancakes) {
        if (should_flip(pancake == '-', is_flipped)) {
            is_flipped = !is_flipped;
            is_prev_flipped.push_back(true);
            ++flips;
        } else {
            is_prev_flipped.push_back(false);
        }
        is_flipped = bxor(is_flipped, is_prev_flipped.front());
        is_prev_flipped.pop_front();
    }

    if (std::any_of(
            is_prev_flipped.cbegin(),
            is_prev_flipped.cend(),
            [](bool b){return b;}
       )) {
        return "IMPOSSIBLE";
    }
    return std::to_string(flips);
}

int main() {
    unsigned int T;
    std::cin >> T;

    for (auto i = 1u; i <= T; ++i) {
        unsigned int K;
        std::string s;
        std::cin >> s >> K;
        std::cout << "Case #" << i << ": " << solve(s, K) << std::endl;
    }
}
