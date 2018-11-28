#include <bits/stdc++.h>

using namespace std;

int sum[1005];

int seat[1005];

int minX;

int n, c, m;

bool check(int M) {
    int tot = 0;
    for (int i = 1; i <= n; ++ i) {
        tot += M;
        if (seat[i] > tot)
            return false;
        tot -= seat[i];
    }
    minX = 0;
    for (int i = n; i >= 1; -- i) {
        if (seat[i] > M)
            minX += seat[i] - M;
    }
    return true;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d%d", &n, &c, &m);
        memset(sum, 0, sizeof(sum));
        memset(seat, 0, sizeof(seat));
        int l = 0, r = m;
        for (int i = 0; i < m; ++ i) {
            int x, y;
            scanf("%d%d", &x, &y);
            ++ sum[y];
            ++ seat[x];
        }
        for (int i = 1; i <= c; ++ i)
            l = max(l, sum[i]);
        int ret;
        while (l <= r) {
            int m = (l + r) >> 1;
            if (check(m)) {
                ret = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        check(ret);
        printf("Case #%d: %d %d\n", cas, ret, minX);
    }
    return 0;
}
