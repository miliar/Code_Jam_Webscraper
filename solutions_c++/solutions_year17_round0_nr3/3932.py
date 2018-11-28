#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

int main() {

    int T;

    unsigned long long int N, K, sum;

    cin >> T;

    for (int t = 1; t <= T; t++) {

        cin >> N >> K;

        sum = (N - K) / (1 << (int) log2(K));

        printf("Case #%d: %llu %llu \n", t, sum - sum / 2, sum / 2);
    }

    return 0;
}
