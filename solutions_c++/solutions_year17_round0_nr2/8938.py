#include <iostream>
#include <string>
#include <vector>

#include <cstdint>

struct TestCase {
    unsigned ctr;
    uint64_t N;
};

std::istream& operator>>(std::istream &is, TestCase &test) {
    return is >> test.N;
}

struct TestResult {
    unsigned ctr;
    uint64_t answer;
};

std::ostream& operator<<(std::ostream &os, TestResult &result) {
    return os << "Case #" << result.ctr << ": " << result.answer;
}

std::vector<TestCase> read_tests() {
    unsigned T;
    std::cin >> T;

    std::vector<TestCase> tests;
    for (auto i=0u; i < T; ++i) {
        tests.emplace_back();
        tests.back().ctr = tests.size();
        std::cin >> tests.back();
    }

    return tests;
}

bool is_tidy(uint64_t n) {
    auto digit = n % 10;
    n /= 10;

    while (n) {
        auto next_digit = n % 10;
        if (next_digit > digit) { return false; }

        digit = next_digit;
        n /= 10;
    }

    return true;
}

TestResult solve_test(TestCase &test) {
    TestResult result;
    result.ctr = test.ctr;

    result.answer = test.N;
    while (!is_tidy(result.answer)) {
        --result.answer;
    }

    return result;
}

int main() {
    auto tests = read_tests();

    for (auto &test : tests) {
        auto result = solve_test(test);
        std::cout << result << std::endl;
    }

    return 0;
}
