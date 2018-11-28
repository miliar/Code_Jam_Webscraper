#include <bits/stdc++.h>

using namespace std;

#define N 100
int n, p, g[N];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    for (int it = 1; it <= t; it++) {
        cin >> n >> p;
        int nsum = 0;
        for (int i = 0; i < n; i++)
            cin >> g[i], nsum += g[i];
        vector<int> gx[4];
        for (int i = 0; i < n; i++) {
            gx[g[i] % p].push_back(g[i]);
        }
        if (p == 2) {
            int xm = gx[0].size() + gx[1].size();
            int dp[p][xm + 1][xm + 1];
            dp[0][1][0] = 1;
            dp[0][0][1] = 1;
            dp[1][1][0] = 0;
            dp[1][0][1] = 0;
            for (int k = 2; k <= xm; k++) {
                for (int i = 0; i <= k; i++) {
                    for (int l = 0; l < p; l++) {
                        int j = k - i;
                        if (i > gx[0].size())
                            continue;
                        if (j > gx[1].size())
                            continue;
                        dp[l][i][j] = 0;
                        if (i >= 1)
                            dp[l][i][j] = max(dp[l][i][j],
                                              dp[(l + 0) % p][i - 1][j]);
                        if (j >= 1)
                            dp[l][i][j] = max(dp[l][i][j],
                                              dp[(l + 1) % p][i][j - 1]);
                        dp[l][i][j] += l == 0;
                    }
                }
            }
            int ans = dp[0][gx[0].size()][gx[1].size()];
            // if (ans > (nsum - 1 + p) / p)
            //    ans = (nsum - 1 + p) / p;
            cout << "Case #" << it << ": " << ans << endl;
        } else if (p == 3) {
            int xm = gx[0].size() + gx[1].size() + gx[2].size();
            int dp[p][xm + 1][xm + 1][xm + 1];
            for (int l = 0; l < p; l++) {
                if (gx[0].size() > 0)
                    dp[l][1][0][0] = gx[0][1 - 1] > l && l == 0 ? 1 : 0;
                if (gx[1].size() > 0)
                    dp[l][0][1][0] = gx[1][1 - 1] > l && l == 0 ? 1 : 0;
                if (gx[2].size() > 0)
                    dp[l][0][0][1] = gx[2][1 - 1] > l && l == 0 ? 1 : 0;
            }
            for (int kp = 2; kp <= xm; kp++) {
                for (int i = 0; i <= kp; i++) {
                    for (int j = 0; j + i <= kp; j++) {
                        int k = kp - i - j;
                        for (int l = 0; l < p; l++) {
                            if (i > gx[0].size())
                                continue;
                            if (j > gx[1].size())
                                continue;
                            if (k > gx[2].size())
                                continue;
                            
                            dp[l][i][j][k] = 0;
                            if (i >= 1)
                                dp[l][i][j][k] =
                                    max(dp[l][i][j][k],
                                        dp[(l + 0) % p][i - 1][j][k] +
                                            (gx[0][i - 1] > l && l == 0 ? 1 : 0));
                            if (j >= 1)
                                dp[l][i][j][k] =
                                    max(dp[l][i][j][k],
                                        dp[(l + 1) % p][i][j - 1][k] +
                                            (gx[1][j - 1] > l && l == 0 ? 1 : 0));
                            if (k >= 1)
                                dp[l][i][j][k] =
                                    max(dp[l][i][j][k],
                                        dp[(l + 2) % p][i][j][k - 1] +
                                            (gx[2][k - 1] > l && l == 0 ? 1 : 0));
                            // dp[l][i][j][k] += l == 0;
                            // printf(" %d %d %d = %d (%d, %d, %d)\n", i, j, k, dp[l][i][j][k], gx[0].size(), gx[1].size(), gx[2].size());
                            // dp[l][i][j][k]);
                        }
                    }
                }
            }
            int ans = dp[0][gx[0].size()][gx[1].size()][gx[2].size()];
            // if (ans > (nsum - 1 + p) / p)
            //     ans = (nsum - 1 + p) / p;
            cout << "Case #" << it << ": " << ans << endl;
        } else if (p == 4) {
            int xm = gx[0].size() + gx[1].size() + gx[2].size() + gx[3].size();
            // cerr << "a" << endl;
            int dp[p][gx[0].size() + 1][gx[1].size() + 1][gx[2].size() + 1][gx[3].size() + 1];
            // cerr << "a" << endl;
            for (int l = 0; l < p; l++) {
                if (gx[0].size() > 0)
                    dp[l][1][0][0][0] = gx[0][1 - 1] > l && l == 0 ? 1 : 0;
                if (gx[1].size() > 0)
                    dp[l][0][1][0][0] = gx[1][1 - 1] > l && l == 0 ? 1 : 0;
                if (gx[2].size() > 0)
                    dp[l][0][0][1][0] = gx[2][1 - 1] > l && l == 0 ? 1 : 0;
                if (gx[3].size() > 0)
                    dp[l][0][0][0][1] = gx[3][1 - 1] > l && l == 0 ? 1 : 0;
            }
            for (int kp = 2; kp <= xm; kp++) {
                for (int i = 0; i <= kp; i++) {
                    for (int j = 0; j + i <= kp; j++) {
                        for (int k = 0; k + j + i <= kp; k++) {
                            for (int l = 0; l < p; l++) {
                                int w = kp - i - j - k;
                                if (i > gx[0].size())
                                    continue;
                                if (j > gx[1].size())
                                    continue;
                                if (k > gx[2].size())
                                    continue;
                                if (w > gx[3].size())
                                    continue;
                                dp[l][i][j][k][w] = 0;
                                if (i >= 1)
                                    dp[l][i][j][k][w] =
                                        max(dp[l][i][j][k][w],
                                            dp[(l + 0) % p][i - 1][j][k][w] +
                                                (gx[0][i - 1] > l && l == 0 ? 1 : 0));
                                if (j >= 1)
                                    dp[l][i][j][k][w] =
                                        max(dp[l][i][j][k][w],
                                            dp[(l + 1) % p][i][j - 1][k][w] +
                                                (gx[1][j - 1] > l && l == 0 ? 1 : 0));
                                if (k >= 1)
                                    dp[l][i][j][k][w] =
                                        max(dp[l][i][j][k][w],
                                            dp[(l + 2) % p][i][j][k - 1][w] +
                                                (gx[2][k - 1] > l && l == 0 ? 1 : 0));
                                if (w >= 1)
                                    dp[l][i][j][k][w] =
                                        max(dp[l][i][j][k][w],
                                            dp[(l + 3) % p][i][j][k][w - 1] +
                                                (gx[3][w - 1] > l && l == 0 ? 1 : 0));
                                // dp[l][i][j][k][w] += l == 0;
                            }
                        }
                    }
                }
            }
            int ans =
                dp[0][gx[0].size()][gx[1].size()][gx[2].size()][gx[3].size()];
            // if (ans > (nsum - 1 + p) / p)
            //     ans = (nsum - 1 + p) / p;
            cout << "Case #" << it << ": " << ans << endl;
        }
    }
    return 0;
}
