#include<stdio.h>
#include <iostream>
#include<string.h>
char s[1010];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t,icase=0;
    scanf("%d",&t);
    while(t--)
    {
        int sum=0;
        scanf("%s",s);
        int k;
        scanf("%d",&k);
        int len;
        len=strlen(s);
        printf("Case #%d: ",++icase);
        if(k>len)printf("IMPOSSIBLE\n");
        else
        {
            for(int i = 0; i < len-k+1; i++)
            {
                if(s[i]=='-')
                {
                    for(int j = i; j < i+k; j++)
                    {

                        if(s[j]=='-')s[j]='+';
                        else s[j]='-';
                    }
                    sum++;
                }
            }
            int flag=0;
            for(int i = len-k; i < len; i++)
                if(s[i]=='-')
            {
                flag=1;
                break;
            }
            if(flag==1)printf("IMPOSSIBLE\n");
            else printf("%d\n",sum);
        }
    }
}
/*
3
---+-++- 3
+++++ 4
-+-+- 4
*/
