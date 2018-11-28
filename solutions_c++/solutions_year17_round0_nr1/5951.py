#include<cstdio>
#include<cstring>
using namespace std;
int T,K,ans,len;
char s[1010];
bool judge()
{
    for(int i=len-1;i>=0;i--)
        if(s[i]=='-')
            return false;
    return true;
}
void deal(int pos)
{
    for(int i=pos;i<pos+K;i++)
        if(s[i]=='+')
            s[i]='-';
        else
            s[i]='+';
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%s%d",s,&K);
        len=strlen(s),ans=0;
        for(int i=0;i<=len-K;i++)
            if(s[i]=='-')
                ans++,deal(i);
        if(judge())
            printf("Case #%d: %d\n",t,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",t);
    }
    return 0;
}
