#include <cstdio>
#include <cstring>
#define MAXN 30
int n, m;
char a[MAXN][MAXN];
int main()
{
    int T;
    scanf("%d", &T);
    for (int Ti = 1; Ti <= T; ++Ti) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                scanf(" %c", &a[i][j]);
        int no[MAXN] = {};
        for (int i = 0; i < n; ++i) {
            int pos[MAXN], lp = 0;
            for (int j = 0; j < m; ++j)
                if (a[i][j] != '?') {
                    ++no[i];
                    pos[lp++] = j;
                }
            pos[lp] = m;
            if (no[i] != 0) {
                for (int k = 0; k < pos[0]; ++k)
                    a[i][k] = a[i][pos[0]];
                for (int j = 0; j < lp; ++j)
                    for (int k = pos[j]; k < pos[j + 1]; ++k)
                        a[i][k] = a[i][pos[j]];
            }
        }
        for (int i = 0; i < n; ++i)
            if (no[i] != 0) {
                for (int j = i - 1; j >= 0; --j)
                    if (no[j] == 0)
                        memcpy(a[j], a[i], MAXN), no[j]=1;
                    else
                        break;
                for (int j = i + 1; j < n; ++j)
                    if (no[j] == 0)
                        memcpy(a[j], a[i], MAXN),no[j]=1;
                    else
                        break;
            }
        printf("Case #%d:\n", Ti);
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
                putchar(a[i][j]);
            putchar('\n');
        }
    }
    return 0;
}
