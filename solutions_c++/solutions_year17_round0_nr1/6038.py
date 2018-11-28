#include <stdio.h>
#include <string.h>

const int N = 1010;

void flip(char s[], int p, int k)
{
    for (int i = 0; i < k; i++) {
        if (s[p + i] == '-') {
            s[p + i] = '+';
        } else {
            s[p + i] = '-';
        }
    }
}

int main()
{
    int t;
    scanf("%d", &t);
    char s[N];
    for (int cases = 1; cases <= t; cases++) {
        int k;
        scanf("%s%d", s, &k);

        int n = strlen(s);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                if (i < n - k + 1) {
                    ans++;
                    flip(s, i, k);
                } else {
                    ans = -1;
                    break;
                }
            }
        }

        printf("Case #%d: ", cases);
        if (ans >= 0) {
            printf("%d\n", ans);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }

    return 0;
}
