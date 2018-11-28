#include<bits/stdc++.h>
using namespace std;
int n;
int num[20];
char str[20];
long long ans;
void dfs(int pos,long long val,int flag)
{
    if(pos==0)
    {
        dfs(pos+1,val*10+num[pos],flag);
        dfs(pos+1,val*10+num[pos]-1,1);
    }
    else if(pos==n)
    {
        ans=max(ans,val);
        return ;
    }
    else
    {
        if(flag)
            dfs(pos+1,val*10+9,flag);
        else
        {
            if(num[pos]>=num[pos-1])
            {
                dfs(pos+1,val*10+num[pos],flag);
            }
            if(num[pos]-1>=num[pos-1])
                dfs(pos+1,val*10+num[pos]-1,1);
        }
    }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%s",str);
        n=strlen(str);
        for(int i=0;i<n;i++)num[i]=str[i]-'0';
        ans=0;
        dfs(0,0,0);
        printf("Case #%d: %lld\n",cas,ans);
    }
    return 0;
}
