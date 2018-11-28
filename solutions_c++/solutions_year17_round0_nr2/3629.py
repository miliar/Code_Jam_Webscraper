#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define maxn 1005
char s[maxn];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        scanf("%s",s);
        int len=strlen(s);
        for(int i=0;i<len-1;i++)
        {
            if(s[i]>s[i+1])
            {
                int idx=i;
                while(idx>0&&s[idx]<=s[idx-1])
                {
                    idx--;
                }
                s[idx]=s[idx]-1;
                for(int j=idx+1;j<len;j++) s[j]='9';
            }
        }
        int idx=0;
        for(int i=0;i<len;i++) if(s[i]!='0')
        {
            idx=i;
            break;
        }
        printf("Case #%d: %s\n",cas,s+idx);
    }
}
