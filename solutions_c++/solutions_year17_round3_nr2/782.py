#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>

#define mp make_pair
#define pb push_back

using namespace std;

typedef pair<int, int> pii;

const int MAXN = 2000;
const int inf = 1e9;
int shift[24 * 60 + 1];
int dp[24 * 60 + 1][12 * 60 + 2][2][2];

int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int q;
    cin >> q;
    cout.precision(20);
    for (int t = 0; t < q; t++) {

        for (int i = 0; i < 24 * 60 + 1; i++)
            for (int j = 0; j < 12 * 60 + 1; j++)
                for (int i1 = 0;  i1 < 2; i1++)
                    for (int j1 = 0; j1 < 2; j1++)
                        dp[i][j][i1][j1] = inf;
        for (int i = 0; i < 24 * 60 + 1; i++)
            shift[i] = 0;

        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            int l, r;
            cin >> l >> r;
            for (int j = l; j < r; j++)
                shift[j] = 2;
        }
        for (int i = 0; i < m; i++) {
            int l, r;
            cin >> l >> r;
            for (int j = l; j < r; j++)
                shift[j] = 1;
        }

        if (shift[0] == 0) {
            dp[0][1][0][0] = 0;
            dp[0][0][1][1] = 0;
        } else {
            if (shift[0] == 1)
                dp[0][1][0][0] = 0;
            else
                dp[0][0][1][1] = 0;
        }
        //shift[24 * 60] = shift[0];

        for (int i = 0; i < 24 * 60; i++)
            for (int j = 0; j < 12 * 60 + 1; j++)
                for (int i1 = 0; i1 < 2; i1++)
                    for (int j1 = 0; j1 < 2; j1++) {
                        if (dp[i][j][i1][j1] == inf)
                            continue;
                        if (shift[i + 1] == 0) {
                            if (j1 == 0) {
                                dp[i + 1][j][i1][1] = min(dp[i + 1][j][i1][1],
                                                          dp[i][j][i1][j1] + 1);
                                    dp[i + 1][j + 1][i1][0] = min(dp[i + 1][j + 1][i1][0],
                                                              dp[i][j][i1][j1]);
                            } else {
                                dp[i + 1][j + 1][i1][0] = min(dp[i + 1][j + 1][i1][0],
                                                          dp[i][j][i1][j1] + 1);
                                dp[i + 1][j][i1][1] = min(dp[i + 1][j][i1][1],
                                                              dp[i][j][i1][j1]);
                            }

                        } else {
                            int t1 = j;
                            if (shift[i + 1] != j1 + 1) {
                                if (j1 == 1)
                                    t1++;
                                dp[i + 1][t1][i1][shift[i + 1] - 1] = min(dp[i + 1][t1][i1][shift[i + 1] - 1],
                                                                          dp[i][j][i1][j1] + 1);
                            } else {
                                if (j1 == 0)
                                    t1++;
                                dp[i + 1][t1][i1][shift[i + 1] - 1] = min(dp[i + 1][t1][i1][shift[i + 1] - 1],
                                                                          dp[i][j][i1][j1]);
                            }
                        }
                    }
        int ans = inf;
        ans = min(ans, dp[24 * 60 - 1][12 * 60][0][0]);
        ans = min(ans, dp[24 * 60 - 1][12 * 60][1][1]);
        ans = min(ans, dp[24 * 60 - 1][12 * 60][0][1] + 1);
        ans = min(ans, dp[24 * 60 - 1][12 * 60][1][0] + 1);

        cout << "Case #" << t + 1 << ": " << ans << "\n";
    }

    return 0;
}