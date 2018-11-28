#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testcase;
    scanf("%d", &testcase);
    for (int ti = 1; ti <= testcase; ti++) {
        printf("Case #%d: ", ti);
        int m, n, c;
        scanf("%d%d%d", &n, &c, &m);
        int a[2000], b[2000], e[2000], f[2000];
        for (int i = 1; i <= n; i++) f[i] = 0;
        for (int i = 1; i <= c; i++) e[i] = 0;
        for (int i = 0; i < m; i++) {
            scanf("%d%d", &b[i], &a[i]);
            e[a[i]]++;
            f[b[i]]++;
        }

        int ans = 0;
        int max_ans = 0;
        for (int i = 1; i <= c; i++) {
            if (e[i] > ans) ans = e[i];

        }

        int l = 0;
        for (int i = 1; i <= n; i++) {
            l += f[i];
            ans = max(ans, (l + (i - 1)) / i);
        }

        int ans2 = 0;
        for (int i = 1; i <= n; i++) {
            if (f[i] > ans)
                ans2 += f[i] - ans;
        }

        printf("%d %d\n", ans, ans2);
    }
}