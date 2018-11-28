#include <cstdio>
#include <cstring>

void tcase()
{
    char pattern[1001];
    int flipperSize;

    scanf("%s %d", pattern, &flipperSize);

    int patternSize = strlen(pattern);
    int count = 0;

    for (int start = 0; start + flipperSize <= patternSize; start++)
    {
        int end = start + flipperSize - 1;
        if (pattern[start] == '-')
        {
            count++;
            for (int j = start; j <= end; j++)
            {
                pattern[j] = pattern[j] == '+' ? '-' : '+';
            }
        }
    }

    for (int i = 0; i < patternSize; i++)
    {
        if (pattern[i] == '-')
        {
            printf("IMPOSSIBLE\n");
            return;
        }
    }

    printf("%d\n", count);
}

int main()
{
    int tNo;

    scanf("%d", &tNo);

    for (int t = 1; t <= tNo; t++)
    {
        printf("Case #%d: ", t);
        tcase();
    }
}