#include <algorithm>
#include <cstdio>
#include <cstring>

#define DEBUG(...) fprintf(stderr, __VA_ARGS__)

int m, dp[4][101][101][101];

int solve(int now, int a, int b, int c)
{
    if (a == 0 && b == 0 && c == 0) {
        return 0;
    }
    int& ref = dp[now][a][b][c];
    if (ref == -1) {
        ref = 0;
        if (a) {
            ref = std::max(ref, solve((now + 1) % m, a - 1, b, c));
        }
        if (b) {
            ref = std::max(ref, solve((now + 2) % m, a, b - 1, c));
        }
        if (c) {
            ref = std::max(ref, solve((now + 3) % m, a, b, c - 1));
        }
        ref += (now == 0);
    }
    return ref;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++ t) {
        DEBUG("Test %d\n", t);
        int n;
        scanf("%d%d", &n, &m);
        int cnt[4];
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < n; ++ i) {
            int a;
            scanf("%d", &a);
            cnt[a % m] ++;
        }
        memset(dp, -1, sizeof(dp));
        printf("Case #%d: %d\n", t, solve(0, cnt[1], cnt[2], cnt[3]) + cnt[0]);
    }
}
