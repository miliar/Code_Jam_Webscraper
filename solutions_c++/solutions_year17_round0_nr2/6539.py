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
        char g[30];
        scanf("%s", &g);
        int l = 0;
        int glen = strlen(g);
        for (int i = 0; i < glen - 1; i++) {
            if (g[i] == g[i + 1]) {
                continue;
            }
            if (g[i] < g[i + 1]) {
                l = i + 1;
            }
            if (g[i] > g[i + 1]) {
                g[l] = g[l] - 1;
                for (int j = l + 1; j < glen; j++) {
                    g[j] = '9';
                }
                break;
            }
        }
        l = 0;
        if (g[0] == '0') l = 1;
        for (int i = l; i < glen; i++) {
            printf("%c", g[i]);
        }
        printf("\n");

    }
}