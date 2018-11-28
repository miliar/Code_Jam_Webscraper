#include <bits/stdc++.h>
using namespace std;

char *solve(char *s)
{
    int len=strlen(s);
    for(int k=0; k<len; k++)
    {
        for(int i=0; i<len-1; i++)
        {
            if(s[i]>s[i+1] && s[i]!='0')
            {
                s[i]--;
                for(int j=i+1; j<len; j++) s[j]='9';
            }
        }
    }
    if(s[0]=='0')
    {
        for(int i=0; i<len-1; i++)
        {
            s[i]=s[i+1];
        }
        s[len-1]=0;
    }
    return s;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int t,n;
    char str[101];
    scanf("%d",&t);
    for(int x=1; x<=t; x++)
    {
        scanf("%s",str);
        printf("Case #%d: ",x);
        printf("%s\n",solve(str));
        str[0]=0;
    }
    return 0;
}
