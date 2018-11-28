#include <stdio.h>

int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++) {
        int n, p;
        scanf("%d%d", &n, &p);
        int x[4];
        for (int j = 0; j < p; j++) {
            x[j] = 0;
        }
        for (int i = 0; i < n; i++) {
            int a;
            scanf("%d", &a);
            x[a % p]++;
        }
        int ans = x[0];
        if (p == 2) {
            ans += x[1] / 2;
            x[1] = x[1] % 2;
            if (x[1] > 0) {
                ans++;
            }
        } else if (p == 3) {
            if (x[1] > x[2]) {
                ans += x[2];
                x[1] -= x[2];
                x[2] = 0;
                ans += x[1] / 3;
                x[1] = x[1] % 3;
            } else {
                ans += x[1];
                x[2] -= x[1];
                x[1] = 0;
                ans += x[2] / 3;
                x[2] = x[2] % 3;
            }
            if (x[1] + x[2] > 0) {
                ans++;
            }
        } else {
            if (x[1] > x[3]) {
                ans += x[3];
                x[1] -= x[3];
                x[3] = 0;
            } else {
                ans += x[1];
                x[3] -= x[1];
                x[1] = 0;
            }
            int y = x[1] + x[3];
            int p = y / 2;
            y = y % 2;
            if (x[2] > p) {
                ans += p;
                x[2] -= p;
                ans += x[2] / 2;
                y += x[2] % 2;
            } else {
                ans += x[2];
                p -= x[2];
                ans += p / 4;
                y += p % 4;
            }
            if (y > 0) {
                ans++;
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
