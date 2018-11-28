#include <cstdio>
#include <cstring>
#define MAXN 1003
char s[MAXN];
int k;
void flip(char &x)
{
    x = x == '+' ? '-' : '+';
}
int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        scanf("%s%d", s, &k);
        int n = strlen(s);
        bool ok = true;
        int ct = 0;
        for (int i = 0; i < n; ++i)
            if (s[i] == '-') {
                if (n - i >= k) {
                    for (int j = 0; j < k; ++j)
                        flip(s[i + j]);
                    ++ct;
                }
                else {
                    ok = false;
                    break;
                }
            }
        printf("Case #%d: ", i);
        if (ok)
            printf("%d\n", ct);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
