#include <algorithm>
#include <iostream>
#include <limits>
#include <iomanip>
#include <cmath>

long long T, N, K, R[1000], H[1000], order[1000];

int main() {
    std::ios::sync_with_stdio(false);
    std::cout.tie(0);
    std::cin.tie(0);

    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        std::cin >> N >> K;
        for (int n = 0; n < N; ++n) {
            std::cin >> R[n] >> H[n];
            order[n] = n;
        }
        std::sort(order, order + N, [](int a, int b){return H[a] * R[a] < H[b] * R[b];});

        long double result = 0;
        for (int i = 0; i < N; ++i) {
            long double cresult = 0;
            int pccount = 1;

            cresult = M_PI * (long double)(R[i] * R[i]) + 2 * M_PI * (long double)(H[i] * R[i]);
            for (int j = N - 1; j >= 0 && pccount < K; --j) {
                if (order[j] == i || R[order[j]] > R[i])
                    continue;
                cresult += 2 * M_PI * (long double)(H[order[j]] * R[order[j]]);
                pccount ++;
            }

            if (pccount == K)
                result = std::max(result, cresult);
        }


        std::cout << "Case #" << t << ": "
            << std::setprecision(std::numeric_limits<long double>::digits10 + 1)
            << result
            << "\n";
    }
}
