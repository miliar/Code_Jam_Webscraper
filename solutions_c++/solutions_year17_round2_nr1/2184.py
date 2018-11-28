#include <iostream>
#include <iomanip>

using namespace std;

#define EPS 5e-7

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int tid = 0; tid < T; ++tid) {
        int D, N;
        int K[1010], S[1010];

        // Input
        cin >> D >> N;
        for (int i = 0; i < N; ++i) {
            cin >> K[i] >> S[i];
        }

        // Solve
        long double l = 1, r = 1e13;
        while (l + EPS < r) {
            long double mid = (l + r) / 2;

            // Check mid
            bool ok = true;
            for (int i = 0; i < N; ++i) {
                if (mid <= S[i]) {
                    continue;
                }
                // mid * t = K + s * t
                double t = K[i] / (mid - S[i]);
                if (t * mid < D) {
                    ok = false;
                    break;
                }
            }

            if (ok) {
                l = mid + EPS;
            } else {
                r = mid;
            }
        }
        cout << fixed << setprecision(6) << "Case #" << tid + 1 << ": " << l << endl;
    }

    return 0;
}
