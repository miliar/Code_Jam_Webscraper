#include<stdio.h>
#include<string.h>

int T;
int K;
char S[1005];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Aoutput.txt","w",stdout);

    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        int ans = 0;
        int ch = 0;

        scanf(" %s%d", S, &K);
        printf("Case #%d: ", t);

        int n = strlen(S);
        for (int j = 0; j < n-K+1; j++)
        {
            if (S[j] == '-')
            {
                ans++;
                for (int k = 0; k < K; k++)
                {
                    if (S[j+k] == '-')
                    {
                        S[j+k] = '+';
                    }
                    else
                    {
                        S[j+k] = '-';
                    }
                }
            }
        }

        for (int j = 0; j < n; j++)
        {
            if (S[j] == '-')
            {
                ch = 1;
                break;
            }
        }
        if (ch == 1)
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            printf("%d\n", ans);
        }
    }

    return 0;
}