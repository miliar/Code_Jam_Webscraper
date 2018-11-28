#include <cmath>
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <utility>

struct Pancake
{
    int i;
    int r;
    int h;
    int64_t rh2;
};

double solve(int N, int K, std::vector<Pancake>& P_by_rh2)
{
    std::sort(P_by_rh2.begin(), P_by_rh2.end(), [](const auto& x, const auto& y) -> bool {
        return x.rh2 > y.rh2;
    });

    auto best = 0LL;
    for (auto it = P_by_rh2.begin(); it != P_by_rh2.end(); ++it) {
        auto& bottom_p = *it;

        auto current = int64_t{bottom_p.r} * int64_t{bottom_p.r} + bottom_p.rh2;
        auto remaining = K - 1;
        for (auto it2 = P_by_rh2.begin(); it2 != P_by_rh2.end() && remaining > 0; ++it2) {
            if (it == it2) continue;
            auto& p = *it2;

            if (p.r <= bottom_p.r) {
                --remaining;
                current += p.rh2;
            }
        }
        if (remaining > 0) continue; // discard if bottom pancake is too small

        if (current > best) best = current;
    }

    return best * M_PI;
}

int main()
{
    auto T = 0;
    std::cin >> T;

    for (auto i = 0; i < T; ++i) {
        auto N = 0;
        auto K = 0;
        std::cin >> N >> K;

        auto P = std::vector<Pancake>{};
        for (auto j = 0; j < N; ++j) {
            auto r = 0;
            auto h = 0;
            std::cin >> r >> h;
            P.push_back({j, r, h, int64_t{r}*int64_t{h}*2LL});
        }

        auto result = solve(N, K, P);
        printf("Case #%d: %.8f\n", i+1, result);
    }
    return 0;
}
