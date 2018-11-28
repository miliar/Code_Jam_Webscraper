//cdoj 92 LCA
#include<bits/stdc++.h>
#define maxn 100009
#define inf 0x3f3f3f3f
#define mod 1000000007
#define Mat_size 11
#define sha 99999999
using namespace std;
int way[maxn][25],lca[maxn][25],ans[maxn],dep[maxn],cnt,n,m,r1,r2,r3;
vector< pair<int,int> > g[maxn];
struct que
{
   int x,y;
}q[maxn];

void init()
{
    cnt=1;
    memset(lca,0,sizeof(lca));
    memset(way,0,sizeof(way));
    memset(dep,0,sizeof(dep));
    memset(ans,0,sizeof(ans));
    for(int i=0;i<=n;i++)
      g[i].clear();
}

void dfs(int a,int b,int d)
{
    dep[a]=d;
    for(int i=0;i<g[a].size();i++)
    {
        int j=g[a][i].first;
        int jj=g[a][i].second;
        if(j==b)
            continue;
        lca[j][0]=a;
        way[j][0]=jj;
        //printf("shabi %d %d\n",j,a);
        dfs(j,a,d+1);
    }
}

void _lca()
{
    for(int i=1;i<=20;i++)
    {
        for(int j=1;j<=n;j++)
        {
            if(lca[j][i-1])
            {
                lca[j][i]=lca[lca[j][i-1]][i-1];
                //printf("lca %d  %d  %d\n",j,i,lca[j][i]);
                way[j][i]=way[lca[j][i-1]][i-1]+way[j][i-1];
                //printf("way %d  %d  %d\n",way[lca[j][i-1]][i-1],way[j][i-1],way[j][i]);
            }
        }
    }
}

int query(int a,int b)
{
    int an=0;
    if(dep[a]<dep[b])
        swap(a,b);
    for(int i=20;i>=0;i--)
    {
        if(dep[a]-(1<<i)>=dep[b])
        {
            an+=way[a][i];
            a=lca[a][i];
        }
    }
    if(a==b)
        return an;
    //printf("1 a=%d b=%d\n",a,b);
    for(int i=20;i>=0;i--)
    {
        if(lca[a][i]!=lca[b][i])
        {
            an+=(way[a][i]+way[b][i]);
            //printf("a=%d b=%d i=%d\n",lca[a][i],lca[b][i],i);
            a=lca[a][i];
            b=lca[b][i];
        }
    }
    //printf("a=%d b=%d\n",a,b);
    return an+way[a][0]+way[b][0];
}

int main()
{
    //freopen("d:\\in.txt","r",stdin);
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d:\n",cas++);
        init();
        lca[1][0]=0;
        scanf("%d%d",&n,&m);
        for(int i=1;i<n;i++)
        {
            int a,b,c;
            scanf("%d%d%d",&a,&b,&c);
            g[a].push_back(make_pair(b,c));
            g[b].push_back(make_pair(a,c));
        }
        scanf("%d%d%d",&r1,&r2,&r3);
        dfs(1,1,1);
        _lca();
        for(int i=1;i<=m;i++)
        {
            int a,b;
            scanf("%d%d",&a,&b);
            q[i].x=a;
            q[i].y=b;
            int l1=query(a,b);
            int l2=min(query(a,r1)+query(b,r2)+r3,query(b,r1)+query(a,r2)+r3);
            if(l2<l1)
                ans[i]=l1-l2;
            else
                ans[i]=0;
            printf("%d\n",ans[i]);
        }
    }
    return 0;
}
