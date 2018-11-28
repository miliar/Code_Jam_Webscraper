#include <stdio.h>
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, t;
    char S[1005];
    int K, i, j;
    int cnt, valid;
    scanf("%d", &T);
    for (t = 1; t <= T; t++)
    {
        scanf(" %s", S);
        scanf("%d", &K);

        valid = 1;
        cnt = 0;
        for (i = 0; S[i + K - 1] != '\0'; i++)
        {
            if (S[i] == '-')
            {
                cnt++;
                for (j = 0; j < K; j++)
                {
                    S[i + j] = (S[i + j] == '-')?'+':'-';
                }
            }
        }
        for (; S[i] != '\0'; i++)
            if (S[i] == '-')
                valid = 0;
        if (valid)
            printf("Case #%d: %d\n", t, cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n", t);
    }
}
