#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 1001;

int a[N], b[N], d[N];
int n, c, m;

int main() {
    int total_cas;
    scanf("%d", &total_cas);
    for (int cas = 1; cas <= total_cas; cas++) {
        scanf("%d%d%d", &n, &c, &m);
        for (int i = 1; i <= c; i++) a[i] = 0;
        for (int i = 1; i <= n; i++) b[i] = 0;
        for (int i = 0; i < m; i++) {
            int p, x;
            scanf("%d%d", &p, &x);
            a[x]++;
            b[p]++;
        }
        for (int i = 1; i <= n; i++) d[i] = b[i] + b[i - 1];
        int ans1 = 0, ans2 = 0;
        for (int i = 1; i <= c; i++) ans1 = max(ans1, a[i]);
        for (int i = 1; i <= n; i++) ans1 = max(ans1, (d[i] + i - 1) / i);
        for (int i = 1; i <= n; i++) ans2 += max(0, b[i] - ans1);
        printf("Case #%d: %d %d\n", cas, ans1, ans2);
    }
    return 0;
}
