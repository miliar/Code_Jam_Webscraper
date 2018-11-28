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


void solve(long N, long K)
{
    // hole size -> number of holes with this size
    std::map<long, long, std::greater<long>> holes;

    // we start with one hole of size N
    holes[N] = 1;

    while (K > 1) {
        // person always chooses the largest hole
        auto it = holes.begin();
        long h_size = it->first;
        long& h_num = it->second;
        assert(h_size > 0);
        assert(h_num > 0);

        // How many people are going to occupy holes of this size (not more than available holes, not more than available people)
        long num = std::min(h_num, K - 1);

        long n1, n2;
        if (h_size % 2 == 0) {
            // even number of stalls
            // => person will sit at the one left to the middle
            n1 = h_size / 2 - 1;
            n2 = h_size / 2;
        } else {
            // odd number of stalls
            // => person will sit at center stall
            n1 = h_size / 2;
            n2 = h_size / 2;
        }
        // we might add "holes" of size 0 here, but since K <= N we won't let a person sit there.
        holes[n1] += num;
        holes[n2] += num;
        h_num -= num;
        K -= num;

        assert(h_num == it->second);  // to be sure that reference to value works

        if (h_num == 0) {
            holes.erase(it);
        }
    }

    // now the last person will occupy the largest remaining hole
    auto it = holes.begin();
    long h_size = it->first;
    assert(h_size > 0);
    assert(it->second > 0);
    if (h_size % 2 == 0) {
        std::cout << (h_size / 2) << ' ' << (h_size / 2 - 1);
    } else {
        std::cout << (h_size / 2) << ' ' << (h_size / 2);
    }

    return;
}


void run_test_case()
{
    long N, K;
    std::cin >> N >> K;
    assert(1 <= K);
    assert(K <= N);

    solve(N, K);
}


int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        std::cout << "Case #" << t << ": ";
        run_test_case();
        std::cout << '\n';
    }

    return 0;
}
