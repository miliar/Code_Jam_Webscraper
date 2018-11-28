#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
typedef long long ll;
const double PI = acos(-1.0);
const int maxn = 1010;

struct Pan {
    int h, r;
    bool operator<(const Pan& rhs) const {
        return (ll) h * r > (ll) rhs.h * rhs.r;
    }
} p[maxn];

int main() {
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ca++) {
        int N, K;
        scanf("%d%d", &N, &K);
        for (int i = 0; i < N; i++) scanf("%d%d", &p[i].r, &p[i].h);
        sort(p, p + N);
        int R = 0;
        double ans = 0;
        for (int i = 0; i < K - 1; i++) {
            R = max(R, p[i].r);
            ans += 2.0 * PI * p[i].r * p[i].h;
        }
        double t = 0;
        for (int i = K - 1; i < N; i++) {
            int r = max(R, p[i].r);
            double t1 = PI * r * r + 2.0 * PI * p[i].r * p[i].h;
            t = max(t, t1);
        }
        printf("Case #%d: %.8lf\n", ca, ans + t);
    }
    return 0;
}