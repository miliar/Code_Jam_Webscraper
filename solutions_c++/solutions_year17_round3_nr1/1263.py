#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <iostream>

using namespace std;

#define DEBUG(x) cout<<#x<<":"<<x<<endl

typedef long long ll;
const int MAXN = 1024;
const double PI = atan(1.0) * 4.0;

struct Cake {
    ll r, h;
    bool operator < (const Cake &oth) const {
        return r * h > oth.r * oth.h;
    }
}cake[MAXN];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        int n, k;
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; ++i) {
            scanf("%lld%lld", &cake[i].r, &cake[i].h);
        }
        sort(cake, cake + n);
        double ans = 0.0;
        double sum = 0.0;
        ll max_r = 0;
        for (int i = 0; i < k - 1; ++i) {
            sum += 2.0 * PI * cake[i].r * cake[i].h;
            max_r = max(max_r, cake[i].r);
        }
        for (int i = k - 1; i < n; ++i) {
            ll rd = max(max_r, cake[i].r);
            double tmp = sum + PI * rd * rd + 2.0 * PI * cake[i].r * cake[i].h;
            ans = max(ans, tmp);
        }
        printf("Case #%d: %.8lf\n", cas, ans);
    }
    return 0;
}
