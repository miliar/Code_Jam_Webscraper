#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int NN = 4000;

int main()
{
    int t, T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++)
    {
        int n;
        char s[2002];

        scanf("%s %d", &s, &n);

        int a[2002];

        int m = strlen(s);

        for (int i = 0; i < m; i++)
            a[i] = s[i] == '+' ? 1 : 0;

        int flips = 0;
        bool imposible = false;
        for (int i = 0; i < m; i++)
        {
            if (a[i] == 0)
            {
                if (i + n > m)
                {
                    imposible = true;
                    break;
                }

                for (int j = 0; j < n; j++)
                {
                    int g = i + j;
                    a[g] = a[g] == 0 ? 1 : 0;
                }

                flips++;
            }
        }

        if(imposible)
            printf("Case #%d: IMPOSSIBLE\n", t);
        else
            printf("Case #%d: %d\n", t, flips);

    }

    return 0;
}
