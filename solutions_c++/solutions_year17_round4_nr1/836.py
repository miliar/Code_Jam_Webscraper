#include <bits/stdc++.h>

using namespace std;

int tc, n, p;

const int MAX_N = 105;

int dp[MAX_N][MAX_N][MAX_N][4];
int cnt[4];

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> n >> p;
        fill(cnt, cnt + 4, 0);
        for (int i = 0; i < n; i++) {
            int t;
            cin >> t;
            cnt[t % p]++;
        }
        int ans = 0;
        for (int i = 0; i <= cnt[1]; i++) {
            for (int j = 0; j <= cnt[2]; j++) {
                for (int k = 0; k <= cnt[3]; k++) {
                    for (int last = 0; last < 4; last++) {
                        dp[i][j][k][last] = 0;
                    }
                }
            }
        }
        dp[0][0][0][0] = cnt[0];
        for (int i = 0; i <= cnt[1]; i++) {
            for (int j = 0; j <= cnt[2]; j++) {
                for (int k = 0; k <= cnt[3]; k++) {
                    for (int last = 0; last < 4; last++) {
                        int bon = 0;
                        if (last == 0) {
                            bon++;
                        }
                        dp[i + 1][j][k][(last + 1) % p] = max(dp[i + 1][j][k][(last + 1) % p], dp[i][j][k][last] + bon);
                        dp[i][j + 1][k][(last + 2) % p] = max(dp[i][j + 1][k][(last + 2) % p], dp[i][j][k][last] + bon);
                        dp[i][j][k + 1][(last + 3) % p] = max(dp[i][j][k + 1][(last + 3) % p], dp[i][j][k][last] + bon);
                    }
                }
            }
        }
        for (int i = 0; i < 4; i++) {
            ans = max(ans, dp[cnt[1]][cnt[2]][cnt[3]][i]);
        }
        cout << ans << "\n";
    }
}
