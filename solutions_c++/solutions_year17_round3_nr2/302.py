#include <bits/stdc++.h>
#define int long long
#define double long double
#define eps 1e-9
#define inf 1e4
#define fs first
#define sc second
#define pi acos(-1)

using namespace std;

int tc[1442];
int tj[1442];
int dp[24 * 60 + 2][728][2][2];

void solve(int X) {
    int N, K;
    cin >> N >> K;
    memset(tc, 0, sizeof(tc));
    int x, y;
    for (int i = 0; i < N; i++) {
        cin >> x >> y;
        tc[x] += 1;
        tc[y] -= 1;
    }
    memset(tj, 0, sizeof(tj));
    for (int i = 0; i < K; i++) {
        cin >> x >> y;
        tj[x] += 1;
        tj[y] -= 1;
    }

    for (int i = 1; i < 24 * 60 + 2; i++) {
        tc[i] += tc[i - 1];
        tj[i] += tj[i - 1];
    }


    for (int i = 0; i < 24 * 60 + 2; i++) {
        for (int j = 0; j < 721; j++) {
            for (int c = 0; c < 2; c++) {
                dp[i][j][0][c] = dp[i][j][1][c] = inf;
            }
        }
    }
    if (!tc[0]) {
        dp[0][1][0][0] = 0;
    }
    if (!tj[0]) {
        dp[0][0][1][1] = 0;
    }

    for (int i = 1; i < 1440; i++) {
        for (int j = 0; j <= 12 * 60; j++) {
            for (int c = 0; c < 2; c++) {
                if (j && !tc[i]) {
                    dp[i][j][0][c] = min(dp[i - 1][j - 1][0][c], dp[i][j][0][c]);
                    dp[i][j][0][c] = min(dp[i - 1][j - 1][1][c] + 1, dp[i][j][0][c]);
                }
                if (!tj[i]) {
                    dp[i][j][1][c] = min(dp[i - 1][j][1][c], dp[i][j][1][c]);
                    dp[i][j][1][c] = min(dp[i - 1][j][0][c] + 1, dp[i][j][1][c]);
                }
            }
        }
    }
    cout << "Case #" << X << ':' << ' ';
    cout << min(min(dp[1439][720][1][1], dp[1439][720][1][0] + 1), min(dp[1439][720][0][0], dp[1439][720][0][1] + 1));
    cout << '\n';
}


signed main() {
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 1;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
    return 0;
}

