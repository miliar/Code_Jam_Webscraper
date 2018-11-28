#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define pb push_back

const int N = 1010;
vector<int> v[N];
vector<int> g[N];
int n, c, m, ans;

bool check(int rows) {
    int places = 0;
    ans = 0;
    for (int i = 1; i <= n; ++i) {
        places += g[i].size();
        if (places > rows * i) {
            return false;
        }
        ans += max<int>(g[i].size() - rows, 0);
    }
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt) {
        scanf("%d%d%d", &n, &c, &m);
        for (int i = 1; i <= c; ++i) {
            v[i].clear();
        }
        for (int i = 1; i <= n; ++i) {
            g[i].clear();
        }
        int l = 1, r = m;
        for (int i = 1; i <= m; ++i) {
            int p, b;
            scanf("%d%d", &p, &b);
            v[b].pb(p);
            g[p].pb(b);
            l = max<int>(l, v[b].size());
        }
        while (l < r) {
            int mid = (l + r) / 2;
            if (!check(mid)) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        check(l);
        printf("Case #%d: %d %d\n", tt, l, ans);
    }
}
