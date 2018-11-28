#include <stdio.h>
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int R, C;
    char Board[25][26];
    int T, t;
    scanf("%d", &T);
    int i, j, k, l;
    for (t = 1; t <= T; t++)
    {
        scanf("%d %d", &R, &C);
        for (i = 0; i < R; i++)
            scanf(" %s", Board[i]);
        for (j = 0; j < C; j++)
        {
            for (i = 0; i < R; i++)
            {
                if (Board[i][j] != '?')
                {
                    for (k = 0; k <= i; k++)
                        if (Board[k][j] == '?')
                            Board[k][j] = Board[i][j];
                }
            }
        }
        for (i = 0; i < C; i++)
        {
            for (j = R - 1; j >= 0; j--)
            {
                if (Board[j][i] != '?')
                {
                    for (k = j; k < R; k++)
                        Board[k][i] = Board[j][i];
                    break;
                }
            }
        }
        for (i = 0; i < C; i++)
        {
            for (j = R - 1; j >= 0; j--)
            {
                if (Board[j][i] != '?')
                    break;
            }
            if (j == -1)
            {
                if (i == 0)
                {
                    k = i;
                    while (Board[0][k] == '?') k++;
                    for (j = 0; j < R; j++)
                        Board[j][i] = Board[j][k];
                }
                else
                {
                    for (j = 0; j < R; j++)
                        Board[j][i] = Board[j][i - 1];
                }
            }
        }
        printf("Case #%d:\n", t);
        for (i = 0; i < R; i++)
            printf("%s\n", Board[i]);
    }
}
