#include <bits/stdc++.h>
using namespace std;

const int kN = 1e2 + 10;
const double kM = 1e-9;
double E[kN], S[kN], D[kN][kN], dp[kN];

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T, t = 1;
    cin >> T;
    while (t <= T) {
        int N, Q;
        cin >> N >> Q;
        for (int i = 0; i < N; ++i) cin >> E[i] >> S[i];
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) cin >> D[i][j];
        }
        for (int i = 0, u, v; i < Q; ++i) cin >> u >> v;
        //cout << N << "::" << Q << endl;
        fill(dp, dp + kN, 1e18);
        dp[0] = 0;
        for (int i = 0; i < N; ++i) {
            double d = 0;
            for (int j = i + 1; j < N; ++j) {
                d += D[j - 1][j];
                //cout << i << ": " << j << ":: " << d << " " << D[j - 1][j] << endl;
                if (d > E[i] + kM) break;
                dp[j] = min(dp[j], dp[i] + d / S[i]);
            }
        }
        cout << "Case #" << t++ << ": ";
        cout << fixed << setprecision(9) << dp[N - 1] << "\n";
    }
    return 0;
}
