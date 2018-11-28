#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

template<class T>
inline T read() {
    T value;
    std::cin >> value;
    return value;
}

int main() {
    auto T = read<int>();
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        int N, K; std::cin >> N >> K;
        double U; std::cin >> U;
        std::vector<double> P(N);
        for (int i = 0; i < N; ++i) {
            std::cin >> P[i];
        }
        std::sort(P.begin(), P.end());

        // small dataset 1, K = N
        for (int i = 1; i <= N && U > 0.0; ++i) {
            double a = P[i-1];
            double b = (i < N) ? P[i] : 1.0;
            double d = (b - a) * i; // how much we want added
            if (d > U) {
                d = U; // clamp to available training units
            }
            U -= d;
            d /= i; // spread equaly among the prefix
            for (int j = 0; j < i; ++j) {
                P[j] += d;
            }
        }

        double p = 1.0;
        for (int i = 0; i < N; ++i) {
            p *= P[i];
        }
        printf("Case #%d: %.9lf\n", caseNum, p);
    }
    return 0;
}
