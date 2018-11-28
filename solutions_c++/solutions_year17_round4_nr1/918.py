#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, P;
        cin >> N >> P;
        vector<int> G(N);
        for (int i = 0; i < N; i++) {
            cin >> G[i];
        }

        int result = 0;
        if (P == 2) {
            int odds = 0;
            for (int g : G) {
                if (g % 2 == 0) {
                    result++;
                } else {
                    if (odds % 2 == 0)
                        result++;
                    odds++;
                }
            }
        } else if (P == 3){
            vector<int> cnt(3, 0);
            for (int g : G) {
                cnt[g % 3]++;
            }

            vector<vector<vector<vector<int>>>> dp(101, vector<vector<vector<int>>>(101, vector<vector<int>>(101, vector<int>(4))));
            dp[0][0][0][0] = 0;
            dp[0][0][0][1] = -9999;
            dp[0][0][0][2] = -9999;
            dp[0][0][0][3] = -9999;

            for (int a = 0; a < 101; a++) {
                for (int b = 0; b < 101; b++) {
                    for (int c = 0; c < 101; c++) {
                        for (int rest = 0; rest < 3; rest++) {
                            if (a + b + c > 0) {
                                int best = -9999;
                                if (a) {
                                    best = max(best, dp[a-1][b][c][rest - 0] + (rest == 0));
                                }
                                if (b) {
                                    best = max(best, dp[a][b-1][c][(rest + 2) % 3] + (rest == 1));
                                }
                                if (c) {
                                    best = max(best, dp[a][b][c-1][(rest + 1) % 3] + (rest == 2));
                                }
                                dp[a][b][c][rest] = best;
                            }
                        }
                    }
                }
            }

            int best = -9999;
            for (int i = 0; i < 3; i++) {
                best = max(dp[cnt[0]][cnt[1]][cnt[2]][i], best);
            }
            result = best;
        } else {
            vector<int> cnt(4, 0);
            for (int g : G) {
                cnt[g % 4]++;
            }

            vector<vector<vector<vector<int>>>> dp(101, vector<vector<vector<int>>>(101, vector<vector<int>>(101, vector<int>(4))));
            dp[0][0][0][0] = 0;
            dp[0][0][0][1] = -9999;
            dp[0][0][0][2] = -9999;
            dp[0][0][0][3] = -9999;

            for (int a = 0; a < 101; a++) {
                for (int b = 0; b < 101; b++) {
                    for (int c = 0; c < 101; c++) {
                        for (int rest = 0; rest < 4; rest++) {
                            if (a + b + c > 0) {
                                int best = -9999;
                                if (a) {
                                    best = max(best, dp[a-1][b][c][(rest + 3) % 4] + (rest == 1));
                                }
                                if (b) {
                                    best = max(best, dp[a][b-1][c][(rest + 2) % 4] + (rest == 2));
                                }
                                if (c) {
                                    best = max(best, dp[a][b][c-1][(rest + 1) % 4] + (rest == 3));
                                }
                                dp[a][b][c][rest] = best;
                            }
                        }
                    }
                }
            }

            int best = -9999;
            for (int i = 0; i < 4; i++) {
                best = max(dp[cnt[1]][cnt[2]][cnt[3]][i], best);
            }
            result = best + cnt[0];

        }
        

        cout << "Case #" << t << ": " << result;
        cout << '\n';
    }
    
}
