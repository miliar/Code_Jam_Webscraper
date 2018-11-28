#include <cstdint>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int64_t solve(int64_t N)
{
    auto s = std::to_string(N);
    auto v = std::vector<char>{std::begin(s), std::end(s)};
    auto i = 1;
    for (; i < v.size(); ++i) {
        if (v[i - 1] > v[i]) {
            break;
        }
    }
    if (i < v.size()) {
        auto c = v[i - 1];
        for (auto j = i - 1; j > 0 && v[j] == c && v[j - 1] == c; --j) {
            v[j] = '0';
        }
        for (auto j = i; j < v.size(); ++j) {
            v[j] = '0';
        }
        std::stringstream str{};
        str << std::string{v.begin(), v.end()};
        auto K = 0LL;
        str >> K;
        return K - 1;
    }
    return N;
}

int main()
{
    auto T = 0;
    std::cin >> T;
    for (auto i = 0; i < T; ++i) {
        auto N = 0LL;
        std::cin >> N;
        auto result = solve(N);
        printf("Case #%d: %lld\n", i + 1, result);
    }
    return 0;
}
