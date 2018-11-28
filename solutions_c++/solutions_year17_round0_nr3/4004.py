#include <iostream>
#include <queue>
using namespace std;
struct data {
    int length, x, y;
    bool operator<(const data &a) const {
        if (length != a.length) {
            return length < a.length;
        }
        return x < a.x;
    }
};
int main() {
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int n, k;
        scanf("%d%d", &n, &k);
        priority_queue<data> pq;
        pq.push({n, 1, n});
        for (int i = 1; i <= k; ++i) {
            data a = pq.top();
            pq.pop();
            int s = (a.length - 1) / 2 + a.x;
            int ls = s - a.x;
            int rs = a.y - s;
            if (i == k) {
                printf("Case #%d: %d %d\n", ca, max(ls, rs), min(ls, rs));
            }
            if (ls) {
                pq.push({ls, a.x, s - 1});
            }
            if (rs) {
                pq.push({rs, s + 1, a.y});
            }
        }
    }
    return 0;
}
