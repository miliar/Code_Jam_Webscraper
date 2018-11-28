#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int, int> II;

int main() {
#ifdef LOCAL
    freopen("inp", "r", stdin);
    freopen("out", "w", stdout);
#endif
    int TC; scanf("%d", &TC);
    for (int testID = 1; testID <= TC; ++testID) {
        printf("Case #%d: ", testID);
        int n, p; scanf("%d%d", &n, &p);
        int c[10] = {0};
        for (int i = 1; i <= n; ++i) {
            int x; scanf("%d", &x);
            c[x % p]++;
        }
        if (p == 2) printf("%d\n", c[0] + (c[1] + 1) / 2);
        if (p == 3) {
            int ans = c[0] + min(c[1], c[2]);
            ans += (abs(c[1] - c[2]) + 2) / 3;
            printf("%d\n", ans);
        }
        if (p == 4) {
            int ans = c[0] + min(c[1], c[3]) + c[2] / 2;
            if (c[2] % 2 == 1) {
                if (c[1] < c[3]) swap(c[1], c[3]); c[1] -= c[3];
                if (c[1] >= 2) ans += 1 + (c[1] + 1) / 4;
                else ans += 1;
            }
            else ans += (abs(c[1] - c[3]) + 3) / 4;
            printf("%d\n", ans);
        }
    }
    return 0;
}
