#include <bits/stdc++.h>
using namespace std;
int t,i,n,q,j,k;
double e[111],s[111],d[111][111],ans;//d[i][j]=i->j
void dfs(int x,int h,double l,double t)//x=도시 h=말 l=남은 거리 t=시간
{
    if(x==n)
    {
        if(ans>t)
            ans=t;
        return;
    }
    if(x!=1 && e[x]>=d[x][x+1])
        dfs(x+1,x,e[x]-d[x][x+1],t+d[x][x+1]/s[x]);
    if(l>=d[x][x+1])
        dfs(x+1,h,l-d[x][x+1],t+d[x][x+1]/s[h]);
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);
    for(scanf("%d",&t);i<t;i++)
    {
        scanf("%d%d",&n,&q);
        for(j=1;j<=n;j++)
            scanf("%lf%lf",&e[j],&s[j]);
        for(j=1;j<=n;j++)
            for(k=1;k<=n;k++)
                scanf("%lf",&d[j][k]);
        scanf("%d%d",&j,&k);
        ans=1e308;
        dfs(1,1,e[1],0);
        printf("Case #%d: %f\n",i+1,ans);
    }
}
