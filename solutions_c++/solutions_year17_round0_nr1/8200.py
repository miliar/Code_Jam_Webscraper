#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

void flip(std::vector<bool>& p, int pos, int k) {
    if (pos + k > p.size()) {
        // Can't flip anything, bail out.
        return;
    }

    for (size_t i = 0; i < k; ++i) {
        p[pos + i] = !p[pos + i];
    }
}

std::string solve(std::string const& pancakes, int k) {
    std::vector<bool> p;
    for (auto& x : pancakes) {
        p.push_back(x == '+');
    }

    int moves = 0;
    const auto sz = p.size();
    for (size_t i = 0; i < sz; ++i) {
        if (!p[i]) {
            ++moves;
            flip(p, i, k);
        }
    }

    bool good = true;
    for (auto x : p) {
        if (!x) {
            good = false;
            break;
        }
    }

    if (good) {
        return std::to_string(moves);
    } else {
        return "IMPOSSIBLE";
    }
}

int main() {
    int t = 0;
    std::cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        std::string pancakes;
        int k = 0;
        std::cin >> pancakes >> k;
        std::cout << "Case #" << tc << ": " << solve(pancakes, k) << std::endl;
    }

    return 0;
}
