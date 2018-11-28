#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

#define MaxN 1010

using namespace std;

int n, c, m;
int cnt[MaxN], f[MaxN], ans0;
int a[MaxN], b[MaxN];

int main() {
    int T, T0 = 0;
    scanf("%d", &T);
    for ( ; T; --T) {
        scanf("%d%d%d", &n, &c, &m);
        memset(cnt, 0, sizeof(cnt));
        memset(f, 0, sizeof(f));
        for (int i = 0; i < m; ++i) {
            scanf("%d%d", &a[i], &b[i]);
            ++cnt[b[i]];
            ++f[a[i]];
        }
        ans0 = 0;
        int tot = 0;
        for (int i = 1; i <= n; ++i) {
            // ans0 * i >= tot
            tot += f[i];
            ans0 = max((double)ans0, ceil(tot * 1.0 / i));
        }
        for (int i = 1; i <= c; ++i)
            ans0 = max(ans0, cnt[i]);
        int ans1 = 0;
        for (int i = 1; i <= n; ++i)
            ans1 += min(f[i], ans0);
        ans1 = m - ans1;
        printf("Case #%d: %d %d\n", ++T0, ans0, ans1);
    }
    return 0;
}
