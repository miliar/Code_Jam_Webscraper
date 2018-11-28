#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long long D, N;
        cin >> D >> N;
        double maxTime = 0.0;
        for (int n = 0; n < N; n++) {
            long long K, S;
            cin >> K >> S;
            double actTime = (double) (D - K) / (double) S;
            if (actTime > maxTime) {
                maxTime = actTime;
            }
        }
        cout << fixed << "Case #" << t << ": " << setprecision(6) << (double) D / maxTime << endl;
    }
    return 0;
}
