#include <bits/stdc++.h>
using namespace std;
#define maxn 2200
#define maxm 3300000
#define inf 999999999

struct et
{
    int s,t,val,cost,next;
}e[maxm];
int fir[maxn],dis[maxn],vis[maxn],q[maxm],pre[maxn];
bool inque[maxn];
int st,ed,tot,ans,sum;
int n,m,c;
int x[maxn], y[maxn];


void prepare()
{
    for (int i=st;i<=ed;i++) dis[i]=inf;//min
    int head=0,tail=1;
    q[1]=ed; dis[ed]=0; inque[ed]=1;
    while (head<tail)
    {
        int now=q[++head];
        for (int j=fir[now];j;j=e[j].next)
        {
            int k=e[j].t;
            if (e[j^1].val&&dis[k]>dis[now]+e[j^1].cost)//min
            {
                dis[k]=dis[now]+e[j^1].cost;
                if (!inque[k]) q[++tail]=k,inque[k]=1;
            }
        }
        inque[now]=0;
    }
}

int dfs(int now,int flow)
{
    if (now==ed)
    {
    	ans+=flow;
        sum+=dis[st]*flow;
        return flow;
    }
    int sap=0;    vis[now]=1;
    for (int j=fir[now];j;j=e[j].next)
    {
        int k=e[j].t;
        if (!vis[k]&&e[j].val&&dis[now]==dis[k]+e[j].cost)
        {
            int tmp=dfs(k,min(e[j].val,flow-sap));
            e[j].val-=tmp;
            e[j^1].val+=tmp;
            sap+=tmp;
            if (sap==flow) return sap;
        }
    }
    return sap;
}

bool adjust()
{
    int tmp=inf;
    for (int i=st;i<=ed;i++) if (vis[i])
        for (int j=fir[i];j;j=e[j].next)
        {
            int k=e[j].t;
            if (!vis[k]&&e[j].val) tmp=min(tmp,dis[k]+e[j].cost-dis[i]);//min
        }
    if (tmp==inf) return 0;
    for (int i=st;i<=ed;i++) if (vis[i])
        dis[i]+=tmp;
    return 1;
}

void add_edge(int x,int y,int z,int w)
{
    e[++tot].s=x; e[tot].t=y; e[tot].val=z; e[tot].cost=w; e[tot].next=fir[x]; fir[x]=tot;
    e[++tot].s=y; e[tot].t=x; e[tot].val=0; e[tot].cost=-w; e[tot].next=fir[y]; fir[y]=tot;
}

int zkw_flow()
{
	ans=sum=0;
	prepare();
	do{
		do memset(vis,0,sizeof(vis));
		while (dfs(st,inf));
	}while (adjust());
}

int init()
{
	memset(fir,0,sizeof(fir));
	tot=1; st=0; ed=m+1;
}


int main()
{
	freopen("B-small.in","r",stdin);
	// freopen("B-large.in","r",stdin);
	freopen("B1.out","w",stdout);
	int Case;
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf("%d%d%d",&n,&c,&m);
		init();
		for (int i=1;i<=m;i++){
			scanf("%d%d",&x[i],&y[i]);
			if (y[i]==1) add_edge(st, i, 1, 0);
			else add_edge(i, ed, 1, 0);
		}
		for (int i=1;i<=m;i++)
			for (int j=1;j<i;j++){
				if (y[i]==y[j]) continue;
				if (y[i]>y[j]) swap(i, j);
				if (x[i]==x[j]){
					if (x[i]>1)
						add_edge(i, j, 1, 1);
				}
				else
					add_edge(i, j, 1, 0);
				if (i<j) swap(i, j);
			}
		// for (int j=2;j<=tot;j+=2)
		// 	cout<<e[j].s<<' '<<e[j].t<<' '<<e[j].val<<' '<<e[j].cost<<endl;
		
		zkw_flow();
		printf("Case #%d: %d %d\n",o, m-ans, sum);
	}
	return 0;
}