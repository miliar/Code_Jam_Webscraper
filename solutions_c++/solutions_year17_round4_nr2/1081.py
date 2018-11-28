

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#define pb push_back
#define mp make_pair
#define eps 1e-9
#define zero(x) (fabs(x)<eps)
#define pi acos(-1.0)
#define f1 first
#define f2 second
#define ms(x,y) memset(x,y,sizeof(x))
using namespace std;
typedef long long LL;
typedef pair <int, int> PII;
template<typename X> inline bool minimize(X&p,X q){if(p<=q)return 0;p=q;return 1;}
template<typename X> inline bool maximize(X&p,X q){if(p>=q)return 0;p=q;return 1;}
#define fr(i,x,y) for(int i=x;i<=y;i++)

#define MAXN 4010
#define MAXM 5000000
#define inf 300000
#define INF 300000

struct edge{
    int cost, cap, v;
    int next, e;
}e[MAXM];
int ans,ans1;
int cost,ss,tt,n;
int head[MAXN], o;
int vis[MAXN];
int m,nn,c;
int p[1005],r[1005],ren[1005],idd[1005];

void init()
{
    memset(head,-1,sizeof(head));
    o = 0;
    ans = cost = ans1=0;
}
void add(int u, int v, int cap, int cost)
{
    e[o].v = v;
    e[o].cap = cap;
    e[o].cost = cost;
    e[o].next =head[u];
    head[u]=o++;

    e[o].v = u;
    e[o].cap = 0;
    e[o].cost = -cost;
    e[o].next = head[v];
    head[v]=o++;
}

int aug(int u, int flow)
{
    if (u == tt)
    {   ans1 += flow;
        ans += cost * flow;
        return flow;
    }
    vis[u] =1;
    int tmp=flow;
    for (int i =head[u]; i!=-1; i=e[i].next)
        if (e[i].cap && !vis[e[i].v] && !e[i].cost)
        {
            int add= aug(e[i].v, tmp<e[i].cap?tmp:e[i].cap);
            e[i^1].cap += add;
            e[i].cap -= add;
            tmp-=add;
            if (!tmp) return flow;
        }
    return flow-tmp;
}

bool modifylabel()
{
    int add= INF;
    for(int u=1;u<=n;u++)
        if (vis[u])
            for(int i=head[u];i!=-1;i=e[i].next)
                if (e[i].cap && !vis[e[i].v] && e[i].cost<add)
                    add=e[i].cost;
    if (add==INF) return 0;
    for (int u=1;u<=n;u++)
        if (vis[u])
            for (int i=head[u];i!=-1;i=e[i].next)
                e[i].cost-=add,e[i^1].cost+=add;
    cost+=add;
    return 1;

}

void costflow()
{
    do{
        do{
            memset(vis,0,sizeof(vis));
        }while (aug(ss,tt));
    }while (modifylabel());

}

bool ok(int x){

    init();
    int o=0;
    ss=1;
    tt=2;
    fr(i,1,nn){
        add(ss,i+2,x,0);
        if (i!=nn)add(i+2,i+1+2,inf,1);
    }
    o=nn+2;
    fr(i,1,m){
        add(p[i]+2,o+i,1,0);
        idd[i]=o+i;
    }
    o+=m;
    fr(i,1,c) ren[i]=o+i;

    fr(i,1,m){
        add(idd[i],ren[r[i]],1,0);
    }
    o+=c;
    fr(j,1,c) fr(i,1,x){
        add(ren[j],i+o,1,0);
    }

    fr(i,1,x) add(i+o,tt,inf,0);
    n=x+o;
    costflow();

    //printf("~~~~~~`%d %d %d\n",x,ans,ans1);

    if (ans1==m) return 1;
    else return 0;
}
void doit()
{

    scanf("%d%d%d", &nn,&c, &m);

    for(int i = 1; i <=m; i++)
        scanf("%d%d",&p[i],&r[i]);


    int l=1,rr=m,mid,anss,anss2;
    while (l<=rr){
        mid=(l+rr)/2;
        if (ok(mid)) {
            anss=mid;
            rr=mid-1;
            anss2=ans;
        }
        else l=mid+1;
    }
    printf("%d %d\n",anss,anss2);
}
int main() {

   freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int cas,i=0;
    scanf("%d",&cas);
    while (cas--)
    {
            printf("Case #%d: ",++i);
            doit();

    }


}

