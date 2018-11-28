#include<stdio.h>
#include<string.h>

int T;
char N[20];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        scanf("%s", N);
        printf("Case #%d: ", t);
        int i;
        int len = strlen(N);
        if (N[0] == '0')
        {
            printf("0\n");
            continue;
        }
        for (int k = 0; k < len; k++)
        {
            for (i = 1; i < len; i++)
            {
                if (N[i-1] > N[i])
                {
                    N[i-1]--;
                    break;
                }
            }
            for (; i < len; i++)
            {
                N[i] = '9';
            }
        }

        for (i = 0; i < len; i++)
        {
            if (i == 0 && N[i] == '0')
            {
                continue;
            }
            printf("%c", N[i]);
        }
        printf("\n");
    }

    return 0;
}