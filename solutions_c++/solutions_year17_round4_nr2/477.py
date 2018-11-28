#include <bits/stdc++.h>
using namespace std;
const int N = 1024;
int num[N];
int sum[N];
int per[N];
int n, m, c;

bool judge(int mid) {
    for (int i = 1; i <= c; ++ i) {
        if (mid * i < sum[i]) return false;
    }
    return true;
}

int cal(int x) {
    int ret = 0;
    for (int i = 1; i <= c; ++ i) {
        ret += max(0, num[i] - x);
        //printf("%d\n", num[i] - x);
    }
    return ret;
}

int main() {
    int T, x, y;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d%d", &c, &n, &m);
        memset(num, 0, sizeof num);
        memset(sum, 0, sizeof sum);
        memset(per, 0, sizeof per);
        for (int i = 0; i < m; ++ i) {
            scanf("%d%d", &x, &y);
            num[x] ++;
            per[y] ++;
        }
        for (int i = 1; i <= c; ++ i) {
            sum[i] = sum[i - 1] + num[i];
        }
        int l = 0;
        for (int i = 1; i <= n; ++ i) {
            l = max(l, per[i]);
        }
        int r = m;
        //printf("%d\n", l);
        while (l <= r) {
            int mid = (l + r) >> 1;
            if (judge(mid)) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        //printf("%d\n", l);
        printf("Case #%d: %d %d\n", cas, l, cal(l));
    }
    return 0;
}
