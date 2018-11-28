#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int kases;
int n, p, g[200], cnt[200], ans;
int vis[200][200][200], dfsa[200][200][200];

int dfs(int u1, int u2, int u3) {
    if (vis[u1][u2][u3]) return dfsa[u1][u2][u3];
    vis[u1][u2][u3] = 1;
    if (u1 == 0 && u2 == 0 && u3 == 0) {
        dfsa[u1][u2][u3] = 0;
    } else {
        int maxans = 0;
        if (u1 >= 2 && u2 >= 1) maxans = max(maxans, dfs(u1 - 2, u2 - 1, u3) + 1);
        if (u1 >= 4) maxans = max(maxans, dfs(u1 - 4, u2, u3) + 1);
        if (u2 >= 2) maxans = max(maxans, dfs(u1, u2 - 2, u3) + 1);
        if (u3 >= 4) maxans = max(maxans, dfs(u1, u2, u3 - 4) + 1);
        if (u1 >= 1 && u3 >= 1) maxans = max(maxans, dfs(u1 - 1, u2, u3 - 1) + 1);
        if (u3 >= 2 && u2 >= 1) maxans = max(maxans, dfs(u1, u2 - 1, u3 - 2) + 1);
        dfsa[u1][u2][u3] = maxans;
        if (maxans == 0)
            dfsa[u1][u2][u3] = 1;
    }
    return dfsa[u1][u2][u3];
}

int main() {
    #ifdef ULTMASTER
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    #endif
    scanf("%d", &kases);
    for (int kase = 1; kase <= kases; ++kase) {
        scanf("%d%d", &n, &p);
        memset(cnt, 0, sizeof cnt);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &g[i]);
            g[i] %= p;
            cnt[g[i]]++;
        }
        if (p == 2) {
            ans = cnt[0] + cnt[1] / 2;
            if (cnt[1] % 2) ans++;
        } else if (p == 3) {
            ans = cnt[0] + min(cnt[1], cnt[2]) + abs(cnt[1] - cnt[2]) / 3;
            if ((cnt[1] - cnt[2]) % 3) ans++;
        } else if (p == 4) {
            ans = cnt[0] + dfs(cnt[1], cnt[2], cnt[3]);
        }
        printf("Case #%d: %d\n", kase, ans);
    }
    return 0;
}