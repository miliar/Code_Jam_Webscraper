#include<stdio.h>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <numeric>
#include <queue>
#include <map>
#include <set>
#include <string.h>
#include <functional>
typedef long long ll;
using namespace std;
const double PI=acos(-1.0);
struct node1
{
    double r,h,sh,sr;
}node[1010];
bool cmp1(node1 p1,node1 p2)
{
    if(p1.r!=p2.r)
        return p1.r>p2.r;
    return p1.h>p2.h;
}
double dp[1010][1010];
double maxx[1010][1010];

double dfs(int x,int y)
{
    if(dp[x][y]!=0)
        return dp[x][y];
    for(int i=y-1;i>=1;i--)
    {
        dp[x][y]=max(dp[x][y],dfs(x-1,i));
    }
    dp[x][y]+=node[y].sh;
    return dp[x][y];
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int v=1;v<=t;v++)
    {
        memset(dp,0,sizeof(dp));
        int n,k;
        scanf("%d%d",&n,&k);
        for(int i=1;i<=n;i++)
        {
            scanf("%lf%lf",&node[i].r,&node[i].h);
        }
        sort(node+1,node+n+1,cmp1);
        double ans=0;
        for(int i=1;i<=n;i++)
        {
            node[i].sr=PI*node[i].r*node[i].r;
            node[i].sh=2*PI*node[i].r*node[i].h;
        }
        for(int i=1;i<=n;i++)
        {
            dp[1][i]=node[i].sh+node[i].sr;
        }
        for(int i=k;i<=n;i++)
        {
            ans=max(ans,dfs(k,i));
        }
        printf("Case #%d: %.8lf\n",v,ans);
    }
    return 0;
}
