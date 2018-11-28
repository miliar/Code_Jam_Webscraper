#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testcase;
    scanf("%d", &testcase);
    for (int ti = 1; ti <= testcase; ti++) {
        printf("Case #%d: ", ti);
        char g[2000];
        int k;
        scanf("%s %d", &g, &k);
        int flips[2000];
        int ll = 0, rr = -1;
        int glen = strlen(g);
        bool suc = true;
        for (int i = 0; i < glen; i++) {
            while (ll <= rr && flips[ll] <= i - k) ll++;
            if (i > glen - k) {
                if (g[i] == '+' && (rr - ll + 1) % 2 != 0 || g[i] == '-' && (rr - ll + 1) % 2 != 1) {
                    suc = false;
                    break;
                }
            } else {
                if (g[i] == '+' && (rr - ll + 1) % 2 != 0 || g[i] == '-' && (rr - ll + 1) % 2 != 1) {
                    rr++;
                    flips[rr] = i;
                }
            }
        }
        if (suc) {
            printf("%d\n", rr + 1);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
}