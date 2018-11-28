#include <cstdio>

#define N 1024

int T, k, ret, n;
char s[N];
bool f;

int main() {
    scanf("%d", &T);
    for (int r = 1; r <= T; ++r) {
        printf("Case #%d: ", r);
        ret = 0;
        scanf("%s%d", s, &k);
        n = -1;
        while (s[++n]);
        for (int i = 0; i <= n - k; ++i)
            if (s[i] == '-') {
                ++ret;
                for (int j = 0; j < k; ++j)
                    s[i + j] = '+' + '-' - s[i + j];
            }
        f = 1;
        for (int i = 0; i < n; ++i)
            if (s[i] == '-')
                f = 0;
        if (f)
            printf("%d\n", ret);
        else
            puts("IMPOSSIBLE");
    }
    return 0;
}
