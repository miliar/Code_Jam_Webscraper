#include <cmath>
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <utility>

typedef std::vector<std::pair<int, int>> vpii;

int solve(int A_c, int A_j, vpii& AC, vpii& AJ)
{
    if (A_c <= 1 && A_j <= 1) return 2;

    if (A_c == 2 || A_j == 2) {
        vpii* A_ = nullptr;
        if (AC.size() > 0) A_ = &AC;
        if (AJ.size() > 0) A_ = &AJ;

        auto& A = *A_;
        auto p1 = A[0];
        auto p2 = A[1];

        if (p2.second - p1.first <= 720) {
            return 2;
        }

        if (p1.second + 1440 - p2.first <= 720) {
            return 2;
        }

        return 4;
    }

    return -1;
}

int main()
{
    auto T = 0;
    std::cin >> T;

    for (auto i = 0; i < T; ++i) {
        auto A_c = 0;
        auto A_j = 0;
        std::cin >> A_c >> A_j;

        auto AC = vpii{};
        for (auto j = 0; j < A_c; ++j) {
            auto s = 0;
            auto e = 0;
            std::cin >> s >> e;
            AC.push_back({s, e});
        }

        auto AJ = vpii{};
        for (auto j = 0; j < A_j; ++j) {
            auto s = 0;
            auto e = 0;
            std::cin >> s >> e;
            AJ.push_back({s, e});
        }

        std::sort(AC.begin(), AC.end());
        std::sort(AJ.begin(), AJ.end());
        auto result = solve(A_c, A_j, AC, AJ);
        printf("Case #%d: %d\n", i+1, result);
    }
    return 0;
}
