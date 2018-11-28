#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <iomanip>

using namespace std;

const double PI = atan(1) * 4;

bool sc[1440], sj[1440];

const int INF = 1 << 28;
int dp[2][1500][1000];
int vis[2][1500][1000];

int doit(int p, int time, int c) {
    if (c < 0) return INF;
    if (time < 0) return INF;
    if (vis[p][time][c]) return dp[p][time][c];
    vis[p][time][c] = true;
    if (p == 0 && sc[time - 1]) return INF;
    if (p == 1 && sj[time - 1]) return INF;
    return dp[p][time][c] = min(doit(p, time - 1, c - p), 1 + doit(1 - p, time - 1, c - p));
}

void solve() {
    int ac, aj;
    cin >> ac >> aj;
    for (int i = 0; i < 1440; i++) {
        sc[i] = false;
        sj[i] = false;
    }
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 1500; j++) {
            for (int k = 0; k < 1000; k++) {
                dp[i][j][k] = INF;
                vis[i][j][k] = false;
            }
        }
    }
    for (int i = 0; i < ac; i++) {
        int l, r;
        cin >> l >> r;
        for (int j = l; j < r; j++) {
            sc[j] = true;
        }
    }
    for (int i = 0; i < aj; i++) {
        int l, r;
        cin >> l >> r;
        for (int j = l; j < r; j++) {
            sj[j] = true;
        }
    }

    dp[0][0][0] = 0;
    dp[1][0][0] = 0;
    vis[0][0][0] = true;
    vis[1][0][0] = true;

    int ans = min(doit(0, 1440, 720), doit(1, 1440, 720));
    if (ans % 2 == 1) ans++;
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}