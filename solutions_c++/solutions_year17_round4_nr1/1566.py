#include <cstdio>
#include <algorithm>

using namespace std;

int n, p, a[4];

int main() {
    int total_cas;
    scanf("%d", &total_cas);
    for (int cas = 1; cas <= total_cas; cas++) {
        scanf("%d%d", &n, &p);
        for (int i = 0; i < p; i++) a[i] = 0;
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            a[x % p]++;
        }
        int ans = a[0], t;
        if (p == 2) {
            ans += a[1] / 2;
            if (a[1] % 2 != 0) ans++;
        } else if (p == 3) {
            t = min(a[1], a[2]);
            ans += t;
            a[1] -= t; a[2] -= t;

            ans += a[1] / 3;
            ans += a[2] / 3;
            if (a[1] % 3 != 0 || a[2] % 3 != 0) ans++;
        } else if (p == 4) {
            t = min(a[1], a[3]);
            ans += t;
            a[1] -= t; a[3] -= t;

            t = a[2] / 2;
            ans += t;
            a[2] -= t;

            t = min(a[1] / 2, a[2]);
            ans += t;
            a[1] -= t * 2; a[2] -= t;

            t = min(a[3] / 2, a[2]);
            ans += t;
            a[3] -= t * 2; a[2] -= t;

            ans += a[1] / 4;
            ans += a[3] / 4;
            if (a[1] % 4 != 0 || a[2] % 4 != 0 || a[3] % 4 != 0) ans++;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
