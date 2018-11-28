#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main() {
    long long dist[100][100];
    long long E[100];
    long long S[100];

    double dp[100][100];
    long long rest[100][100];

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, Q;
        cin >> N >> Q;
        vector<int> U(Q), V(Q);
        for (int i = 0; i < N; i++) {
            cin >> E[i] >> S[i];
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                dp[i][j] = 1e50;
                cin >> dist[i][j];
            }
        }
        for (int q = 0; q < Q; q++) {
            cin >> U[q] >> V[q];
        }
        dp[0][0] = 0.0;
        rest[0][0] = E[0];
        for (int i = 1; i < N; i++) {
            dp[i][i] = 1e50;
            rest[i][i] = E[i];
            for (int j = 0; j < i; j++) {
                if (rest[i - 1][j] >= dist[i - 1][i]) {
                    dp[i][j] = dp[i - 1][j] + (double) dist[i - 1][i] / S[j];
                    rest[i][j] = rest[i - 1][j] - dist[i - 1][i];
                    dp[i][i] = min(dp[i][i], dp[i][j]);
                }
            }
        }
        double res = dp[N - 1][N - 1];
        for (int i = 0; i < N; i++) {
            res = min(dp[N - 1][i], res);
        }
        cout << fixed << "Case #" << t << ": " << setprecision(8) << res << endl;
    }
    return 0;
}
