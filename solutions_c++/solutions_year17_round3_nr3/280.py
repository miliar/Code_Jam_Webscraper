#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, K;
        cin >> N >> K;
        double U;
        cin >> U;
        vector<double> P(N);
        for (int n = 0; n < N; n++) {
            cin >> P[n];
        }
        sort(P.begin(), P.end());
        for (int i = 0; i < N; i++) {
            int subN = i + 1;
            double subU;
            if (i + 1 == N) {
                subU = min(U, (1.0 - P[0]) * (double) subN);
            } else if (P[i] == P[subN]) {
                continue;
            } else {
                subU = min(U, (P[subN] - P[0]) * (double) subN);
            }
            for (int j = 0; j < subN; j++) {
                P[j] += subU / (double) subN;
            }
            if (subU == U) {
                break;
            }
            U -= subU;
        }
        double ans = 1.0;
        for (int n = 0; n < N; n++) {
            ans *= P[n];
        }
        cout << "Case #" << t << ": " << fixed << setprecision(9) << ans << endl;
    }
	return 0;
}
