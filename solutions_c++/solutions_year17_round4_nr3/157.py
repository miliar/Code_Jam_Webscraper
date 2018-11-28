#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<sstream>
using namespace std;
typedef long long lld;
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define eps 1e-8
#define pi acos(-1.0)
#define MAXN 1010
struct Edge
{
	int u,v,next;
}edge[2000010];
int head[2000010];
int pos;
void insert(int x,int y)
{
	edge[pos].u=x;
	edge[pos].v=y;
	edge[pos].next=head[x];
	head[x]=pos++;
}
int dfsn[MAXN];
bool vis[MAXN];
int low[MAXN];
int stack[MAXN];
int scc[MAXN];
int front;
int number;
int pre;
bool Instack[MAXN];
void dfs(int now)
{
	int i,v;
	stack[++front]=now;
	vis[now]=true;
	dfsn[now]=low[now]=pre++;
	Instack[now]=true;
	for(i=head[now];i;i=edge[i].next)
	{
		v=edge[i].v;
		if(vis[v])
		{
			if(Instack[v])
				low[now]=min(low[now],dfsn[v]);
			continue;
		}
		dfs(v);
		low[now]=min(low[now],low[v]);
	}
	if(low[now] == dfsn[now])
	{
		number++;
		do
		{
			v=stack[front--];
			scc[v]=number;
			Instack[v]=false;
		}while(v!=now);
	}
}
void init()
{
	memset(dfsn,0,sizeof(dfsn));
	memset(low,0,sizeof(low));
	memset(vis,false,sizeof(vis));
	memset(Instack,false,sizeof(Instack));
	pre=1;
	number=0;
	memset(head,0,sizeof(head));
	pos=1;
}
int anti[100010];
int color[100010];
int n,m;
vector<int>ooxx[100010];
int in[100010];
int queue[100010];
int ffront,rear;
int T;
char str[110][110];
int id[110][110];
void solve()
{
	int x,y;
	memset(in,0,sizeof(in));
	memset(color,-1,sizeof(color));
	for(int i=0;i<T*2;i++)
		ooxx[i].clear();
	for(int i=0;i<T;i++)
	{
		anti[scc[i]]=scc[i+T];
		anti[scc[i+T]]=scc[i];
	}
	for(int i=1;i<pos;i++)
	{
		x=edge[i].u;
		y=edge[i].v;
		if(scc[x] == scc[y])
			continue;
		ooxx[scc[y]].push_back(scc[x]);
		in[scc[x]]++;
	}
	ffront=0;
	rear=0;
	for(int i=1;i<=number;i++)
		if(in[i] == 0)
			queue[rear++]=i;
	int now;
	int v;
	while(rear != ffront)
	{
		now=queue[ffront++];
		if(color[now] == -1)
		{
			color[now]=1;
			color[anti[now]]=0;
		}
		for(int i=0;i<(int)ooxx[now].size();i++)
		{
			v=ooxx[now][i];
			in[v]--;
			if(in[v] == 0)
				queue[rear++]=v;
		}
	}
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			if(str[i][j] == '|' || str[i][j] == '-')
			{
				int at=id[i][j];
				if(color[scc[at]] == 0)
					str[i][j]='|';
				else
					str[i][j]='-';
			}
}
bool inside(int x,int y)
{
	return x >= 0 && x < n && y >= 0 && y < m;
}
int lll(int x,int y)
{
	while(1)
	{
		y--;
		if(!inside(x,y))
			return -1;
		if(str[x][y] == '#')
			return -1;
		if(str[x][y] == '|' || str[x][y] == '-')
			return id[x][y];
	}
}
int rrr(int x,int y)
{
	while(1)
	{
		y++;
		if(!inside(x,y))
			return -1;
		if(str[x][y] == '#')
			return -1;
		if(str[x][y] == '|' || str[x][y] == '-')
			return id[x][y];
	}
}
int ddd(int x,int y)
{
	while(1)
	{
		x++;
		if(!inside(x,y))
			return -1;
		if(str[x][y] == '#')
			return -1;
		if(str[x][y] == '|' || str[x][y] == '-')
			return id[x][y];
	}
}
int uuu(int x,int y)
{
	while(1)
	{
		x--;
		if(!inside(x,y))
			return -1;
		if(str[x][y] == '#')
			return -1;
		if(str[x][y] == '|' || str[x][y] == '-')
			return id[x][y];
	}
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++)
			scanf("%s",str[i]);
		T=0;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				if(str[i][j] == '|' || str[i][j] == '-')
					id[i][j]=T++;
		init();
		bool ok=true;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
			{
				if(str[i][j] == '.')
				{
					int l=lll(i,j);
					int r=rrr(i,j);
					int d=ddd(i,j);
					int u=uuu(i,j);
					int x,y;
					if(l != -1 && r != -1)
						x=-1;
					else if(l == -1 && r == -1)
						x=-1;
					else
						x=max(l,r);
					if(d != -1 && u != -1)
						y=-1;
					else if(d == -1 && u == -1)
						y=-1;
					else
						y=max(d,u);
					if(x == -1 && y == -1)
						ok=false;
					if(x == -1)
						insert(y,y+T);
					else if(y == -1)
						insert(x+T,x);
					else
					{
						insert(x+T,y+T);
						insert(y,x);
					}
				}
				if(str[i][j] == '|' || str[i][j] == '-')
				{
					int now=id[i][j];
					int l=lll(i,j);
					int r=rrr(i,j);
					int d=ddd(i,j);
					int u=uuu(i,j);
					if(l != -1 || r != -1)
						insert(now,now+T);
					if(d != -1 || u != -1)
						insert(now+T,now);
				}
			}
		if(!ok)
		{
			printf("Case #%d: IMPOSSIBLE\n",cc);
			continue;
		}
		for(int i=0;i<T*2;i++)
			if(!vis[i])
			{
				front=-1;
				dfs(i);
			}
		bool flag=true;
		for(int i=0;i<T && flag;i++)
			if(scc[i] == scc[i+T])
				flag=false;
		if(flag)
		{
			printf("Case #%d: POSSIBLE\n",cc);
			solve();
			for(int i=0;i<n;i++)
				printf("%s\n",str[i]);
		}
		else
			printf("Case #%d: IMPOSSIBLE\n",cc);
	}
	return 0;
}
/*
3
1 3
-.-
3 4
#.##
#--#
####
2 2
-.
#|

 */
