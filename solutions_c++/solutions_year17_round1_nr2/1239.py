#include <iostream>
#include <vector>
#include <cmath>

typedef unsigned long long ull;
typedef long long ll;

bool intersect(const std::pair<ull, ull>& pair_1, const std::pair<ull, ull>& pair_2) {
    return pair_1.first <= pair_1.second && pair_2.first <= pair_2.second
           && std::max(pair_1.first, pair_2.first) <= std::min(pair_1.second, pair_2.second);
}

void permute(std::vector<std::vector<std::pair<ull, ull>>>& pairs, ull start, std::vector<ull>& results) {
    if (start + 1 == pairs[1].size()) {
        results.push_back(0);
        for (ull i = 0; i < pairs[0].size(); ++i) {
            if (intersect(pairs[0][i], pairs[1][i])) {
                ++results.back();
            }
        }
    } else {
        permute(pairs, start + 1, results);
        for (ull i = start + 1; i < pairs[0].size(); ++i) {
            std::swap(pairs[1][start], pairs[1][i]);
            permute(pairs, start + 1, results);
            std::swap(pairs[1][start], pairs[1][i]);
        }
    }
}

ull value(std::vector<std::vector<std::pair<ull, ull>>>& pairs) {
    if (pairs.size() == 1) {
        ull result = 0;
        for (auto&& pair : pairs.front()) {
            if (pair.first <= pair.second) {
                ++result;
            }
        }
        return result;
    }

    if (pairs.size() == 2) {
        std::vector<ull> results;
        permute(pairs, 0, results);
        return *std::max_element(results.begin(), results.end());
    }

    throw std::exception();
}

int main() {
    ull t;
    std::cin >> t;
    for (ull c = 1; c <= t; ++c) {
        ull n, p;
        std::cin >> n >> p;
        std::vector<ull> r(n);
        for (auto&& ri : r) {
            std::cin >> ri;
        }
        std::vector<std::vector<std::pair<ull, ull>>> pairs(n);
        for (ull i = 0; i < n; ++i) {
            for (ull j = 0; j < p; ++j) {
                ull qij;
                std::cin >> qij;
                ull min = std::ceil(qij / 1.1 / r[i]);
                ull max = std::floor(qij / 0.9 / r[i]);
                pairs[i].push_back({min, max});
            }
        }
        std::cout << "Case #" << c << ": " << value(pairs) << std::endl;
    }
    return 0;
}