#include <cstdio>

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        int n, m;
        char a[30][30];
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            scanf("%s", a[i]);
            for (int j = 1; j < m; ++j) {
                if (a[i][j] == '?') {
                    a[i][j] = a[i][j-1];
                }
            }
            for (int j = m - 2; j >= 0; --j) {
                if (a[i][j] == '?') {
                    a[i][j] = a[i][j+1];
                }
            }
        }
        for (int i = 1; i < n; ++i) {
            if (a[i][0] == '?') {
                for (int j = 0; j < m; ++j) {
                    a[i][j] = a[i-1][j];
                }
            }
        }
        for (int i = n - 2; i >= 0; --i) {
            if (a[i][0] == '?') {
                for (int j = 0; j < m; ++j) {
                    a[i][j] = a[i+1][j];
                }
            }
        }
        printf("Case #%d:\n", cas);
        for (int i = 0; i < n; ++i) {
            puts(a[i]);
        }
    }
}
