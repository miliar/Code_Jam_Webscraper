#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

const int MN = 10;
const int KOEF = 5;
bool dp[(1 << MN) + 10][KOEF * MN + 10] = { 0 };

int doFlip(int mask, int pos, int k) {
    int new_mask = mask;
    for (int i = pos; i < pos + k; ++i) {
        new_mask ^= (1 << i);
    }
    return new_mask;
}

void doSolve(int mask, int cnt, int n, int k) {
    if (cnt >= KOEF * MN || dp[mask][cnt]) {
        return;
    }
    dp[mask][cnt] = 1;
    for (int pos = 0; pos + k - 1 < n; ++pos) {
        auto new_mask = doFlip(mask, pos, k);
        doSolve(new_mask, cnt + 1, n, k);
    }
}

int greedySolve(const std::string& str, int k) {
    std::string s = str;
    int step = 0;
    for (int i = 0; i + k <= s.size(); ++i) {
        if (s[i] == '-') {
            ++step;
            for (int j = i; j < i + k; ++j) {
                s[j] = (s[j] == '+' ? '-' : '+');
            }
        }
    }
    if (std::all_of(s.begin(), s.end(), [](char c) { return c == '+'; })) {
        return step;
    } else {
        return -1;
    }
}

int slowSolve(const std::string& str, int k) {
    if (str.size() > 10) {
        return greedySolve(str, k);
    }
    std::fill(&dp[0][0], &dp[(1 << MN) + 10][KOEF * MN + 10], 0);
    int mask = 0;
    int n = str.size();
    for (auto i = 0; i < n; ++i) {
        if (str[i] == '+') {
            mask |= (1 << (n - i - 1));
        }
    }
    doSolve(mask, 0, n, k);
    for (int i = 0; i <= KOEF * n; ++i) {
        if (dp[(1 << n) - 1][i]) {
            return i;
        }
    }
    return -1;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    std::cin >> tests;
    for (int test = 1; test <= tests; test++) {
        std::string str;
        int k;
        std::cin >> str >> k;
        int ans = slowSolve(str, k);
        assert(ans == greedySolve(str, k));
        if (ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", test);
        } else {
            printf("Case #%d: %d\n", test, ans);
        }
    }
    return 0;
}