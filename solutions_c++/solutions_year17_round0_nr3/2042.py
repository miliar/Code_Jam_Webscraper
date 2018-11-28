#include <stdio.h>
#include <queue>
#include <iostream>

#define NMAX 1000001

using namespace std;

int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);

    int tests, power;
    long long N, K, currMin, currMax, noMax, minLR, maxLR, power2, diff;

    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cin >> N >> K;
        currMin = currMax = N;

        power = 1;
        while (true) {
            power2 = 1LL << power;

            if (K < power2) break;

            if (1 != currMin) currMin = (currMin - 1) / 2;
            if (1 != currMax) currMax /= 2;

            ++power;
        }

        cout << "Case #" << test << ": ";

        power2 >>= 1;
        diff = K - power2;
        noMax = (N - power2 + 1) % power2;

        if (diff < noMax) {
            minLR = (currMax - 1) / 2;
            maxLR = currMax / 2;
        } else {
            minLR = (currMin - 1) / 2;
            maxLR = currMin / 2;
        }

        cout << maxLR << " " << minLR << endl;
    }

    return 0;
}
