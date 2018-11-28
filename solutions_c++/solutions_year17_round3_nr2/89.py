#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 207;
const int INF = 720 * 2;

int tc, n, m;
pair<int, int> a[MAX_N], b[MAX_N];
pair<int, int> c[10000];
int col[INF];
int dp[INF + 1][721][2];

int main() {
    freopen("B.in", "r", stdin);
    freopen("B2.out", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            cin >> a[i].first >> a[i].second;
        }
        for (int i = 0; i < m; i++) {
            cin >> b[i].first >> b[i].second;
        }
        sort(a, a + n);
        sort(b, b + m);
        int pos1 = 0;
        int pos2 = 0;
        int ti = 0;
        int cnt = 0;
        while (ti != INF) {
            if (pos1 != n && ti == a[pos1].first) {
                c[cnt++] = {a[pos1].second - a[pos1].first, 0};
                ti = a[pos1].second;
                pos1++;
                continue;
            }
            if (pos2 != m && ti == b[pos2].first) {
                c[cnt++] = {b[pos2].second - b[pos2].first, 1};
                ti = b[pos2].second;
                pos2++;
                continue;
            }
            int nx = INF;
            if (pos1 != n) {
                nx = min(nx, a[pos1].first);
            }
            if (pos2 != m) {
                nx = min(nx, b[pos2].first);
            }
            c[cnt++] = {nx - ti, 2};
            ti = nx;
        }
        int pos = 0;
        for (int i = 0; i < cnt; i++) {
            for (int j = 0; j < c[i].first; j++) {
                col[pos] = c[i].second;
                pos++;
            }
        }
        for (int i = 0; i <= INF; i++) {
            for (int j = 0; j <= 720; j++) {
                dp[i][j][0] = INF;
                dp[i][j][1] = INF;
            }
        }
        dp[0][0][0] = 0;
        dp[0][0][1] = 0;
        for (int i = 0; i < INF; i++) {
            for (int j = 0; j <= 720; j++) {
                if (col[i] == 0 || col[i] == 2) {
                    if (j + 1 <= 720) {
                        dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][0]);
                        dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][1] + 1);
                    }
                }
                if (col[i] == 1 || col[i] == 2) {
                    dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][0] + 1);
                    dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][1]);
                }
            }
        }
        if (dp[INF][720][0] % 2 == 1) {
            dp[INF][720][0]++;
        }
        if (dp[INF][720][1] % 2 == 1) {
            dp[INF][720][1]++;
        }
        cout << min(dp[INF][720][0], dp[INF][720][1]) << "\n";
    }
}

