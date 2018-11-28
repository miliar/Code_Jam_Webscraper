#include <bits/stdc++.h>

using namespace std;

typedef long long LL;


int main() {
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        int d, n;
        scanf("%d%d", &d, &n);
        double mx = 0;
        while (n--) {
            int k, s;
            scanf("%d%d", &k, &s);
            mx = max(mx, (d - k) * 1.0 / s);
        }
        printf("Case #%d: %.6f\n", _, d / mx);
    }

    return 0;
}
