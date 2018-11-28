#include <iostream>
#include <string>
#include <vector>

struct TestCase {
    unsigned ctr;
    unsigned N,K;
};

std::istream& operator>>(std::istream &is, TestCase &test) {
    return is >> test.N >> test.K;
}

struct TestResult {
    unsigned ctr;
    unsigned min, max;
};

std::ostream& operator<<(std::ostream &os, TestResult &result) {
    return os << "Case #" << result.ctr << ": " << result.max << " " << result.min;
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

unsigned calc_ls(const std::vector<int> &stalls, unsigned ndx) {
    unsigned ls = 0;

    --ndx;
    while (!stalls[ndx]) {
        ++ls;
        --ndx;
    }

    return ls;
}

unsigned calc_rs(const std::vector<int> &stalls, unsigned ndx) {
    unsigned rs = 0;

    ++ndx;
    while (!stalls[ndx]) {
        ++rs;
        ++ndx;
    }

    return rs;
}

unsigned calc_best_S(const std::vector<int> &stalls) {
    unsigned best = 0, best2 = 0, best_S = 0;

    for (auto S=0u; S < stalls.size(); ++S) {
        if (stalls[S]) { continue; }

        auto ls = calc_ls(stalls, S),
             rs = calc_rs(stalls, S);

        auto s_min = (ls < rs) ? ls : rs,
             s_max = (ls > rs) ? ls : rs;

        if (s_min > best || (s_min == best && s_max > best2)) {
            best = s_min;
            best2 = s_max;
            best_S = S;
        }
    }

    return best_S;
}

TestResult solve_test(TestCase &test) {
    std::vector<int> stalls(test.N + 2, 0);
    stalls.front() = stalls.back() = 1;

    for (auto k=0; k < test.K-1; ++k) {
        auto best_S = calc_best_S(stalls);
        stalls[best_S] = 1;
    }
    
    unsigned best = 0, best2 = 0;
    for (auto S=0u; S < stalls.size(); ++S) {
        if (stalls[S]) { continue; }

        auto ls = calc_ls(stalls, S),
             rs = calc_rs(stalls, S);

        auto s_min = (ls < rs) ? ls : rs,
             s_max = (ls > rs) ? ls : rs;

        if (s_min > best || (s_min == best && s_max > best2)) {
            best = s_min;
            best2 = s_max;
        }
    }

    TestResult result;
    result.ctr = test.ctr;
    result.min = best;
    result.max = best2;
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
