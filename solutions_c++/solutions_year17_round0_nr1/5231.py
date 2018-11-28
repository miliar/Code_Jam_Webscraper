#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
typedef long long LL;

#define FLIP(c) (c == '+' ? '-' : '+')
int main()
{
#ifndef ONLINE_JUDGE
    freopen("data.txt", "r", stdin);
    freopen("out.txt","w",stdout);
#endif

    int cases, ans, len, k;
    char in[2048];
    scanf("%d\n", &cases);
    for (int c = 1; c <= cases; c++)
    {
        printf("Case #%d: ", c);
        scanf("%s %d", in, &k);
        ans = 0;
        len = strlen(in);
        for (int i = 0; i < len; i++)
        {
            if (in[i] == '-')
            {
                if (i + k > len)
                {
                    ans = -1;
                    break;
                }
                else
                {
                    for (int j = i; j <= i + k - 1; j++)
                        in[j] = FLIP(in[j]);
                    ans++;
                }
            }
        }
        if (ans < 0)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", ans);

    }
    return 0;

}
