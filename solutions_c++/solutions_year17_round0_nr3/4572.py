#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
using namespace std;

typedef long long LL;
struct on {
        LL l, r, p;
        on (LL _l, LL _r, LL _p) : l(_l), r(_r), p(_p) {}
        bool operator < (const on &A) const {
                return r < A.r;
        }
};
priority_queue<on> que;

int main () {
//        freopen ("in.txt", "r", stdin);
//        freopen ("out.txt", "w", stdout);
        int T;
        scanf ("%d", &T);
        for (int cas = 1; cas <= T; cas++) {
                LL n, m, k;
                scanf ("%lld%lld", &n, &k);
                while (!que.empty())    que.pop();
                que.push (on (1, n, 1));
                LL now = 0;
                while (!que.empty()) {
                        on tmp = que.top();
                        que.pop();
                        LL l = tmp.l, r = tmp.r;
                        if (now + tmp.p >= k) {
                                printf ("Case #%d: %lld %lld\n", cas, max (r - ((l + r) / 2), (l + r) / 2 - l), min (r - ((l + r) / 2), (l + r) / 2 - l));
                                break;
                        }
                        now += tmp.p;
                        LL mid = (l + r) / 2;
                        if (r - mid == mid - l) {
                                if (mid - 1 >= 1)
                                        que.push (on(1, mid - 1, tmp.p * 2));
                        } else {
                                if (mid >= 1)
                                        que.push (on(1, mid, tmp.p));
                                if (mid - 1 >= 1)
                                        que.push (on(1, mid - 1, tmp.p));
                        }
                }
        }
        return 0;
}
