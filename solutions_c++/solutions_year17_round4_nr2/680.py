#include <bits/stdc++.h>
using namespace std;
const int N = 1000 + 5;
int T, Case;
int n, m, c;
vector<int> a[N];
int cnt[N];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out1.out", "w", stdout);
    scanf("%d", &T);
    while(T--) {
        scanf("%d%d%d", &n, &c, &m);
        memset(cnt, 0, sizeof(cnt));
        int ans1 = 0, ans2 = 0, mx = 0;
        for(int i = 1; i <= n; i++) a[i].clear();
        memset(cnt, 0, sizeof(cnt));
        for(int i = 0; i < m; i++) {
            int p, x;
            scanf("%d%d", &x, &p);
            a[x].push_back(p);
            cnt[p]++;
            mx = max(mx, cnt[p]);
        }
        for(int i = 1; i <= c; i++) sort(a[i].begin(), a[i].end());
        for(ans1 = mx; ans1 <= m; ans1++) {
            int promote = 0, ok = 1, foo = 0;
            for(int i = 1; i <= n; i++) {
                if(ans1 > a[i].size()) foo += ans1 - a[i].size();
                else if(foo < a[i].size() - ans1) {
                    ok = 0;
                    break;
                }else {
                    int delta = a[i].size() - ans1;
                    promote += delta;
                    foo -= delta;
                }
            }
            if(ok) {
                ans2 = promote;
                break;
            }
        }
        printf("Case #%d: %d %d\n", ++Case, ans1, ans2);
    }
    return 0;
}
