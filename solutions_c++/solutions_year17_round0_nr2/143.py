#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int main() {
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        LL n;
        scanf("%lld", &n);
        LL tmp = n;
        int m = 0;
        while (tmp) m++, tmp /= 10;
        m--;
        LL pw = 1, pm = 1;
        for (int i = 1; i <= m; i++) pw += pm *= 10;
        LL ans = 0;
        int mx = 0;
        for (int i = m; i >= 0; i--) {
            int j;
            for (j = mx; j <= 9; j++) 
                if (ans + j * pw > n) break;
            ans += --j * pm;
            pw -= pm;
            pm /= 10;
        }
        printf("Case #%d: %lld\n", _, ans);
    }
    return 0;
}
