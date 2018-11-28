#include <stdio.h>
#include <string.h>

void query()
{
    int k;
    char s[1010];
    scanf("%s %d", s, &k);

    int flips = 0;
    int start = 0, end = k - 1;
    int panc = strlen(s);

    while (end < panc)
    {
        if (s[start] == '-')
        {
            for (int i = start; i <= end; i++)
            {
                if (s[i] == '+') s[i] = '-';
                else s[i] = '+';
            }
            flips++;
        }
        start++;
        end++;
    }

    for (int i = start; i < panc; i++)
    {
        if (s[i] == '-')
        {
            printf("IMPOSSIBLE\n");
            return;
        }
    }

    printf("%d\n", flips);
}

int main()
{
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        query();
    }

    return 0;
}