#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

void solve() {
    int N, K;
    cin >> N >> K;
        
    double U; cin >> U;

    vector<double> P(N);
    for (auto & el : P) cin >> el;

    sort(P.begin(), P.end());

    for (int i = 1; i < N; i++) {
        double incr_required = (P[i] - P[i-1]) * i;
        if (incr_required > U) {
            double incr_received = U / i;
            for (int j = 0; j < i; j++) {
                P[j] += incr_received;
            }
            U = 0;
            break;
        }
        else {
            U -= incr_required;
            for (int j = 0; j < i; j++) {
                P[j] = P[i];
            }
        }
    }
                    
    if (U > 0) {
        double incr_received = U/N;
        for (int i = 0; i < N; i++) {
            P[i] = P[N-1] + incr_received;
        }
    }

    double p_succeed = 1.0;

    for (int i = 0; i < N; i++) {
        p_succeed *= P[i];
    }

    printf("%.9f\n", p_succeed);
}

int main (void) {
    
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
