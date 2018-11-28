#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int T;
    cin >> T;
    cout << fixed << setprecision(6);
    for(int i = 1; i <= T; ++i) {
        int D, N;
        cin >> D >> N;
        double maxTime = 0;
        for(int j = 0; j < N; ++j) {
            int K, S;
            cin >> K >> S;
            maxTime = max(maxTime, (double) (D - K) / S);
        }

        cout << "Case #" << i << ": " << D / maxTime << endl;
    }
}