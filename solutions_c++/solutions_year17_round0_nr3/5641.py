#include <cstdio>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <cmath>
using namespace std;

class foo {
  public:
    int l;
    int r;
    foo(int _l, int _r):l(_l), r(_r) {}
    bool operator<(const foo& f) const {
        int d1 = r - l;
        int d2 = f.r - f.l;
        if (d1 == d2) {
            if (l == f.l) return r > f.r;
            else l > f.l;
        }
        return d1 < d2;
    }
};
priority_queue<foo> pfq;

int main() {
    int tt, n, k;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        scanf("%d%d", &n, &k);
        while (!pfq.empty()) pfq.pop();
        foo f(1, n);
        pfq.push(f);
        int lx, rx;
        while (!pfq.empty() && k--) {
            foo x = pfq.top();
            int l = x.l, r = x.r;
            pfq.pop();
            int mid = (l + r) / 2;
            foo f1(l, mid - 1); foo f2(mid + 1, r);
            lx = mid - l; rx = r - mid;
            pfq.push(f1); pfq.push(f2);
        }
        printf("Case #%d: %d %d\n", t, max(lx, rx), min(lx, rx));
    }
    return 0;
}
