#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int N = 1000;
const double pi = acos(-1.0);

struct Pancake {
    long long r, h;
    bool operator<(const Pancake &other) const {
        return r * h > other.r * other.h;
    }
} p[N];

template<typename T>
T sqr(T x) {
    return x * x;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, n, k;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++ cas) {
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; ++ i) {
            scanf("%lld%lld", &p[i].r, &p[i].h);
        }
        sort(p, p + n);
        double ans = 0;
        for (int i = 0; i < n; ++ i) {
            double tmp = pi * sqr(p[i].r) + 2 * pi * (p[i].r * p[i].h);
            int cnt = k - 1;
            for (int j = 0; j < n && cnt > 0; ++ j) {
                if (i != j && p[j].r <= p[i].r) {
                    tmp += 2 * pi * (p[j].r * p[j].h);
                    -- cnt;
                }
            }
            ans = max(ans, tmp);
        }
        printf("Case #%d: %f\n", cas, ans);
    }
    return 0;
}
