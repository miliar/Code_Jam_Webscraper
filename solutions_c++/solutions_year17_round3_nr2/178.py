#include <iostream>
#include <cmath>
#include <iomanip>
#include <cstring>
#include <algorithm>

using namespace std;

bool covered[2][1444];

const int INF = 0x7f7f7f7f;

int solve2(const int start) {
    int dp[2][722][2] = {};
    int cur = 1, prv = 0;

    memset(dp, 0x7f, sizeof dp);
    dp[prv][(start == 0) ? 1 : 0][start] = 0;

    for (int i=1; i<1440; ++i) {
        memset(dp[cur], 0x7f, sizeof dp[cur]);

        for (int who=0; who<2; ++who) {
            if (covered[who][i])
                continue;
            for (int prvwork=0; prvwork<=720; ++prvwork) {
                for (int prvwho=0; prvwho<2; ++prvwho) {
                    if (dp[prv][prvwork][prvwho] == INF)
                        continue;
                    int exchange = who == prvwho ? 0 : 1;
                    if (i + 1 == 1440)
                        if (who != start)
                            ++exchange;
                    int work = prvwork + (who == 0 ? 1 : 0);
                    if (work > 720)
                        continue;
                    if (i + 1 - work > 720)
                        continue;
                    dp[cur][work][who] = min(dp[cur][work][who], dp[prv][prvwork][prvwho] + exchange);
                }
            }
        }

        swap(cur, prv);
    }

    return min(dp[prv][720][0], dp[prv][720][1]);
}


void solve(const int e) {
    cout << "Case #" << e << ": ";

    int activities[2]; cin >> activities[0] >> activities[1];

    memset(covered, 0, sizeof covered);
    for (int p=0; p<2; ++p) {
        for (int i=0; i<activities[p]; ++i) {
            int from, to; cin >> from >> to;
            for (int u=from; u<to; ++u)
                covered[p][u] = true;
        }
    }

    int ans = INF;

    for (int start=0; start<2; ++start) {
        if (covered[start][0])
            continue;
        ans = min(ans, solve2(start));
    }

    cout << ans << endl;
}

int main() {
    int t; cin >> t;
    for (int e=1; e<=t; ++e)
        solve(e);
}

