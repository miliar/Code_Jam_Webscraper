#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define maxn 1005
char s[maxn];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        int a;
        scanf("%s%d",s,&a);
        int len=strlen(s);
        int ans=0;
        for(int i=0;i<len;i++)
        {
            if(s[i]=='+') continue;
            if(i+a>len)
            {
                ans=-1;
                break;
            }
            for(int j=i;j<i+a;j++)
            {
                if(s[j]=='+') s[j]='-';
                else s[j]='+';
            }
            ans++;
        }
        if(ans==-1) printf("Case #%d: IMPOSSIBLE\n",cas);
        else printf("Case #%d: %d\n",cas,ans);
    }
}
