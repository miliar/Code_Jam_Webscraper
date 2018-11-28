#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
typedef long long LL;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("data.txt", "r", stdin);
    freopen("out.txt","w",stdout);
#endif

    int cases, len;
    char in[1024], *p;
    scanf("%d\n", &cases);
    for (int c = 1; c <= cases; c++)
    {
        printf("Case #%d: ", c);
        scanf("%s", in);
        len = strlen(in);
        for (int i = 1; i < len; i++)
        {
            if (in[i] < in[i - 1])
            {
                memset(in + i, '9', sizeof(char) * (len - i));

                for (int j = i - 1; j >= 0; j--)
                {
                    if (in[j] == '0' || (j > 0 && (in[j] - 1) < in[j - 1]))
                    {
                        if (j == 0)
                            in[0] = '0';
                        else
                            in[j] = '9';
                    }
                    else
                    {
                        in[j]--;
                        break;
                    }
                }
                break;
            }
        }

        p = in;
        if (in[0] == '0')
            p++;
        printf("%s\n", p);
    }
    return 0;

}
