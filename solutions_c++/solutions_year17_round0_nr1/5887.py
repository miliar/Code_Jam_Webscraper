#include <stdio.h>
#include <string.h>

char str[1002];
int k, len;

void flip(int idx)
{
    int i, j;
    for(i=0;i<k;i++)
    {
        j = idx+i;
        str[j] = str[j]=='+'?'-':'+';
    }
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int i, cc, t, ans;
    bool su;
    scanf("%d", &t);
    for(cc=1;cc<=t;cc++)
    {
        su = 1;
        ans = 0;
        scanf("%s%d", str, &k);
        len = strlen(str);
        for(i=0;i<len-k+1;i++)
        {
            if(str[i]=='-')
            {
                flip(i);
                ans++;
            }
        }
        for(;i<len;i++)
        {
            if(str[i]=='-')
            {
                su = 0;
                break;
            }
        }
        if(su)
        {
            printf("Case #%d: %d\n", cc, ans);
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n", cc);
        }
    }
    return 0;
}
