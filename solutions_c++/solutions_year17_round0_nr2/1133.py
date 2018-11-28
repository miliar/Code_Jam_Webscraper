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


std::string solve(std::string N)
{
    assert(N[0] > '0');
    std::cerr << N;
    for (unsigned int i = 0; i < N.size() - 1; ++i) {
        if (N.at(i) > N.at(i+1)) {
            while (i > 0 && N.at(i - 1) == N.at(i)) {
                --i;
            }
            assert(i >= 0);
            std::cerr << " (" << i << ")";

            assert(N[i] > '0');
            N[i] -= 1;
            for (unsigned int j = i + 1; j < N.size(); ++j) {
                N[j] = '9';
            }
            break;
        }
    }

    std::cerr << " -> ";

    // remove leading zeros
    unsigned k = 0;
    while (N[k] == '0') {
        ++k;
    }
    assert(k < N.size());

    return N.substr(k);
}


void run_test_case()
{
    std::string N;
    std::cin >> N;

    std::cout << solve(N);
}


int main()
{
    std::cerr << "long\t" << std::numeric_limits<long>::lowest() << '\t' << std::numeric_limits<long>::max() << '\n';
    static_assert(1'000'000'000'000'000'000 < std::numeric_limits<long>::max(), "datatype too small");

    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        std::cout << "Case #" << t << ": ";
        run_test_case();
        std::cout << '\n';
    }

    return 0;
}
