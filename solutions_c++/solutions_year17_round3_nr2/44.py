#include <algorithm>
#include <cstdio>
#include <cstring>

const int N = 12 * 60;

int belong[2 * N], dp[2][N + 1][2];

void update(int& x, int a)
{
    if (x == -1) {
        x = a;
    } else {
        x = std::min(x, a);
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++ t) {
        memset(belong, -1, sizeof(belong));
        int count[2];
        scanf("%d%d", count, count + 1);
        for (int i = 0; i < 2; ++ i) {
            for (int j = 0; j < count[i]; ++ j) {
                int a, b;
                scanf("%d%d", &a, &b);
                for (int k = a; k < b; ++ k) {
                    belong[k] = i;
                }
            }
        }
        int result = -1;
        for (int first = 0; first < 2; ++ first) {
            if (belong[0] == (first ^ 1)) {
                continue;
            }
            memset(dp, -1, sizeof(dp));
            dp[0][first == 1][first] = 0;
            for (int i = 1; i < 2 * N; ++ i) {
                memset(dp[i & 1], -1, sizeof(dp[i & 1]));
                for (int cnt = 0; cnt <= i && cnt <= N; ++ cnt) {
                    for (int last = 0; last < 2; ++ last) {
                        if (dp[i + 1 & 1][cnt][last] == -1) {
                            continue;
                        }
                        for (int next = 0; next < 2; ++ next) {
                            if (belong[i] == (next ^ 1)) {
                                continue;
                            }
                            int new_cnt = cnt + (next == 1);
                            if (new_cnt <= N) {
                                update(dp[i & 1][new_cnt][next], dp[i + 1 & 1][cnt][last] + (last != next));
                            }
                        }
                    }
                }
            }
            for (int last = 0; last < 2; ++ last) {
                int& ref = dp[2 * N + 1 & 1][N][last];
                if (ref != -1) {
                    update(result, ref + (first != last));
                }
            }
        }
        printf("Case #%d: %d\n", t, result);
    }
}
