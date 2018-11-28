#include <bits/stdc++.h>
using namespace std;
const int N = 50;
char Grid[N][N];
int T, r, c;
int main()
{
    scanf("%d", &T);
    int P = 0;
    while (T --)
    {
        P ++;
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; ++ i)
            scanf("%s", Grid[i]);
        for (int i = 0; i < r; ++ i)
        {
            for (int j = 1; j < c; ++ j)
                if (Grid[i][j] == '?')
                    Grid[i][j] = Grid[i][j - 1];
            if (Grid[i][c - 1] == '?')
            {
                if (i)
                    for (int j = 0; j < c; ++ j) Grid[i][j] = Grid[i - 1][j];
            }
            else
            {
                for (int j = c - 1; ~j; -- j)
                    if (Grid[i][j] == '?')
                        Grid[i][j] = Grid[i][j + 1];
            }
        }
        for (int i = r - 1; ~i; -- i)
            if (Grid[i][0] == '?')
                for (int j = 0; j < c; ++ j)
                    Grid[i][j] = Grid[i + 1][j];

        printf("Case #%d:\n", P);
        for (int i = 0; i < r; ++ i)
            printf("%s\n", Grid[i]);
    }
}
