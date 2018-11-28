#include <bits/stdc++.h>
using namespace std;

struct Interval {
    int interval;
    int l, r;
    Interval(int _l, int _r) : l(_l), r(_r) {
        interval = r - l + 1;
    }
};

bool operator < (const Interval& lhs, const Interval& rhs) {
    if (lhs.interval != rhs.interval)
        return lhs.interval < rhs.interval;
    return lhs.l > rhs.l;
}

int main() {
    freopen("C-output.txt", "w", stdout);
    int T;
    scanf("%d", &T);

    for (int testcase = 1; testcase <= T; testcase++) {
        int N, K;
        scanf("%d %d", &N, &K);

        priority_queue<Interval> q;
        q.push(Interval(1, N));

        int y, z;
        for (int i = 0; i < K; i++) {
            Interval curr = q.top(); q.pop();
            int l = curr.l, r = curr.r;
            int mid = l + (r - l) / 2;
            y = r - mid;
            z = mid - l;
            if (l <= mid - 1) {
                q.push(Interval(l, mid - 1));
            }
            if (mid + 1 <= r) {
                q.push(Interval(mid + 1, r));
            }
        }
        printf("Case #%d: %d %d\n", testcase, y, z);
    }
}
