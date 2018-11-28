#include<iostream>
#include<cstdio>
using namespace std;

char cake[25][25];

int main(void)
{
    int T;  cin >> T;
    for (int t = 1; t <= T; t ++)
    {
        int R, C;   cin >> R >> C;

        for (int i = 0; i < R; i ++)
            for (int j = 0; j < C; j ++)
                scanf(" %c", &cake[i][j]);

        for (int i = 1; i < R; i ++)
            for (int j = 0; j < C; j ++)
                if (cake[i-1][j] != '?' && cake[i][j] == '?')
                    cake[i][j] = cake[i-1][j];

        for (int i = R-1; i > 0; i --)
            for (int j = 0; j < C; j ++)
                if (cake[i][j] != '?' && cake[i-1][j] == '?')
                    cake[i-1][j] = cake[i][j];

        for (int i = 0; i < R; i ++)
            for (int j = 1; j < C; j ++)
            {
                /*
                if (i - 1 >= 0)
                    if (cake[i-1][j] == cake[i][j])
                        continue;
                if (i + 1 < R)
                    if (cake[i+1][j] == cake[i][j])
                        continue;
*/
                if (cake[i][j-1] != '?' && cake[i][j] == '?')
                    cake[i][j] = cake[i][j-1];
            }

        for (int i = 0; i < R; i ++)
            for (int j = C-1; j > 0; j --)
                if (cake[i][j] != '?' && cake[i][j-1] == '?')
                    cake[i][j-1] = cake[i][j];

        printf("Case #%d:\n", t);
        for (int i = 0; i < R; i ++)
        {
            for (int j = 0; j < C; j ++)
                printf("%c", cake[i][j]);
            printf("\n");
        }
    }
}
