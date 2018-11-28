#include<stdio.h>
#include<cstring>
int t;
int k;
char s[1001];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int x = 0; x < t;x++)
    {
        scanf("%s %d",s,&k);
        int sol = 0;
        int l = strlen(s) - k;
        for(int y = 0; y <= l; y++)
        {
            if(s[y] == '-')
            {
                sol++;
                for(int z = 0; z < k; z++)
                {
                    if(s[y+z] == '-')
                        s[y+z] = '+';
                    else
                        s[y+z] = '-';
                }
            }
        }
        int c;
        for(c = 1; c < k; c++)
        {
            if(s[l+c] == '-')
                break;

        }
        printf("Case #%d: ",x + 1);
        if(c == k)
            printf("%d\n",sol);
        else
            printf("IMPOSSIBLE\n",sol);
    }

}
