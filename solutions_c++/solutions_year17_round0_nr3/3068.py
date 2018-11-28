#include <cstdio>
#include <cstdint>
#include <utility>
#include <iostream>

using namespace std;

void solve() {
    uint64_t N, K;
    scanf("%lu %lu", &N, &K);

    uint64_t cumsum = 0;
    uint64_t p = 1;
    uint64_t is = N;

    while (cumsum + p < K) {
        is >>= 1;
        cumsum += p;
        p <<= 1;
    }

    if (is == 1) {
        printf("0 0\n");
        return;
    }

    uint64_t r = K - cumsum;
    uint64_t big_intervals = (N-cumsum) - p * (is-1);
    if (r > big_intervals) {
        is -= 1;
    }

    uint64_t L = (is-1) >> 1;
    uint64_t R = (is) >> 1;

    if (L < R)
        swap(L, R);

    printf("%lu %lu\n", L, R);
}

int main(void) {

    int T; scanf("%u", &T);

    for (int t = 1; t <= T; t++) {
        printf("Case #%u: ", t);
        solve();
    }
    
    return 0;
}
