#include<stdio.h>
#include<string.h>
int main() {
    int t, k, len, i, j, flipCount, isFlip, ans, fPos;
    char s[1005];
    int spos[1005];
    scanf("%d", &t);
    for (i = 1; i <= t; i += 1) {
        scanf("%s %d", s, &k);
        len = strlen(s);
        for (j = 0; j < len; j += 1) {
            spos[j] = 0;
        }
        ans = 0;
        flipCount = 0;
        for (j = 0; j <= (len - k); j += 1) {
            isFlip = 0;
            if ((s[j] == '+' && flipCount % 2 != 0) || (s[j] == '-' && flipCount % 2 == 0)) {
                isFlip = 1;
            }
            if (spos[j] == -1) {
                flipCount -= 1;
            }
            if (isFlip == 1) {
                ans += 1;
                flipCount += 1;
                spos[j] = 1;
                fPos = j + k - 1;
                if (fPos >= len) {
                    fPos = len - 1;
                }
                spos[fPos] = -1;
            }
        }
        for (j = len - k + 1; j < len; j += 1) {
            if ((s[j] == '+' && flipCount % 2 != 0) || (s[j] == '-' && flipCount % 2 == 0)) {
                ans = -1;
                break;
            }
            if (spos[j] == -1) {
                flipCount -= 1;
            }
        }
        if (ans >= 0) {
            printf("Case #%d: %d\n", i, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", i);
        }
    }
    return 0;
}
