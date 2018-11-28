#include <iostream>
#include <vector>
#include <cstdint>
#include <string>
#include <algorithm>
#include <functional>


struct problem {
    std::vector<std::uint8_t> signs;
    int paddle;
};


std::vector<problem> read_problems() {
    int n;
    std::cin >> n;

    std::vector<problem> results;

    for (int i = 0; i < n; i++) {
        std::string s;
        int paddle;
        std::cin >> s >> paddle;

        std::vector<std::uint8_t> x(s.size());

        for (int i = 0; i < s.size(); i++) {
            x[i] = s[i] == '+';
        }

        results.push_back({ std::move(x), paddle });
    }

    return results;
}

void flip(std::vector<std::uint8_t>& p, int paddle, int loc) {
    for (int i = loc; i < loc + paddle; i++) {
        p[i] = 1 - p[i];
    }
}

int solve(problem p) {
    auto signs = p.signs;
    int result = 0;

    for (int i = 0; i < signs.size() - p.paddle + 1; i++) {
        if (!signs[i]) {
            result += 1;
            flip(signs, p.paddle, i);
        }
    }

    for (int i = signs.size() - p.paddle; i < signs.size(); i++) {
        if (!signs[i]) {
            return -1;
        }
    }

    return result;
}


int main(int argc, char* argv[]) {
    auto problems = read_problems();

    int n = 1;

    for (auto p : problems) {
        auto result = solve(p);

        std::cout << "Case #" << n << ": ";

        if (result != -1) {
            std::cout << result;
        }
        else {
            std::cout << "IMPOSSIBLE";
        }

        std::cout << std::endl;

        n += 1;
    }
    return 0;
}