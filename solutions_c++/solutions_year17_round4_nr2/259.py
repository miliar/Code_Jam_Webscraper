/*
 *  Author:
 *      Indestinee
 *  Date:
 *      2017/05/13
 *  Name:
 *      b.cpp
 */

#include <bits/stdc++.h>
using namespace std;
const int maxn = 1010;
int cas, n, c, m, p[maxn], id[maxn], cnt[maxn], vis[maxn];
int main() {
    scanf("%d", &cas);
    for (int t = 1; t <= cas; t++) {
        memset(cnt, 0, sizeof cnt);
        memset(vis, 0, sizeof vis);
        scanf("%d%d%d", &n, &c, &m);
        for (int i = 0; i < m; i++) {
            scanf("%d%d", &p[i], &id[i]);
            cnt[id[i]]++;
            vis[p[i]]++;
        }
        int maxi = 0, tot = 0;
        for (int i = 1; i <= c; i++)
            maxi = max(maxi, cnt[i]);
        for (int i = 1; i <= n; i++) {
            tot += vis[i];
            maxi = max(maxi, (tot + i - 1) / i);
        }
        int ans = 0;
        for (int i = 1; i <= n; i++)
            ans += max(0, vis[i] - maxi);
        printf("Case #%d: %d %d\n", t, maxi, ans);
    }

    return 0;
}
