#include <stdio.h>
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, t;
    scanf("%d", &T);
    char N[500];
    int l, i, j;
    for (t = 1; t <= T; t++)
    {
        scanf(" %s", N);
        for (l = 0; N[l] != '\0'; l++);
        for (i = l - 1; i > 0; i--)
        {
            if (N[i] < N[i - 1])
            {
                N[i - 1]--;
                for (j = i; j < l; j++)
                    N[j] = '9';
            }
        }
        printf("Case #%d: ", t);
        for (i = 0; N[i] == '0'; i++);
        for (; i < l; i++)
            printf("%c", N[i]);
        printf("\n");
    }
}
