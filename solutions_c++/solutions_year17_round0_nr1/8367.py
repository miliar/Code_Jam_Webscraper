#include <stdio.h>
char c[1001];
int main()
{
    int t,ans,flag,len,k;
    scanf("%d", &t);
    for(int i=1; i<=t; ++i)
    {
        for(int j=0; j<1000; ++j)
        {
            c[j]='\0';
        }
        ans=0; flag=0;
        for(int j=0; true; ++j)
        {
            scanf("%c", &c[j]);
            if(c[j]==' ') {
                c[j]='\0';
                len=j;
                break;
            }
            if(c[j]!='-' && c[j]!='+')
            {
                c[j]='\0';
                j--;
            }
        }
        scanf("%d", &k);
        for(int j=0; j<=len-k; ++j)
        {
            if(c[j]=='-')
            {
                ans++;
                for(int e=j; e<j+k; e++)
                {
                    if(c[e]=='-')
                        c[e]='+';
                    else
                        c[e]='-';
                }
            }
           // printf("%s\n", c);
        }
        for(int j=0; j<=len; ++j)
        {
            if(c[j]=='-')
            {
                flag=1;
                break;
            }
        }
        if(flag==1) printf("Case #%d: IMPOSSIBLE\n", i);
        else printf("Case #%d: %d\n", i, ans);

    }
}
