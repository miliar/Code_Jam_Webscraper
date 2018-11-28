#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        int n, p;
        scanf("%d%d", &n, &p);
        vector<int> g(4, 0);
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            g[x % p]++;
        }

        int ans = g[0];
        if (p == 2) {
            ans += g[1] / 2;
            if (g[1] % 2) {
                ans++;
            }
        } else if (p == 3) {
            int tmp = min(g[1], g[2]);
            ans += tmp;
            g[1] -= tmp;
            g[2] -= tmp;
            ans += g[1] / 3;
            if (g[1] % 3) {
                ans++;
            }
            ans += g[2] / 3;
            if (g[2] % 3) {
                ans++;
            }
        }

        printf("Case #%d: %d\n", cases, ans);
    }
    return 0;
}
