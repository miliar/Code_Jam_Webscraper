#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void solve()
{
    char num[22];

    scanf("%s", num);

    int len = strlen(num);

    for (int i = len - 1; i > 0; --i) {
        if (num[i] >= num[i - 1]) continue;
        --num[i - 1];
        memset(num + i, '9', len - i);
    }
    char *start = num;
    while (*start == '0') ++start;

    printf("%s\n", start);
}

int main(void)
{
    int nC;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        printf("Case #%d: ", cC + 1);
        solve();
    }
    return 0;
}