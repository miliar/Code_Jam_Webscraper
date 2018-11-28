#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <queue>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

#define INF 1000000000000000000

int delx[4]={0,0,-1,1};
int dely[4]={-1,1,0,0};

int trans_R[4]={2, 3, 0, 1};
int trans_L[4]={3, 2, 1, 0};

int n,m; 

char room[60][60];
int vis[60][60][5], v2[60][60];
int item[60][60], eid[60][60];

void trace(int i, int j, int d)
{
	int first=1;
	while (1)
	{
		if (vis[i][j][d]) break;
		if (!first) vis[i][j][d]=1;
		first=0;
		i+=delx[d]; j+=dely[d];
		if (i<1 || i>n || j<1 || j>m) break;
		if (room[i][j]=='#') break;
		if (room[i][j]=='\\') d=trans_R[d];
		if (room[i][j]=='/') d=trans_L[d];
	}
}

vector< pair<int,int> > sol[5010];

int check(int id, int face)
{
	memset(v2, 0, sizeof v2);
	rep(i,1,n)
		rep(j,1,m)
			rep(k,0,3) 
				if (vis[i][j][k])
					v2[i][j]=1;
	
	rep(i,1,n)
		rep(j,1,m)
			if (v2[i][j] && item[i][j])
				return 0;
	
	rep(i,1,n)
		rep(j,1,m)
			if (v2[i][j] && eid[i][j])
			{
				sol[eid[i][j]].push_back(make_pair(id, face));
			}
	return 1;
}

const int u=5100,w=1000010;
int ver[w],nx[w],head[u],dfn[u],low[u],c[u],s[u],v[u];
int vx[w],vy[w],ans[u],du[u],opp[u];
int tot,num,t,p,i,j,x,y,e;
char cx,cy;

void add(int x,int y)
{
	//printf("%d %d\n",x,y);
	if (!num) {x--; y--;}
	if(!num) vx[++e]=x,vy[e]=y; else du[y]++;
	ver[++tot]=y,nx[tot]=head[x],head[x]=tot;
}

void tarjan(int x)
{
	int i;
	dfn[x]=low[x]=++num;
	s[++p]=x,v[x]=1;
	for(i=head[x];i;i=nx[i])
		if(!dfn[ver[i]])
		{
			tarjan(ver[i]);
			low[x]=min(low[x],low[ver[i]]);
		}
		else if(v[ver[i]])
			low[x]=min(low[x],low[ver[i]]);
	if(dfn[x]==low[x])
	{
		t++;
		do{i=s[p--],v[i]=0; c[i]=t;}while(i!=x);
	}
}

int posx[5010], posy[5010];
int all;

void topsort()
{
	queue<int> q;
	memset(head,0,sizeof(head));
	memset(ans,0,sizeof(ans));
	memset(du,0,sizeof(du));
	tot=0;
	for(i=1;i<=e;i++)
		if(c[vx[i]]!=c[vy[i]]) add(c[vy[i]],c[vx[i]]);
	for(i=1;i<=t;i++)
		if(!du[i]) q.push(i);
	while(q.size())
	{
		x=q.front(); q.pop();
		if(!ans[x]) ans[x]=1,ans[opp[x]]=2;
		for(i=head[x];i;i=nx[i])
			if(--du[ver[i]]==0) q.push(ver[i]);
	}
	for(i=0; i<all; i++) {
		if(ans[c[i]]==1) 
			room[posx[i+1]][posy[i+1]]='-';
		else
			room[posx[i+1]][posy[i+1]]='|';
	}
	
	rep(i,1,n) printf("%s\n",room[i]+1);
}

int can[5010][2];


void lemon()
{
	scanf("%d%d",&n,&m);
	rep(i,1,n) scanf("%s",room[i]+1);
	all=0;
	memset(item,0,sizeof item);
	rep(i,1,n) 
		rep(j,1,m) 
			if (room[i][j]=='-' || room[i][j]=='|') 
			{
				all++;
				item[i][j]=all;
				posx[all]=i; posy[all]=j;
			}
			
	int em_all=0;
	memset(eid,0,sizeof eid);
	rep(i,1,n)
		rep(j,1,m)
			if (room[i][j]=='.')
			{
				em_all++;
				eid[i][j]=em_all;
			}
			
	memset(sol,0,sizeof sol);
	memset(can,0,sizeof can);
	rep(i,1,n)
		rep(j,1,m)
			if (item[i][j])
			{
				memset(vis,0,sizeof vis);
				trace(i,j,0);
				trace(i,j,1);
				if (check(item[i][j], 0)) can[item[i][j]][0]=1;
				
				memset(vis,0,sizeof vis);
				trace(i,j,2);
				trace(i,j,3);
				if (check(item[i][j], 1)) can[item[i][j]][1]=1;
				
				if (!can[item[i][j]][0] && !can[item[i][j]][1])
				{
					printf("IMPOSSIBLE\n");
					return;
				}
			}
	
	rep(i,1,em_all)
		if (sol[i].size()>2)
		{
			fprintf(stderr, "wtf\n");
		}
	
	memset(head,0,sizeof(head));
	memset(dfn,0,sizeof(dfn));
	tot=num=p=t=e=0;
	
	rep(i,1,all)
	{
		if (!can[i][0]) add(i,i+all);
		if (!can[i][1]) add(i+all,i);
	}
	
	rep(i,1,em_all)
	{
		if (sol[i].size()==0)
		{
			printf("IMPOSSIBLE\n");
			return;
		}
		if (sol[i].size()==1)
		{
			int id=sol[i][0].first, face=sol[i][0].second;
			if (face==0) add(id+all, id);
			if (face==1) add(id, id+all);
		}
		if (sol[i].size()==2)
		{
			int id1=sol[i][0].first, face1=sol[i][0].second;
			int id2=sol[i][1].first, face2=sol[i][1].second;
			if (id1==id2) continue;
			add(id1+(1-face1)*all, id2+face2*all);
			add(id2+(1-face2)*all, id1+face1*all);
		}
	}
	
	int i;
	for(i=0;i<2*all;i++)
		if(!dfn[i]) tarjan(i);
		
	for(i=0;i<all;i++)
	{
		if(c[i]==c[all+i]) break;
		opp[c[i]]=c[all+i],opp[c[all+i]]=c[i];
	}
	if(i<all) {
		printf("IMPOSSIBLE\n");
		return;
	}
		
	printf("POSSIBLE\n");
	topsort();
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("C.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(i,1,tcase)
	{
		printf("Case #%d: ",i);
		lemon();
	}
	return 0;
}

