#include <iostream>
using namespace std;
const int M = 101;
int dp[M][M][M][4];
int cnt[4];
int main() {
    ios::sync_with_stdio(0);
    int tc; cin >> tc;
    for (int t = 1; t <= tc; t++) {
        int n, p;
        cin >> n >> p;
        for (int j = 0; j < 4; j ++)
            cnt[j] = 0;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            cnt[x % p] ++;
        }
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= n; j++)
                for (int k = 0; k <= n; k++)
                    if (i + j + k <= n && i|j|k)
                        for (int rem = 0; rem < p; rem++) {
                            dp[i][j][k][rem] = 0;
                            if (i) dp[i][j][k][rem] = dp[i - 1][j][k][(rem+1)%p];
                            if (j) dp[i][j][k][rem] = max(dp[i][j][k][rem], dp[i][j - 1][k][(rem+2)%p]);
                            if (k) dp[i][j][k][rem] = max(dp[i][j][k][rem], dp[i][j][k - 1][(rem+3)%p]);
                            if (!rem) dp[i][j][k][rem] ++;
                        }

        cout << "Case #" << t << ": ";
        cout << dp[cnt[1]][cnt[2]][cnt[3]][0] + cnt[0] << endl;
    }
}
