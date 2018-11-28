#include <cmath>
#include <iostream>
#include <vector>

typedef long double ld;
typedef unsigned long long ull;
typedef long long ll;

const ld pi = std::atan(1) * 4;

int main() {
    ull T;
    std::cin >> T;
    std::cout.precision(9);

    for (ull t = 1; t <= T; ++t) {
        ull N, K;
        std::cin >> N >> K;
        std::vector<std::pair<std::pair<ld, ld>, std::pair<ull, ull>>> SSRH(N);
        for (auto&& SSRHi : SSRH) {
            std::cin >> SSRHi.second.first >> SSRHi.second.second;
            SSRHi.first.first = 2 * pi * SSRHi.second.first * SSRHi.second.second;
            SSRHi.first.second = pi * SSRHi.second.first * SSRHi.second.first;
        }
        std::sort(SSRH.begin(), SSRH.end());
        std::reverse(SSRH.begin(), SSRH.end());
        ld max_area = 0;
        for (auto&& SSRHi1 : SSRH) {
            ld area = SSRHi1.first.first + SSRHi1.first.second;
            ld max_radii = SSRHi1.second.first;
            ull chosen = 1;
            if (chosen < K) {
                for (auto &&SSRHi2 : SSRH) {
                    if (&SSRHi2 == &SSRHi1 || SSRHi2.second.first > max_radii) {
                        continue;
                    }
                    area += SSRHi2.first.first;
                    if (++chosen == K) {
                        break;
                    }
                }
            }
            if (chosen == K) {
                max_area = std::max(max_area, area);
            }
        }
        std::cout << "Case #" << t << ": " << std::fixed << max_area << std::endl;
    }
    return 0;
}