#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<string>
#include<string.h>
using namespace std;
char s[30];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b1.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s);
        int len=strlen(s);
        printf("Case #%d: ",++ca);
        if(len==1)
        {
            puts(s);
            continue;
        }
        int cur='0';
        int id=-1;
        for(int i=1;s[i];++i)
        {
            if(s[i]<s[i-1])
            {
                id=i;
                break;
            }
        }

        if(id==-1)
        {
            puts(s);
        }
        else
        {
            int id2=-1;
            for(int i=id-1;i>=1;i--)
                if(s[i]!=s[i-1])
                {
                    id2=i;
                    break;
                }
            if(id2==-1)
            {
                if(s[0]=='1')
                {
                    for(int i=1;i<len;++i)
                        putchar('9');
                }
                else
                {
                    putchar(s[0]-1);
                    for(int i=1;i<len;++i)
                        putchar('9');
                }
                puts("");
            }
            else
            {
                s[id2]--;
                for(int i=id2+1;i<len;++i)
                    s[i]='9';
                puts(s);
            }

        }

    }
}
