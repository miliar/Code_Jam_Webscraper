#include <cstdio>
#include <cstring>

int n, k;
char s[1024];

int solve()
{
    int ret = 0;
    for (int i = 0; i <= n - k; i++) {
        if (s[i] == '+') continue;
        ++ret;
        for (int j = 0; j < k; j++) {
            char &c = s[i + j];
            if (c == '-') c = '+';
            else c = '-';
        }
    }
    for (int i = n - k + 1; i < n; i++)
        if (s[i] == '-') return -1;
    return ret;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        scanf("%s%d", s, &k);
        n = strlen(s);
        int ans = solve();
        printf("Case #%d: ", tc);
        if (ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }

    return 0;
}
