#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

std::vector<bool> used;

std::pair<int, int> slowFindLR(const int pos) {
    int left = 0;
    int right = 0;
    for (int i = pos - 1; pos > 0; --i) {
        if (!used[i]) {
            ++left;
        } else {
            break;
        }
    }
    for (int i = pos + 1; pos < used.size(); ++i) {
        if (!used[i]) {
            ++right;
        } else {
            break;
        }
    }
    return std::make_pair(left, right);
}

std::pair<int ,int> slowSolve(int n, int k) {
    used.clear();
    used.resize(n + 2, false);
    used.front() = used.back() = true;
    std::pair<int, int> ans = std::make_pair(-1, -1);
    for (int i = 0; i < k; ++i) {
        int left = -1;
        int right = -1;
        int bestPos = -1;
        for (int j = 0; j < used.size(); ++j) {
            if (!used[j]) {
                const auto lr = slowFindLR(j);
                if (
                    std::min(lr.first, lr.second) > std::min(left, right) ||
                    (
                        std::min(lr.first, lr.second) == std::min(left, right) &&
                        std::max(lr.first, lr.second) > std::max(left, right)
                    )
                ) {
                    left = lr.first;
                    right = lr.second;
                    bestPos = j;
                }
            }
        }
        used.at(bestPos) = true;
        ans = std::make_pair(left, right);
    }
    if (ans.first < ans.second) {
        std::swap(ans.first, ans.second);
    }
    return ans;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    std::cin >> tests;
    for (int test = 1; test <= tests; test++) {
        int n, k;
        std::cin >> n >> k;
        const auto lr = slowSolve(n, k);
        printf("Case #%d: %d %d\n", test, lr.first, lr.second);
    }
    return 0;
}