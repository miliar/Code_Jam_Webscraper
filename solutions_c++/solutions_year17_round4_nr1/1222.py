#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int N = 110;
int a[N];

int main() {
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        int n, p;
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; i++) scanf("%d", &a[i]);
        int ans = 0;
        if (p == 2) {
            int cnt = 0;
            for (int i = 0; i < n; i++) if (a[i] % 2 == 0) ans++;
            else cnt++;
            ans += (cnt + 1) / 2;
        } else if (p == 3) {
            int cnt1 = 0, cnt2 = 0;
            for (int i = 0; i < n; i++) if (a[i] % 3 == 0) ans++;
            else if (a[i] % 3 == 1) cnt1++;
            else cnt2++;
            ans += min(cnt1, cnt2);
            int cnt = abs(cnt1 - cnt2);
            if (cnt) ans += (cnt - 1) / 3 + 1;
        } else {
            int cnt[4] = {0, 0, 0, 0};
            for (int i = 0; i < n; i++) cnt[a[i] % 4]++;
            ans += cnt[0];
            ans += min(cnt[1], cnt[3]);
            ans += cnt[2] / 2;
            int c = abs(cnt[1] - cnt[3]);
            if (cnt[2] & 1) {
                ans += 1;
                c -= 2;
            }
            if (c > 0) ans += (c-1) / 4 + 1;
        }
        printf("Case #%d: %d\n", _, ans);
    }

    return 0;
}
