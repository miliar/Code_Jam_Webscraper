#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef __int64 lld;

lld dp[20][10];
int bit[20];
lld n;

lld dfs(int len, int last, int fp) {
    if (len == 0) {
        return 1;
    }
    if (!fp && dp[len][last] != -1) {
        return dp[len][last];
    }
    int _max = (fp == 1 ? bit[len] : 9);
    lld ret = 0;
    for (int i = 0; i <= _max; ++i) {
        if (i >= last) {
            ret += dfs(len - 1, i, fp && i == _max);
        }
    }
    if (!fp) {
        dp[len][last] = ret;
    }
    return ret;
}

lld calc(lld x) {
    memset(bit, 0, sizeof(bit));
    int len = 0;
    while (x) {
        bit[++ len] = x % 10;
        x /= 10;
    }
    return dfs(len, 0, 1);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B1.out", "w", stdout);
    memset(dp, -1, sizeof(dp));
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%I64d", &n);
        lld l = 1, r = n;
        while (r >= l) {
            lld mid = l + r >> 1;
            if (calc(mid) == calc(n)) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        printf("Case #%d: ", cas);
        printf("%I64d\n", r + 1);
    }
    return 0;
}
