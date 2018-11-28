#include <cstdio>
#include <cstring>
#include <cctype>
using namespace std;

int T;
int R, C;
char g[30][30];
bool alpha[26];

int letter_in_row(int x, int y, int z)
{
    for (; y <= z; ++y)
        if (isupper(g[x][y]))
            return y;
    return 0;
}

int letter_in_column(int x, int y, int z)
{
    for (; y <= z; ++y)
        if (isupper(g[y][x]))
            return y;
    return 0;
}

void expand(int rt, int rb, int cl, int cr)
{
    char c = g[rt][cl];
    for (int j = cl - 1; j > 0; --j)
    {
        if (letter_in_column(j, rt, rb))
            break;
        for (int i = rt; i <= rb; ++i)
            g[i][j] = c;
        if (cl - 1 > 0)
            cl -= 1;
    }
    for (int j = cr + 1; j <= C; ++j)
    {
        if (letter_in_column(j, rt, rb))
            break;
        for (int i = rt; i <= rb; ++i)
            g[i][j] = c;
        if (cr + 1 <= C)
            cr += 1;
    }
    for (int i = rt - 1; i > 0; --i)
    {
        if (letter_in_row(i, cl, cr))
            break;
        for (int j = cl; j <= cr; ++j)
            g[i][j] = c;
        if (rt - 1 > 0)
            rt -= 1;
    }
    for (int i = rb + 1; i <= R; ++i)
    {
        if (letter_in_row(i, cl, cr))
            break;
        for (int j = cl; j <= cr; ++j)
            g[i][j] = c;
        if (rb + 1 <= R)
            rb += 1;
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for (int z = 1; z <= T; ++z)
    {
        memset(alpha, 0, sizeof alpha);
        scanf("%d%d", &R, &C);
        for (int i = 1; i <= R; ++i)
            scanf("%s", g[i] + 1);
        for (int i = 1; i <= R; ++i)
        {
            for (int j = 1; j <= C; ++j)
            {
                if (isupper(g[i][j]) && !alpha[g[i][j] - 'A'])
                {
                    expand(i, i, j, j);
                    alpha[g[i][j] - 'A'] = true;
                }
            }
        }
        printf("Case #%d:\n", z);
        for (int i = 1; i <= R; ++i)
            printf("%s\n", g[i] + 1);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
