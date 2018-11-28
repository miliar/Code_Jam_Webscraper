#include <cstdio>
#include <map>
#include <queue>
#include <iostream>

std::pair<int64_t, int64_t> solve(int64_t N, int64_t K)
{
    auto S = std::priority_queue<int64_t>{};
    auto M = std::map<int64_t, int64_t>{};
    S.push(N);
    M[N] = 1;
    while (K) {
        auto n = S.top();
        S.pop();

        auto c = M[n];
        if (K > c) {
            K -= c;
        } else {
            K = 0;
        }

        // 5 -> 2, 2; 4 -> 2, 1
        auto a = n/2;
        auto b = (n-1)/2;

        if (a) {
            if (M.find(a) == M.end()) {
                S.push(a);
                M[a] = c;
            } else {
                M[a] += c;
            }
        }
        if (b) {
            if (M.find(b) == M.end()) {
                S.push(b);
                M[b] = c;
            } else {
                M[b] += c;
            }
        }

        if (!K) {
            return {a, b};
        }
    }

    throw std::exception{};
}

int main()
{
    auto T = 0;
    std::cin >> T;
    for (auto i = 0; i < T; ++i) {
        auto N = 0LL;
        auto K = 0LL;
        std::cin >> N >> K;
        auto result = solve(N, K);
        printf("Case #%d: %lld %lld\n", i + 1, result.first, result.second);
    }
    return 0;
}
