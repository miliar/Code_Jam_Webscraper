#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;

typedef pair<int, int> pii;
const int maxn = 1000 + 5;
int cntp[maxn];
int cntb[maxn];
int n, c, m;

int sum[maxn];
bool check(int x) {
    for (int i = 1; i <= n; i++) {
        if (sum[i] > i * x) return false;
    }
    return true;
}

int main() {
    int T; scanf("%d", &T);
    for (int Cas = 1; Cas <= T; Cas++) {
        memset(cntp, 0, sizeof(cntp));
        memset(cntb, 0, sizeof(cntb));
        scanf("%d%d%d", &n, &c, &m);
        int mxb = 0;
        int res = 0, cnt_op = 0;
        for (int i = 1; i <= m; i++) {
            int p, b; scanf("%d%d", &p, &b);
            cntp[p]++; cntb[b]++;
            mxb = max(cntb[b], mxb);
            res = max(cntp[p], res);
        }
        for (int i = 1; i <= n; i++) {
            sum[i] = sum[i-1] + cntp[i];
        }
        int l = mxb, r = m;
        // while(l < r - 1) {
            // int mid = (l + r) / 2;
            // if (check(mid)) r = mid;
            // else l = mid;
        // }
        while(l < r) {
            int mid = (l + r) / 2;
            if (check(mid)) r = mid;
            else l = mid + 1;
        }
        res = r;
        for (int i = 1; i <= n; i++) {
            cnt_op += max(0, cntp[i] - res);
        }
        printf("Case #%d: %d %d\n", Cas, res, cnt_op);
    }
    return 0;
}
