//#345 div.1 E dfs+Í¼ÂÛ
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<set>
#include<queue>
#define maxn 500009
#define inf 0x3f3f3f3f
#define mod 1000000007
#define Mat_size 11
using namespace std;
int n,m,_fa[maxn],fa[2][maxn];
struct e
{
    int a,b,c,d;
};
vector<e> ii;
vector<int> g[2][maxn];

int far(int a)
{
    if(_fa[a]==a)
        return a;
    return _fa[a]=far(_fa[a]);
}

void uni(int a,int b)
{
    _fa[b]=a;
}

void dfs(int id,int a,int b)
{
    for(int i=0;i<g[id][a].size();i++)
    {
        int j=g[id][a][i];
        if(j==b)
            continue;
        fa[id][j]=a;
        dfs(id,j,a);
    }
}

void solve(int a,int b)
{
    for(int i=0;i<g[0][a].size();i++)
    {
        int j=g[0][a][i];
        if(j==b)
            continue;
        solve(j,a);
        if(fa[1][a]!=j&&fa[1][j]!=a)
        {
            e t;
            t.a=a;t.b=j;t.c=far(j);t.d=fa[1][t.c];
            ii.push_back(t);
            uni(t.d,t.c);
        }
    }
}

int main()
{
    //freopen("d:\\in.txt","r",stdin);
    scanf("%d",&n);
    for(int i=1;i<n;i++)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        g[0][a].push_back(b);
        g[0][b].push_back(a);
    }
    for(int i=1;i<n;i++)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        g[1][a].push_back(b);
        g[1][b].push_back(a);
    }
    dfs(1,1,0);
    dfs(0,1,0);
    for(int i=1;i<=n;i++)
    {
        int j=fa[1][i];
        if(fa[0][i]==j||fa[0][j]==i)
            _fa[i]=j;
        else
            _fa[i]=i;
    }
    solve(1,0);
    printf("%d\n",ii.size());
    for(int i=0;i<ii.size();i++)
    {
        e tt=ii[i];
        printf("%d %d %d %d\n",tt.a,tt.b,tt.c,tt.d);
    }
    return 0;
}