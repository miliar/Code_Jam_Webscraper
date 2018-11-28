#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>

std::vector<std::int64_t> read_problem() {
    std::int64_t count;
    std::cin >> count;

    std::vector<std::int64_t> result(count);

    for (std::int64_t i = 0; i < count; i++) {
        std::cin >> result[i];
    }

    return result;
}

std::int64_t smallest_tidy(std::int64_t digits) {
    std::int64_t result = 0;

    for (std::int64_t i = 0; i < digits; i++) {
        result *= 10;
        result += 1;
    }

    return result;
}

std::vector<int> digits(std::int64_t v) {
    std::vector<int> result;

    while (v != 0) {
        result.push_back(v % 10);
        v /= 10;
    }

    return result;
}

std::int64_t solve_problem(std::int64_t v) {
    auto d = digits(v);

    std::vector<int> sol_d(d.size());

    int curr = 0;
    int last = -1;
    bool has_down = false;

    for (int i = d.size() - 1; i >= 0; i--) {
        auto x = d[i];

        if (x > curr) {
            sol_d[i] = x;
            curr = x;
            last = i;
        }
        else if (x == curr) {
            sol_d[i] = x;
        }
        else if (x < curr) {
            has_down = true;
            break;
        }
    }

    if (has_down) {
        sol_d[last] -= 1;

        for (int i = last - 1; i >= 0; i--) {
            sol_d[i] = 9;
        }
    }

    std::int64_t m = 1;
    std::int64_t r = 0;

    for (auto x : sol_d) {
        r += m * x;
        m *= 10;
    }

    return r;
}

int main(int argc, char* argv[]) {
    auto problem = read_problem();

    std::vector<std::int64_t> result(problem.size());
    std::transform(problem.begin(), problem.end(), result.begin(), solve_problem);

    std::int64_t case_num = 1;

    for (auto x : result) {
        std::cout << "Case #" << case_num << ": " << x << std::endl;
        case_num += 1;
    }

    return 0;
}