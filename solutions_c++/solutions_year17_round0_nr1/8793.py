#include <iostream>
#include <string>
#include <vector>

struct TestCase {
    unsigned ctr;
    std::string S;
    unsigned K;
};

std::istream& operator>>(std::istream &is, TestCase &test) {
    return is >> test.S >> test.K;
}

struct TestResult {
    unsigned ctr;
    bool possible;
    unsigned flips;
};

std::ostream& operator<<(std::ostream &os, TestResult &result) {
    os << "Case #" << result.ctr << ": ";
    if (result.possible) { os << result.flips; }
    else { os << "IMPOSSIBLE"; }

    return os;
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

void flip(std::string &s, unsigned ndx, unsigned k) {
    for (auto i=ndx; i < ndx+k; ++i) {
        s[i] = (s[i] == '+') ? '-' : '+';
    }
}

TestResult solve_test(TestCase &test) {
    TestResult result;
    result.ctr = test.ctr;
    result.possible = true;
    result.flips = 0;

    auto &S = test.S;
    auto &K = test.K;

    for (auto i=0; i <= S.size() - K; ++i) {
        if (S[i] == '-') {
            ++result.flips;
            flip(S, i, K);
        }
    }

    for (auto i = S.size() - K + 1; i < S.size(); ++i) {
        if (S[i] == '-') {
            result.possible = false;
            break;
        }
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
