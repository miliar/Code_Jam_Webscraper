#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testcase;
    scanf("%d", &testcase);
    for (int ti = 1; ti <= testcase; ti++) {
        printf("Case #%d: ", ti);
        int m, n;
        scanf("%d%d", &n, &m);
        int b[5];
        for (int i = 0; i < m; i++) {
            b[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            int k;
            scanf("%d", &k);
            b[k % m]++;

        }

        int ans = 0;
        if (m == 2) {
            ans = b[0] + (b[1] + 1) / 2;
        }
        if (m == 3) {
            ans = b[0];
            int da = max(b[1], b[2]);
            int xiao = min(b[1], b[2]);
            ans = ans + xiao;
            ans = ans + (da - xiao + 2) / 3;
        }
        if (m == 4) {
            ans = b[0];
            ans = ans + b[2] / 2;
            int da = max(b[1], b[3]);
            int xiao = min(b[1], b[3]);
            ans = ans + xiao;
            int remains = da - xiao;
            if (b[2] % 2 == 1) {
                remains -= 2;
                ans++;
            }
            if (remains > 0) {
                ans += (remains + 3) / 4;
            }
        }
        printf("%d\n", ans);
    }
}