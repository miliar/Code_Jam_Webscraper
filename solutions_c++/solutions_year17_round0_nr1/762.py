#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void solve()
{
    char inbuf[1001];
    int k;
    scanf("%s%d", inbuf, &k);

    int len = strlen(inbuf);

    int count = 0;
    for (int i = 0; i <= len - k; ++i) {
        if (inbuf[i] == '+') continue;

        ++count;
        for (int j = 0; j < k; ++j) {
            inbuf[i + j] = inbuf[i + j] == '+' ? '-' : '+';
        }
    }

    for (int i = len - k + 1; i < len; ++i) {
        if (inbuf[i] == '-') {
            printf("IMPOSSIBLE\n");
            return;
        }
    }

    printf("%d\n", count);
}

int main(void)
{
    int nC;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        printf("Case #%d: ", cC + 1);
        solve();
    }
}