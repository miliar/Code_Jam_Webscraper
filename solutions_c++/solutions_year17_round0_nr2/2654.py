#include <stdio.h>

void query()
{
    char s[55];
    scanf("%s", s);

    for (int i = 1; s[i] != 0; i++)
    {
        if (s[i] < s[i - 1])
        {
            for (int j = i; s[j] != 0; j++)
            {
                s[j] = '9';
            }
            s[i - 1]--;
            i = 0;
        }
    }

    int firstNonZero = 0;
    while (s[firstNonZero] == '0')
    {
        firstNonZero++;
    }

    for (int i = firstNonZero; s[i] != 0; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
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