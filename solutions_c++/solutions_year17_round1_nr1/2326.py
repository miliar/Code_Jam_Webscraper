#include <cstdio>

using namespace std;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);

    int R, C, TC;
    char cake[30][30];

    scanf("%d", &TC);

    for(int t=1; t<=TC; t++)
    {
        scanf("%d%d", &R, &C);

        for(int i=0; i<R; i++)
            scanf("%s", cake[i]);


        for(int i=0; i<R; i++)
        {
            for(int j=1; j<C; j++)
            {
                if(cake[i][j] == '?') cake[i][j] = cake[i][j-1];
            }
            for(int j=C-2; j>=0; j--)
            {
                if(cake[i][j] == '?') cake[i][j] = cake[i][j+1];
            }
        }

        bool vacia;

        for(int i=1; i<R; i++)
        {
            vacia = true;
            for(int j=0; j<C; j++)
                if(cake[i][j] != '?') vacia = false;

            if(vacia)
                for(int j=0; j<C; j++)
                    cake[i][j] = cake[i-1][j];
        }

        for(int i=R-2; i>=0; i--)
        {
            vacia = true;
            for(int j=0; j<C; j++)
                if(cake[i][j] != '?') vacia = false;

            if(vacia)
                for(int j=0; j<C; j++)
                    cake[i][j] = cake[i+1][j];
        }

        printf("Case #%d:\n", t);
        for(int i=0; i<R; i++)
            printf("%s\n", cake[i]);


    }

    return 0;
}
