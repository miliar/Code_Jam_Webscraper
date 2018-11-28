#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<iomanip>
#include<vector>
#include<set>
#include<map>
#include<queue>

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

#define rep(i,k,n) for(int i=(k);i<=(n);i++)
#define rep0(i,n) for(int i=0;i<(n);i++)
#define red(i,k,n) for(int i=(k);i>=(n);i--)
#define sqr(x) ((x)*(x))
#define clr(x,y) memset((x),(y),sizeof(x))
#define pb push_back
#define mod 1000000007

const int maxn=5010;
const int maxm=8000010;
const int inf=0x3f3f3f3f;

struct edge
{
	int v,w,c,next;
}e[maxm];
int h[maxn],ecnt;

inline void addedge(int u,int v,int w,int c)
{
	e[ecnt]=(edge){v,w,c,h[u]};
	h[u]=ecnt++;
}
inline void Addedge(int u,int v,int w,int c)
{
	addedge(u,v,w,c);
	addedge(v,u,0,-c);
}

int dis[maxn],pre[maxn],peg[maxn];
bool vis[maxn];
int flow,cost;

bool spfa(int s,int t)
{
	clr(vis,0);clr(pre,-1);
	clr(dis,0x3f);
	queue<int> q;
	q.push(s);
	vis[s]=1;
	dis[s]=0;
	while(!q.empty())
	{
		int u=q.front();q.pop();vis[u]=0;
		for(int i=h[u];~i;i=e[i].next)
		{
			int v=e[i].v;
			if(e[i].w && dis[u]+e[i].c<dis[v])
			{
				dis[v]=dis[u]+e[i].c;
				pre[v]=u;
				peg[v]=i;
				if(!vis[v])q.push(v);
				vis[v]=1;
			}
		}
	}
	return dis[t]!=inf;
}

void mcf(int s,int t)
{
	flow=cost=0;
	while(spfa(s,t))
	{
		int mf=inf;
		for(int u=t;~pre[u];u=pre[u])mf=min(mf,e[peg[u]].w);
		for(int u=t;~pre[u];u=pre[u])
		{
			e[peg[u]].w-=mf;
			e[peg[u]^1].w+=mf;
		}
		flow+=mf;
		cost+=mf*dis[t];
	}
}



int n,c,m;
vector<int> a[5];

int main()
{
	freopen("C:\\tmpcode\\gcj\\2017\\r2\\b\\B-small-attempt1.in", "r", stdin);
	freopen("C:\\tmpcode\\gcj\\2017\\r2\\b\\mysmalloutput.txt", "w", stdout);
	int T;scanf("%d",&T);
	rep(ii,1,T)
	{
		scanf("%d%d%d",&n,&c,&m);
		rep(i,1,2)a[i].clear();
		rep(i,1,m)
		{
			int p,b;
			scanf("%d%d",&p,&b);
			a[b].pb(p);
		}
		int l=a[1].size();
		int r=a[2].size();
		
		clr(h,-1);ecnt=0;
		
		int src=0,des=l*2+r*2+1;
		rep(i,0,l-1)
		{
			int id=i+1;
			int rid=id+l;
			
			Addedge(src,id,1,0);
			Addedge(id,rid,1,0);
			rep(j,0,r-1)
			{
				int jid=l*2+j+1;
				if(a[1][i]==a[2][j] && a[1][i]!=1)Addedge(rid,jid,1,1);
				else if(a[1][i]!=a[2][j])Addedge(rid,jid,1,0);
			}
		}
		rep(j,0,r-1)
		{
			int id=l*2+j+1;
			int rid=id+r;
			Addedge(id,rid,1,0);
			Addedge(rid,des,1,0);
		}
		mcf(src,des);
		printf("Case #%d: %d %d\n",ii,m-flow,cost);
	}
	
	
	return 0;
}
