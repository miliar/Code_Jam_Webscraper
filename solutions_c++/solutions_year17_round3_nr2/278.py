#include <bits/stdc++.h>

using namespace std;

const int MX_SZ = 1440 + 5;
const int TM = 720;
int dp[MX_SZ][MX_SZ][2][2]; //[time][Cameron_time][if_Cameron][if_Cameron_starts]
const int INF = 1e+9 + 42;

void init() {
    for (int i = 0; i < MX_SZ; ++i) {
        for (int j = 0; j < MX_SZ; ++j) {
            for (int k = 0; k < 2; ++k) {
                for (int l = 0; l < 2; ++l) {
                    dp[i][j][k][l] = INF;
                }
            }
        }
    }
}

void solve(int t) {
    init();
    int a, b;
    cin >> a >> b;
    vector<pair<bool, bool>> now[MX_SZ]; //{if_opening, if_Cameron}
    for (int i = 0; i < a; ++i) {
        int l, r;
        cin >> l >> r;
        now[l].push_back({true, true});
        now[r].push_back({false, true});
    }
    for (int i = 0; i < b; ++i) {
        int l, r;
        cin >> l >> r;
        now[l].push_back({true, false});
        now[r].push_back({false, false});
    }
    for (int i = 0; i < MX_SZ; ++i) {
        sort(now[i].begin(), now[i].end());
    }
    bool c = true, j = true;
    for (int i = 0; i < MX_SZ; ++i) {
        for (auto x : now[i]) {
            if (x.first) {
                if (x.second) c = false;
                else j = false;
            } else {
                if (x.second) c = true;
                else j = true;
            }
        }
        if (i == 0) {
            if (c) dp[0][1][1][1] = 0;

            if (j) dp[0][0][0][0] = 0;
        } else {
            for (int c_time = 0; c_time < MX_SZ; ++c_time) {
                for (int fr = 0; fr < 2; ++fr) {
                    if (c and c_time != 0) {
                        dp[i][c_time][1][fr] = min(dp[i - 1][c_time - 1][1][fr],
                                                dp[i - 1][c_time - 1][0][fr] + 1);
                    }
                    if (j) {
                        dp[i][c_time][0][fr] = min(dp[i - 1][c_time][0][fr],
                                                   dp[i - 1][c_time][1][fr] + 1);

                    }
                }
            }
        }
    }

    int ans = min(min(dp[TM * 2 - 1][TM][0][0], dp[TM * 2 - 1][TM][0][1] + 1),
                  min(dp[TM * 2 - 1][TM][1][1], dp[TM * 2 - 1][TM][1][0] + 1));

    cout << "Case #" << t << ": " << ans << endl;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
}
