#include <iostream>
#include <algorithm>

using namespace std;

double calcTime(long dist, int speed) {
    return ((double)(dist))/((double)(speed));
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        long D;
        int N;
        cin >> D >> N;

        double maxTime = 0.0;
        for (int j = 0; j < N; ++j) {
            long K;
            int S;
            cin >> K >> S;
            maxTime = max(maxTime, calcTime(D-K, S));
        }

        double result = ((double)(D))/maxTime;
        cout.precision(6);
        cout << "Case #" << i+1 << ": " << fixed << result << endl;
    }

    return 0;
}
