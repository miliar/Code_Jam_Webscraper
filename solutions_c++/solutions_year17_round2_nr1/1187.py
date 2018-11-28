#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    int T; cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        int D, N; cin >> D >> N;
        float slowestTime = 0;
        for (int i = 0; i < N; i++){
            int K, S; cin >> K >> S;
            double time = (double)(D - K) / S;
            if (time > slowestTime) {
                slowestTime = time;
            }
        }
        double ans = D / slowestTime;
        printf("Case #%d: %.6f\n", tt, ans);
    }

    return 0;
}
