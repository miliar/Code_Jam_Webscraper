#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>

char s[20];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t, tt=0;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%s", s);

        printf("Case #%d: ", ++tt);

        int n = strlen(s);
        while (true)
        {
            bool f = false;
            for (int i=0; i+1<n; i++)
            {
                if (s[i] > s[i+1])
                {
                    f = true;
                    s[i]--;
                    for (int j=i+1; j<n; j++)
                        s[j] = '9';
                    break;
                }
            }

            if (!f)
                break;
        }

        bool f = true;
        for (int i=0; i<n; i++)
        {
            if (f && s[i] == '0');
            else
            {
                printf("%c", s[i]);
                f = false;
            }
        }
        printf("\n");
    }

    return 0;
}
