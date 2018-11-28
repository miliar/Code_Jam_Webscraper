#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int t;
char s[25];

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d",&t);
    int z=1;
    while(t--)
    {
        scanf("%s",s);
        int len=strlen(s);
        for(int i=len-1;i>0;--i)
        {
            if(s[i]<s[i-1])
            {
                s[i-1]--;
                for(int j=i;j<len;++j)
                    s[j]='9';
            }
        }
        int i=0;
        for(i;i<len;++i)
            if(s[i]!='0') break;
        printf("Case #%d: ",z++);
        printf("%s\n",s+i);
    }
}
