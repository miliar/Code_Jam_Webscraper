#include <stdio.h>
#include <string.h>

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int i, j, t, cc, len;
    char num[30];
    scanf("%d", &t);
    for(cc=1;cc<=t;cc++)
    {
        scanf("%s", num);
        len = strlen(num);
        for(i=len-2;i>=0;i--)
        {
            if(num[i]>num[i+1])
            {
                for(j=i+1;j<len;j++)
                {
                    num[j] = '9';
                }
                num[i] -= 1;
            }
        }
        printf("Case #%d: ", cc);
        for(i=0;i<len;i++)
        {
            if(num[i]!='0')
            {
                break;
            }
        }
        for(;i<len;i++)
        {
            putchar(num[i]);
        }
        putchar('\n');
    }
    return 0;
}
