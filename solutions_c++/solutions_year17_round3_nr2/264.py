#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int n, m, x, y;
int busy[1500];
int dp[2][750][750];

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for (int ttt = 1; ttt <= T; ++ttt) {
        cin >> n >> m;
        for (int i = 0; i < 1500; ++i)
            busy[i] = 0;
        while (n--) {
            cin >> x >> y;
            for (; x < y; ++x)
                busy[x] = 1;
        }
        while (m--) {
            cin >> x >> y;
            for (; x < y; ++x)
                busy[x] = 2;
        }

        int ans = 2e9;
        for (int k0 = 1; k0 <= 2; ++k0) {
            if (busy[0] == k0)
                continue;
            for (int i = 0; i < 750; ++i)
                for (int j = 0; j < 750; ++j)
                    dp[0][i][j] = dp[1][i][j] = 2e9;
            if (k0 == 1)
                dp[0][1][0] = 0;
            else
                dp[1][0][1] = 0;
            for (int len = 2; len <= 1440; ++len) {
                for (int cameron = 0; cameron <= len && cameron <= 720; ++cameron) {
                    /// cameron
                    if (busy[len - 1] != 1) {
                        if (cameron) {
                            dp[0][cameron][len - cameron] = min(dp[0][cameron][len - cameron],
                                    dp[0][cameron - 1][len - cameron] + (len == 1440 && k0 == 2));
                            dp[0][cameron][len - cameron] = min(dp[0][cameron][len - cameron],
                                    dp[1][cameron - 1][len - cameron] + 1 + (len == 1440 && k0 == 2));
                        }
                    }

                    /// jamie
                    if (busy[len - 1] != 2) {
                        if (len - cameron) {
                            dp[1][cameron][len - cameron] = min(dp[1][cameron][len - cameron],
                                    dp[1][cameron][len - cameron - 1] + (len == 1440 && k0 == 1));
                            dp[1][cameron][len - cameron] = min(dp[1][cameron][len - cameron],
                                    dp[0][cameron][len - cameron - 1] + 1 + (len == 1440 && k0 == 1));
                        }
                    }
                }
            }
            ans = min(ans, min(dp[0][720][720], dp[1][720][720]));
        }

        cout << "Case #" << ttt << ": " << ans << "\n";
    }

    return 0;
}
