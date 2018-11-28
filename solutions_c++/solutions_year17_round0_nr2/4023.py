#include<stdio.h>
#include<string.h>
using namespace std;
typedef long long ll;
#define INF 0x3f3f3f3f
ll n;
int dig[20];
int len;
ll ans;
ll dfs(int p,int f,ll now,int pre)
{
    if(p==-1)
        return now;
    int top=f?dig[p]:9;
    if(top>=pre)
    {
        ll res=dfs(p-1,f&&top==dig[p],now*10+top,top);
        if(!res&&top-1>=pre) res=dfs(p-1,0,now*10+top-1,top-1);
        return res;
    }
    return 0;
}
void solve()
{
    ll tmp=n;
    len=0;
    while(tmp)
    {
        dig[len++]=tmp%10;
        tmp/=10;
    }
    ans=dfs(len-1,1,0,0);
    printf("%lld\n",ans);
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,tt=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld",&n);
        printf("Case #%d: ",++tt);
        solve();
    }
    return 0;
}
//111111111111111110
//111111111111111109
