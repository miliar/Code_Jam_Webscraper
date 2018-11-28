#include <iostream>

typedef long long LL;

#include<cstring>
#define N 20
#define fr(i,x,y) for(int i=x;i<=y;i++)

LL dp[N][11];
int bit[N],len;
LL ten[N];
LL n;
inline int max(int a,int b){return a>b?a:b;}


LL dfs(int pos,int now,int limit)
{
    //printf("%d %d %d %d\n",pos,now,limit,bit[pos]);
    if (pos<=0) return 0;
    if (!limit&&dp[pos][now]!=-1)
    return dp[pos][now];


    int end=(limit?bit[pos]:9);
    LL re=0;
    int tt;
    for (int i=end;i>=now;i--)
    {   tt=max(now, i);
        re=dfs(pos-1,tt,limit && (end == i));

        if (re!=-1)
        {
            re+=ten[pos]*i;
            if (!limit) dp[pos][tt]=re;
            //printf("%d %d %d %d %lld\n",pos,now,limit,bit[pos],re);
            return re;
        }
    }
    re=-1;
    if (!limit) dp[pos][tt]=re;
    return re;


}
LL solve(LL n)
{   if (n==0) return 0;
    len=0;
    while (n)
    {   bit[++len]=n%10;
        n/=10;
    }
    ten[1]=1;
    for (int i=2;i<=18;i++)
            ten[i]=ten[i-1]*10;
    return dfs(len,0,1);
}







void doit()
{

    scanf("%lld",&n);
    printf("%lld\n",solve(n));

}






int main() {
    int cas;

    memset(dp,255,sizeof(dp));
    //printf("%lld\n",dp[0][0]);

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&cas);
    int id=0;
    while (cas--)
    {
        printf("Case #%d: ",++id);
        doit();
    }
    return 0;
}