#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <iostream>
#include <utility>

using namespace std;

pair<uint64_t, uint64_t> solveReduce(uint64_t n, uint64_t k)
{
    uint64_t upper = n / 2;
    uint64_t lower = upper - 1;
    uint64_t numUpper = (n & 1) ? 2 : 1;
    uint64_t numLower = (n & 1) ? 0 : 1;
    uint64_t k1 = 1;
    uint64_t k2 = 1;
    uint64_t count = 2;
    while (true) {
        if ((k1 <= k) && (k <= k2)) {
            uint64_t row = k - k1;
            uint64_t num1 = (row < numUpper) ? upper : lower;
            uint64_t num2 = ((row + count / 2) < numUpper) ? upper : lower;
            return make_pair(num1, num2);
        }
        k1 = k2 + 1;
        k2 = 2 * k1 - 1;
        count *= 2;
        if (upper & 1) {
            numUpper = count - numLower;
        } else {
            numLower = count - numUpper;
        }
        upper /= 2;
        lower = upper - 1;
    }
}

int main()
{
    size_t t;
    cin >> t;
    for (size_t i = 1; i <= t; ++i) {
        uint64_t n, k;
        cin >> n >> k;
        pair<uint64_t, uint64_t> sol = solveReduce(n, k);
        cout << "Case #" << i << ": " << sol.first << " " << sol.second << endl;
    }
}