#include <iostream>
using namespace std;

int n, p;
int dp[110][110][110];
int cnt[100];

int main() {
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> n >> p;
        memset(cnt, 0, sizeof(cnt));
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            if (x % p == 0) ans++;
            else cnt[x % p]++;
        }
        memset(dp, 0, sizeof(dp));
        //dp[0][0][0] = 0;
        int x1 = cnt[1];
        int x2 = cnt[2];
        int x3 = cnt[3];
        for (int i = 0; i <= x1; i++) {
            for (int j = 0; j <= x2; j++) {
                for (int k = 0; k <= x3; k++) {
                    int m = (i * 1 + j * 2 + k * 3) % p;
                    if (i < x1) {
                        dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k] + (m == 0));
                    }
                    if (j < x2) {
                        dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k] + (m == 0));
                    }
                    if (k < x3) {
                        dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k] + (m == 0));
                    }
                }
            }
        }
        ans += dp[x1][x2][x3];
        cout << "Case #" << Case++ << ": " << ans << endl;
    }
    return 0;
}
