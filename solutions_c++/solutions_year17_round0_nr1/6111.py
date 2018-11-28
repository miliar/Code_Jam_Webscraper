#include <stdio.h>
#include <string.h>

const int MX = 1010;

int k;
char s[MX];

int main()
{
    int T;
    scanf("%d", &T);
    for(int ca=1;ca<=T;ca++)
    {
        scanf("%s%d", s, &k);
        int len = strlen(s);
        int step = 0;
        for(int i=0;i+k<=len;i++)
        {
            if( s[i] == '+' ) continue;
            step++;
            for(int j=i;j<i+k;j++)
            {
                s[j] = ('+' == s[j]) ? '-' : '+';
            }
        }
        bool bFailed = false;
        for(int i=0;i<len;i++)
        {
            if( s[i] != '+' ) bFailed = true;
        }
        if( bFailed )
        {
            printf("Case #%d: IMPOSSIBLE\n", ca);
        }
        else
        {
            printf("Case #%d: %d\n", ca, step);
        }
    }

    return 0;
}

