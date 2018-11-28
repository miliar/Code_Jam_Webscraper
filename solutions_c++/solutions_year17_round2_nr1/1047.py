#include <cstdio>
#include <iostream>
using namespace std;

long long T, D, N, K, S;

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        double time = 0;
        cin >> D >> N;
        for (int i = 0; i < N; i++) {
            cin >> K >> S;
            time = max(time, (D-K+0.0)/S);
        }
        printf("Case #%d: %.7f\n", t, D/time);
    }
    return 0;
}
