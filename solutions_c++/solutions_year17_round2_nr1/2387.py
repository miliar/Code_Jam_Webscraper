#include <iostream>
#include <limits>

using namespace std;

typedef long long ll;

int main() {
    int T;

    cin >> T;

    cout.precision(17);

    for (int t = 1; t <= T; t++) {     
        ll D, N;
        ll K, S;
        
        cin >> D >> N;

        double max_time = 0;
        
        for (int i = 0; i < N; i++) {
            cin >> K >> S;

            if (K < D) {
                double time = 1.0 * (D - K) / S;
                if (time > max_time) {
                    max_time = time;
                }
            }
        }
        
        cout << "Case #" << t << ": " << 1.0 * D / max_time << endl;
    }

    return 0;
}
