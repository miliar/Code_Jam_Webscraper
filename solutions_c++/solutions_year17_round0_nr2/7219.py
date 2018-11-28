#include<stdio.h>
#include <iostream>
#include<string.h>
char s[30];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t,icase=0;
    scanf("%d",&t);
    while(t--)
    {
        long long int sum=0;
        scanf("%s",s);
        int len;
        len=strlen(s);
        printf("Case #%d: ",++icase);
        int flag=0;
        if(len==1)
        {
            printf("%s\n",s);
            continue;
        }
        for(int i = 1; i < len; i++)
        {
            if(s[i]<s[i-1])
            {
                flag=i;
                break;
            }
        }
        //printf("*%d*\n",flag);
        if(flag==0)
        {
            printf("%s\n",s);
            continue;
        }
        else
        {
            int flag2=flag;
            s[flag-1]--;

            for(int i = flag-1; i > -1; i--)
            {
                if(i==0&&s[i]<='0')flag2=i;
                else
                {
                    if(s[i]<'0')
                    {
                        s[i]+=10;
                        s[i-1]-=1;
                    }
                    if(s[i]<s[i-1])
                    {
                        s[i-1]--;
                        flag2=i;
                    }
                }
            }
            //printf("%s %d\n",s,flag2);
            if(flag2==0)
            {
                for(int i = 1; i < len; i++)
                {
                    sum*=10;
                    sum+=9;
                }
            }
            else
            {
                for(int i = flag2; i < len; i++)
                    s[i]='9';
                for(int i = 0; i < len; i++)
                {
                    sum*=10;
                    sum+=s[i]-'0';
                }
            }
        }
        printf("%lld\n",sum);
    }
    return 0;
}
/*
4
132
1000
7
111111111111111110
*/

