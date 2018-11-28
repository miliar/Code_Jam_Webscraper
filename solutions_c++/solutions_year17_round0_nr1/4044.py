#include <string>
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int K,len;
char s[1100];
void deal(int l,int r)
{
    for(int i=l;i<=r;i++)
        s[i]=s[i]=='+'?'-':'+';
}
int solve()
{
    int res=0;
    for(int i=0;i+K-1<len; i++)
    {
        if(s[i]=='-')
        {
            deal(i,i+K-1);
            res++;
        }
    }
    for(int i=0;i<len;i++)
        if(s[i] == '-') return -1;
    return res;
}

int main()
{
    //freopen("A.in","r",stdin);
    //freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        printf("Case #%d: ",cas);
        scanf("%s",s);
        len=strlen(s);
        scanf("%d",&K);
        int ans=solve();
        if(ans==-1) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
