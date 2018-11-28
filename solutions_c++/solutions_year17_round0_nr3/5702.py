#include <bits/stdc++.h>

#define fst first
#define snd second

using namespace::std;

const int maxn = 1e3 + 5;
const int inf = 0x3f3f3f3f;
int n, k, vis[maxn];

void solve() {
    scanf("%d%d", &n, &k);
    memset(vis, 0, sizeof(vis));
    vis[0] = vis[n+1] = 1;
    while (k--) {
        int minn = 0, maxx = 0, pos;
        int l = 0, r = 0;
        for (int i = 1; i <= n; i++) {
            if (vis[i]) continue;
            l = r = 0;
            while (vis[i-l-1] == 0) l++;
            while (vis[i+r+1] == 0) r++;
            if (minn < min(l, r)) {
                minn = min(l, r); maxx = max(l, r); pos = i;
            } else if (minn == min(l, r)) {
                if (maxx < max(l, r)) {
                    maxx = max(l, r); pos = i;
                }
            }
        }
        vis[pos] = 1;
        if (k == 0) {
            printf("%d %d\n", maxx, minn);
        }
    }
}

int main() {
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t; scanf("%d", &t);
    for (int Case = 1; Case <= t; Case++) {
        printf("Case #%d: ", Case);
        solve();
    }
    return 0;
}
