#include <iostream>

using namespace std;
typedef long long ll;


int main() {
    freopen("../C-small-attempt1.in", "r", stdin);
    freopen("../C-small.out1", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);

        int n, q;
        cin >> n >> q;
        int e[n + 10], s[n + 10];
        int d[n + 10][n + 10];
        for (int i = 1; i <= n; i++) {
            cin >> e[i] >> s[i];
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cin >> d[i][j];
            }
        }
        double dis[n + 10];
        dis[1] = 0;
        for (int i = 2; i <= n; i++) {
            dis[i] = dis[i - 1] + d[i - 1][i];
            //cout << i << " " << dis[i] << endl;
        }
        double dp[n + 10];
        for (int i = 1; i <= n; i++) {
            dp[i] = 999999999999999999.0;
        }
        dp[1] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                if (dis[j] - dis[i] <= e[i]) {
                    dp[j] = min(dp[j], dp[i] + ((dis[j] - dis[i]) / s[i]));
                }
            }
        }
        while (q--) {
            int ss, ee;
            cin >> ss >> ee;
            printf("%.10f\n", dp[n]);
        }

    }

    return 0;
}