#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int shift3[3][3] = {{-2, 1, 0},
                    { 1,-2, 0},
                    {-1,-1, 1}};
int shift4[6][4] = {{-2, 1, 0},
                    {-1,-1, 1, 0},
                    {-1, 0,-1, 1},
                    { 0,-2, 0, 1},
                    { 1,-1,-1, 0},
                    { 0, 1,-2, 0}};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    const int size = 101;
    vector<vector<vector<int>>> dp(size, vector<vector<int>>(size, vector<int>(size)));
    for (int testCase = 0; testCase < T; ++testCase) {
        int n, p;
        int cnt[4] = {0, 0, 0, 0};
        int total = 0;

        cin >> n >> p;
        for (int i = 0; i < n; ++i) {
            int cur;
            cin >> cur;
            ++cnt[cur % p];
            total += cur;
        }
        //cout << cnt[1] << " " << cnt[2] << " " << cnt[3] << endl;
        int ans = 0;
        if (p == 2) {
            ans = cnt[0] + cnt[1] / 2 + cnt[1] % 2;
        } else if (p == 3) {
            dp[0][0][0] = cnt[0];
            dp[1][0][0] = cnt[0];
            dp[0][1][0] = cnt[0];
            int max_sum = cnt[1] + cnt[2] + cnt[3];
            for (int sum = 2; sum <= max_sum; ++sum) {
                for (int a = 0; a <= sum; ++a) {
                    int b = sum - a;
                    dp[a][b][0] = cnt[0];
                    for (int sh = 0; sh < 3; ++sh) {
                        int na = a + shift3[sh][0];
                        int nb = b + shift3[sh][1];
                        if (na >= 0 && nb >= 0) {
                            dp[a][b][0] = max(dp[a][b][0],
                                              dp[na][nb][0] + shift3[sh][2]);
                        }
                    }
                    //cout << "dp[" << a << "][" << b << "] = " << dp[a][b][0] << endl;
                }
            }
            ans = dp[cnt[1]][cnt[2]][cnt[3]];
            if (total % p > 0) {
                ans++;
            }
        } else { // if (p == 4) {
            dp[0][0][0] = cnt[0];
            dp[1][0][0] = cnt[0];
            dp[0][1][0] = cnt[0];
            dp[0][0][1] = cnt[0];
            int max_sum = cnt[1] + cnt[2] + cnt[3];
            for (int sum = 2; sum <= max_sum; ++sum) {
                for (int a = 0; a <= sum; ++a) {
                    for (int b = 0; b <= sum - a; ++b) {
                        int c = sum - a - b;
                        dp[a][b][c] = cnt[0];
                        for (int sh = 0; sh < 6; ++sh) {
                            int na = a + shift4[sh][0];
                            int nb = b + shift4[sh][1];
                            int nc = c + shift4[sh][2];
                            if (na >= 0 && nb >= 0 && nc >= 0) {
                                dp[a][b][c] = max(dp[a][b][c],
                                                  dp[na][nb][nc] + shift4[sh][3]);
                            }
                        }
                        //cout << "dp[" << a << "][" << b << "][" << c << "] = " << dp[a][b][c] << endl;
                    }
                }
            }
            ans = dp[cnt[1]][cnt[2]][cnt[3]];
            if (total % p > 0) {
                ans++;
            }
        }

        cout << "Case #" << testCase + 1 << ": " << ans << endl;
    }
    return 0;
}
