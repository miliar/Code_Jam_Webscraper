#include <iostream>
#include <vector>

using namespace std;

struct Seg {
    int l, r;
    int type;


    Seg(int l, int r, int type) : l(l), r(r), type(type) { }
};

bool cmp(Seg &a, Seg &b) {
    return a.l < b.l;
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        cerr << tt << endl;
        int ac, aj;
        cin >> ac >> aj;

        vector<int> a(1440, -1);
        for (int i = 0; i < ac; i++) {
            int l, r;
            cin >> l >> r;
            for (int j = l; j < r; j++) {
                a[j] = 0;
            }
        }
        for (int i = 0; i < aj; i++) {
            int l, r;
            cin >> l >> r;
            for (int j = l; j < r; j++) {
                a[j] = 1;
            }
        }

        const int INF = 1000000000;
        int best = INF;

        for (int frst = 0; frst < 2; frst++) {
            vector<vector<vector<int>>> dp(2, vector<vector<int>>(1440, vector<int>(721, INF)));
            int j0 = 0;
            if (frst == 0) {
                j0 = 1;
            }
            dp[frst][0][j0] = 0;
            for (int i = 0; i + 1 < 1440; i++) {
                for (int j = 0; j < 721; j++) {
                    for (int last = 0; last < 2; last++) {
                        if (dp[last][i][j] == INF) continue;
                        for (int nxt = 0; nxt < 2; nxt++) {
                            int j1 = j;
                            if (nxt == 0) {
                                j1++;
                            }
                            int pen = 0;
                            if (nxt != last) {
                                pen++;
                            }
                            if (i + 1 == 1440 - 1 && nxt != frst) {
                                pen++;
                            }
                            if (a[i] != -1 && a[i] != nxt) {
                                continue;
                            }

                            dp[nxt][i + 1][j1] = min(dp[nxt][i + 1][j1], dp[last][i][j] + pen);
                        }
                    }
                }
            }

            best = min(best, dp[0][1440 - 1][720]);
            best = min(best, dp[1][1440 - 1][720]);
        }

        cout << "Case #" << tt << ": " << best << endl;
    }

    return 0;
}