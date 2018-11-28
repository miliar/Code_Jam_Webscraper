#include <cstdio>
#include <cstring>

void tcase()
{
    char str[20];
    scanf("%s", str);

    int strLen = strlen(str);

    int firstBadPos = strLen;
    for (int i = strLen - 2; i >= 0; i--)
    {
        if (str[i] > str[i + 1])
        {
            firstBadPos = i + 1;
            str[i]--;
        }
    }

    bool isPassLeadingZero = false;
    for (int i = 0; i < strLen; i++)
    {
        if (str[i] != '0')
        {
            isPassLeadingZero = true;
        }

        if (i < firstBadPos)
        {
            if (isPassLeadingZero)
            {
                printf("%c", str[i]);
            }
        }
        else
        {
            printf("9");
        }
    }
}

int main()
{
    int tNo;

    scanf("%d", &tNo);

    for (int t = 1; t <= tNo; t++)
    {
        printf("Case #%d: ", t);
        tcase();
        printf("\n");
    }

    return 0;
}
