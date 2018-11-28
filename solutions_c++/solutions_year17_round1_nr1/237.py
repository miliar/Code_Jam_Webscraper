#include <cstdio>
#include <cstring>


char s[110][110];

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
            scanf("%s", s[i]);
        for (int i = 0; i < n; i++) {
            for (int j = 1, k = 0; j < m; j++, k++) {
                if (s[i][j] == '?' && s[i][k] != '?') s[i][j] = s[i][k];
            }
            for (int j = m - 2, k = m - 1; j >= 0; j--, k--) {
                if (s[i][j] == '?' && s[i][k] != '?') s[i][j] = s[i][k];
            }
        }
        for (int j = 0; j < m; j++) {
            for (int i = 1, k = 0; i < n; i++, k++)
                if (s[i][j] == '?' && s[k][j] != '?') s[i][j] = s[k][j];
            for (int i = n - 2, k = n - 1; i >= 0; i--, k--)
                if (s[i][j] == '?' && s[k][j] != '?') s[i][j] = s[k][j];
        }
        printf("Case #%d:\n", cas);
        for (int i = 0; i < n; i++) printf("%s\n", s[i]);
    }
    return 0;
}
