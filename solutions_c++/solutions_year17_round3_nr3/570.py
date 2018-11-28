#include <iostream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <limits>
#include <cassert>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <string>
#include <iomanip>


long solve()
{
    return 0;
}


void run_test_case()
{
    double const eps = 1e-9;

    size_t N, K;
    std::cin >> N >> K;
    double U;
    std::cin >> U;
    std::vector<double> P;
    for (size_t i = 0; i < N; ++i) {
        double p;
        std::cin >> p;
        P.push_back(p);
    }

    std::cerr <<std::setprecision(10);

    if (N > 1) {
        // spread uniformly
        while (U > eps) {
            std::sort(P.begin(), P.end());
            double p = P[0];
            size_t m = 1; // how many in the same size class
            while (m < N && P[m] < p + eps) {
                ++m;
            }
            assert(m >= N || P[m] >= p + eps);
            if (m < N) {
                double d = std::min(P[m] - P[m-1], U/m);
                std::cerr << "increase " << m << " by " << d << "\n";
                U -= m * d;
                assert(U >= -eps);
                for (size_t i = 0; i < m; ++i) {
                    P[i] += d;
                    assert(P[i] <= 1.0);
                }
            } else {
                double d = U/m; //std::min(1 - P[m-1], U/m);
                std::cerr << "increase " << m << " by " << d << "\n";
                U -= m * d;
                assert(U >= 0);
                for (size_t i = 0; i < m; ++i) {
                    P[i] += d;
                    assert(P[i] <= 1.0);
                }
            }
        }
    } else {
        assert(N == 1);
        P[0] += U;
        U = 0;
    }

    if (N == K) {
        double total = 1;
        for (double p : P) {
            total *= p;
        }
        printf("%9f", total);
    } else {
        std::cout << "???";
    }
}


int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        std::cout << "Case #" << t << ":";
        run_test_case();
        std::cout << '\n';
    }

    return 0;
}
