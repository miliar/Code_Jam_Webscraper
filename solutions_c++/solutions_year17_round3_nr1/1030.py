#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

const long double PI = 3.14159265358979323;
int T;
int N, K;
long double DP[1005][1005]; // N, K
pair<int, int> RH[1005]; // R, H

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int TC = 1; TC <= T; ++TC) {
        cin >> N >> K;
        for (int a = 1; a <= N; ++a) {
            cin >> RH[a].first >> RH[a].second;
            for (int b = 1; b <= K; ++b)
                DP[a][b] = 0;
        }
        sort(RH + 1, RH + N + 1);
        for (int a = 1; a <= N; ++a) {
            // Try starting from here?
            int R = RH[a].first, H = RH[a].second;
            DP[a][1] = PI * R * R + H * (2 * PI * R);
            for (int b = 1; b < a; ++b) {
                int R2 = RH[b].first;
                for (int c = 2; c <= K; ++c) {
                    long double extra = PI * R * R + H * (2 * PI * R) - PI * R2 * R2;
                    DP[a][c] = max(DP[a][c], DP[b][c - 1] + extra);
                }
            }
        }
        long double maxn = 0;
        for (int a = 1; a <= N; ++a) {
            maxn = max(maxn, DP[a][K]);
        }
        cout << "Case #" << TC << ": " << fixed << setprecision(9) << maxn << "\n";
    }
    return 0;
}
