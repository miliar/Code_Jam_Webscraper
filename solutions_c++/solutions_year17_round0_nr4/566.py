#include <cstdio>
#include <cstring>
#include <iostream>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;
int a[103][103],N,b[103][103];
const int sz=410;
const int INF=1e9+9; 
const int MAXF=1e8;
struct EDG{int u,v,val;}edg[21800]; int fst[sz],nex[21800],en=1;
//isap
//附建图连边函数make_edg();
//传入一个边的基本信息完备（起点、终点、容量） 的网络edg， 
//以邻接链表形式存储，因此还包括fst[],nex[],以及总边数en，
//要求已经建好了双向边，且边的反向弧为相邻的编号，可以用异或1来得到；
//传入总点数tot，源为S，汇为T；
//常数MAXF为网络中可能出现的最大容量（常在建图连边时使用，人为设定为次级INF）；
//常数INF为一个比MAXF还要大的记为无穷的常数； 
//常数sz比点数稍大，isap函数内的数组都是关于点的。全局的sz与isap函数内部的sz有区别，注意区分。 
//isap()函数返回最大流 
int S,T;
int dis[sz],cur[sz],pre[sz],gap[sz];
void make_edg(int u,int v,int val)
{	en++; edg[en].u=u; edg[en].v=v; edg[en].val=val; nex[en]=fst[u]; fst[u]=en;
	en++; edg[en].u=v; edg[en].v=u; edg[en].val=0;   nex[en]=fst[v]; fst[v]=en;
}
void update(int &ans)
{	int x=INF;
	for(int v=T;v!=S;v=edg[pre[v]].u) if(x>edg[pre[v]].val) x=edg[pre[v]].val;
	for(int v=T;v!=S;v=edg[pre[v]].u){edg[pre[v]].val-=x; edg[pre[v]^1].val+=x;}
	ans+=x;
}
int isap(int tot)
{	memset(dis,0,sizeof(dis)); memset(cur,0,sizeof(cur)); memset(pre,0,sizeof(pre));
	memset(gap,0,sizeof(gap)); int sz=tot+3,ans=0; gap[0]=sz; //此处sz为重定义的点数+3，局部掩盖全局的sz，但没有关系 
	for(int u=S;dis[S]<sz;)
	{	int ok=0;
		if(u==T){update(ans); u=S;}
		for(int i=cur[u];i;i=nex[i]) if(edg[i].val&&dis[u]==dis[edg[i].v]+1)
		{
			ok=1; cur[u]=i; pre[edg[i].v]=i; u=edg[i].v; break;
		}
		if(ok==0)
		{	int k=sz-1; if(--gap[dis[u]]==0) break; //断层 
			for(int i=fst[u];i;i=nex[i]) if(edg[i].val>0&&k>dis[edg[i].v]) k=dis[edg[i].v];
			dis[u]=k+1; gap[dis[u]]++; cur[u]=fst[u];
			if(u!=S) u=edg[pre[u]].u;
		}
	}
	return ans;
}
//isap
short flagR[210],flagC[210];
void build1()
{	int i,j; S=N+N+1; T=N+N+2;
	mem(fst,0); en=1;
	mem(flagR,0); mem(flagC,0);
	for(i=1;i<=N;i++) for(j=1;j<=N;j++)
		if(a[i][j]==1||a[i][j]==3) flagR[i]=flagC[j]=1;
		else make_edg(i,N+j,1);
	for(i=1;i<=N;i++)
	{	if(!flagR[i]) make_edg(S,i,1);
		if(!flagC[i]) make_edg(N+i,T,1);
	}
}
void fill1()
{
	for(int i=2;i<=en;i++) if(edg[i].u<=N&&edg[i].v<=N+N&&edg[i].val==0) b[edg[i].u][edg[i].v-N]+=1;
}
void build2()
{	int i,j; S=401; T=402;
	mem(fst,0); en=1;
	mem(flagR,0); mem(flagC,0);
	for(i=1;i<=N;i++) for(j=1;j<=N;j++)
		if(a[i][j]==2||a[i][j]==3) flagR[i-j+N]=flagC[i+j]=1;
		else make_edg(i-j+N,i+j+200,1);
	for(i=1;i<=200;i++)
	{	if(!flagR[i]) make_edg(S,i,1);
		if(!flagC[i]) make_edg(200+i,T,1);
	}
}
void fill2()
{
	for(int i=2;i<=en;i++) if(edg[i].u<=200&&edg[i].v<=400&&edg[i].val==0)
		b[(edg[i].u+edg[i].v-N-200)/2][((edg[i].v-200)-(edg[i].u-N))/2]+=2;
}
int main()
{
//	freopen("D-large.in","r",stdin);
//	freopen("D-large.out","w",stdout);
	int cas; cin>>cas;
	for(int casi=1;casi<=cas;casi++)
	{	int M,i,j; cin>>N>>M;
		mem(a,0); mem(b,0);
		for(i=1;i<=M;i++)
		{	char ch[3]; int x,y;
			scanf("%s%d%d",ch,&x,&y);
			if(ch[0]=='x') a[x][y]=1;
			else if(ch[0]=='+') a[x][y]=2;
			else a[x][y]=3;
			b[x][y]=a[x][y];
		}
		build1(); isap(N+N+2); fill1();
		build2(); isap(402); fill2();
		int ans=0,ansk=0;
		for(i=1;i<=N;i++)
			for(j=1;j<=N;j++)
			{	if(b[i][j]==1) ans++;
				else if(b[i][j]==2) ans++;
				else if(b[i][j]==3) ans+=2;
				if(b[i][j]!=a[i][j]) ansk++;
			}
		printf("Case #%d: %d %d\n",casi,ans,ansk);
		for(i=1;i<=N;i++)
			for(j=1;j<=N;j++)
			{	if(b[i][j]!=a[i][j])
					if(b[i][j]==1) printf("x %d %d\n",i,j);
					else if(b[i][j]==2) printf("+ %d %d\n",i,j);
					else if(b[i][j]==3) printf("o %d %d\n",i,j);
			}
	}
	return 0;
}

