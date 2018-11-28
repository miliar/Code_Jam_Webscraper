#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
using namespace std;


double P(double r) {
    return M_PI * 2 * r;
}

double S(double r) {
    return M_PI * r * r;
}


int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int tid = 0; tid < T; ++tid) {
        int N, K;
        pair<int, int> pan[1000];
        cin >> N >> K;
        for (int i = 0; i < N; ++i) {
            cin >> pan[i].first >> pan[i].second;
        }
        sort(pan, pan + N, greater< pair<int, int> >());

        double dp[1000][1001];
        for (int i = 0; i < N; ++i) {
            dp[i][0] = 0;
            dp[i][1] = P(pan[i].first) * pan[i].second + S(pan[i].first);
            if (i > 0) {
                dp[i][1] = max(dp[i][1], dp[i - 1][1]);
            }
            for (int j = 2; j <= i + 1; ++j) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + P(pan[i].first) * pan[i].second);
            }
        }

        cout << fixed << setprecision(9) << "Case #" << tid + 1 << ": " << dp[N - 1][K] << endl;
    }


    return 0;
}
