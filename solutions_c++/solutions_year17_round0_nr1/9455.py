#include <stdio.h>
#include <string.h>

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.in", "w", stdout);
    int tc, K, length, flip, done;
    bool finish;
    char S[1010];

    scanf("%d", &tc);

    for(int i = 0; i < tc; i++)
    {
        scanf("%s %d", S, &K);
        done = 0;
        flip = 0;
        finish = false;

        length = strlen(S);

        for(int j = 0; j < length; j++)
        {
            if(S[j] == '-')
            {
                done = 0;
                if(j+K <= length)
                {
                    for(int y = 0; y < K; y++)
                    {
                        if(S[j+y] == '-')
                            S[j+y] = '+';
                        else
                            S[j+y] = '-';
                    }
                    j = -1;
                    flip++;
                }
                else
                {
                    finish = false;
                    break;
                }
            }
            else
            {
                done++;
            }

            if(done == length)
            {
                finish = true;
                break;
            }

        }

        if(finish == true)
            printf("Case #%d: %d\n", i+1, flip);
        else
            printf("Case #%d: IMPOSSIBLE\n", i+1);
    }


    return 0;
}
