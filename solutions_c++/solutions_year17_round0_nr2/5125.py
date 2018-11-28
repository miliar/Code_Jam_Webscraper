#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int kases;
ll n;
int limit[100], len, ans[100];

int dfs(int u, int llim, int rlim, int freedom) {
    if (u >= len)
        return 1;
    int start = limit[u];
    for (int i = rlim; i >= llim; --i) {
        int nextlim = limit[u + 1], new_free = 0;
        if (freedom || i < rlim) {
            nextlim = 9;
            new_free = 1;
        }
        if (dfs(u + 1, i, nextlim, new_free)) {
            ans[u] = i;
            return 1;
        }
    }
    return 0;
}

int main(){
    #ifdef ULTMASTER
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    #endif
    scanf("%d", &kases);
    for (int kase = 1; kase <= kases; ++kase) {
        scanf("%lld", &n);
        len = 0;
        while (n) {
            limit[len++] = n % 10;
            n /= 10;
        }
        reverse(limit, limit + len);
        dfs(0, 0, limit[0], 0);

        printf("Case #%d: ", kase);
        int start = 0;
        while (ans[start] == 0) start++;
        for (; start < len; ++start)
            printf("%d", ans[start]);
        putchar('\n');
    }

    return 0;
}
