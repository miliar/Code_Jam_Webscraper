//
//  fox.cpp
//  mepcpp
//
//  Created by Zinge on 5/28/16.
//  Copyright © 2016 MEP. All rights reserved.
//

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#ifndef LOCAL_JUDGE_
const int max_n = 1010;
#else  // LOCAL_JUDGE_
const int max_n = 1010;
#endif // LOCAL_JUDGE_

void redirect_input(const std::string& path) {
    std::freopen(path.c_str(), "r", stdin);
}

void redirect_output(const std::string& path) {
    std::freopen(path.c_str(), "w", stdout);
}

struct cake_t {
    int r;
    int h;

    explicit cake_t(int r_ = 0, int h_ = 0)
        : r(r_)
        , h(h_) {}
};

cake_t c[max_n];

long long dp[max_n][max_n];

int main() {
#ifdef LOCAL_JUDGE_
    redirect_input("/Volumes/Setup/Android/projects/mep/mepcpp/mepcpp/in");
    redirect_output("/Volumes/Setup/Android/projects/mep/mepcpp/mepcpp/out");
#endif // LOCAL_JUDGE_

    int tn;
    std::cin >> tn;

    for (int ti = 1; ti <= tn; ++ti) {
        int n, k;
        std::cin >> n >> k;

        for (int i = 1; i <= n; ++i) {
            std::cin >> c[i].r >> c[i].h;
        }

        std::sort(c + 1, c + n + 1, [](const cake_t& lhs, const cake_t& rhs) {
            return lhs.r < rhs.r;
        });

        std::memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= n; ++i) {
            dp[i][1] = 2LL * c[i].h * c[i].r;
            for (int j = i + 1; j <= n; ++j) {
                for (int p = 1; p <= i && p < k; ++p) {
                    dp[j][p + 1] = std::max(dp[j][p + 1],
                                            dp[i][p] + 2LL * c[j].h * c[j].r);
                }
            }
        }

        long long best_v = 0;
        for (int i = k; i <= n; ++i) {
            auto v = dp[i][k] + 1LL * c[i].r * c[i].r;
            best_v = std::max(best_v, v);
        }

        double answer = 1.0 * best_v * 3.14159265358979;
        std::cout << "Case #" << ti << ": " << std::fixed
                  << std::setprecision(10) << answer << std::endl;
    }
}
