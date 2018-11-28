#include <iostream>
#include <string>
#include <vector>

std::vector<int> toVec(std::string const& number) {
    std::vector<int> res;
    for (size_t i = 0; i < number.size(); ++i) {
        res.push_back(number[i] - '0');
    }

    return res;
}

bool isSolution(std::vector<int> const& num) {
    const auto sz = num.size();
    for (size_t i = 1; i < sz; ++i) {
        if (num[i] < num[i - 1]) {
            return false;
        }
    }

    return true;
}

std::string toString(std::vector<int> const& num) {
    std::string res;
    // Drop leading zeroes
    size_t start = 0;
    for (start = 0; start < num.size(); ++start) {
        if (num[start] != 0) { break; }
    }

    for (size_t i = start; i < num.size(); ++i) {
        res += std::to_string(num[i]);
    }

    return res;
}

std::string solve(std::string const& number) {
    auto vec = toVec(number);

    const auto sz = number.size();

    while (!isSolution(vec)) {
        for (size_t i = 0; i < sz - 1; ++i) {
            if (vec[i] > vec[i + 1]) {
                --vec[i];
                for (size_t j = i + 1; j < sz; ++j) {
                    vec[j] = 9;
                }
                break;
            }
        }
    }

    return toString(vec);
}

int main() {
    int t = 0;
    std::cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        std::string number;
        std::cin >> number;
        std::cout << "Case #" << tc << ": " << solve(number) << std::endl;
    }

    return 0;
}
