#include <bits/stdc++.h>

const int N = 200 + 10;
const int T = 24 * 60 + 10;
const int INF = 1 << 29;

struct Data {
    int start, end, id;

    Data(int s = 0, int e = 0, int i = 0) : start(s), end(e), id(i) {}

    bool operator < (const Data& other) const {
        return start < other.start;
    }

} data[N];

int dp[T][T / 2][2], n, m, total;

int main() {
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; ++ t) {
        scanf("%d%d", &n, &m);
        total = 0;
        for (int i = 1; i <= n; ++ i) {
            int x, y;
            scanf("%d%d", &x, &y);
            data[++ total] = Data(x, y, 0);
        }
        for (int i = 1; i <= m; ++ i) {
            int x, y;
            scanf("%d%d", &x, &y);
            data[++ total] = Data(x, y, 1);
        }
        std::sort(data + 1, data + total + 1);

        int answer = INF;
        for (int begin = 0; begin <= 1; ++ begin) {
            memset(dp, 60, sizeof(dp));
            dp[0][0][begin] = 0;
            for (int moment = 1, id = 1; moment <= 24 * 60; ++ moment) {
                while (id <= total && data[id].end < moment) id ++;

                int current = -1;
                if (id <= total && data[id].start < moment && moment <= data[id].end) {
                    current = data[id].id;
                }
                for (int a = 0; a <= moment; ++ a) {
                    if (a > 12 * 60 || moment - a > 12 * 60) continue;
                    for (int now = 0; now <= 1; ++ now) {
                        for (int prev = 0; prev <= 1; ++ prev) {
                            if (prev == current) continue;
                            if (a == 0 && prev == 0) continue;
                            if (a == moment && prev == 1) continue;
                            dp[moment][a][now] = std::min(dp[moment][a][now], dp[moment - 1][a - (prev == 0)][prev] + (now != prev));
                        }
                    }
                }
            }
            answer = std::min(answer, dp[24 * 60][12 * 60][begin]);
            answer = std::min(answer, dp[24 * 60][12 * 60][begin ^ 1] + 1);
        }
        printf("Case #%d: %d\n", t, answer);
    }
    return 0;
}